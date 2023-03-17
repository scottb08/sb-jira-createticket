# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sys
import os
import tempfile
from pprint import pprint, pformat

# These paths needed for the Jira python package
path = os.path.join(os.path.dirname(__file__), 'site-packages')
if path not in sys.path:
    sys.path.append(path)

import sgtk
from jira import JIRA

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

screen_grab = sgtk.platform.import_framework("tk-framework-qtwidgets", "screen_grab")
overlay_widget = sgtk.platform.import_framework("tk-framework-qtwidgets", "overlay_widget")

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)

# Global Variables
DEFAULT_PRIORITIES = ['Blocker', 'High', 'Medium', 'Low']


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog(app_instance.get_setting("display_name"), app_instance, AppDialog)


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """

    def __init__(self):
        """
        Constructor
        """
        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - An SGTK API instance, via self._app.sgtk

        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        self.projects = []
        self.screen_grab = None

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._overlay_widget = overlay_widget.ShotgunOverlayWidget(self)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()
        self.context = self._app.context

        # Get current user for ticket
        user = sgtk.get_authenticated_user().resolve_entity()
        self.user = self._app.shotgun.find_one(user['type'], [['id', 'is', user['id']]], ['name', 'login'])

        # Print version of the app being used
        self._app.logger.info(f'App version: {self._app.version}')

        # App settings
        self.jira_server_url = self._app.get_setting('jira_server_url')
        self.jira_service_acct = self._app.get_setting('jira_service_account')
        self.jira_server_pw = self._app.get_setting('jira_service_account_pw')
        self.jira_project_ids = self._app.get_setting('jira_project_ids')
        self.ticket_priorities = self._app.get_setting('ticket_priorities') or DEFAULT_PRIORITIES
        self.ui.priority_comboBox.addItems(self.ticket_priorities)

        self._connect_to_jira_server()
        self.update_jira_projects()

        # Signals
        self.ui.screen_capture_btn.clicked.connect(self._on_screen_capture_btn_clicked)
        self.ui.clear_capture_btn.clicked.connect(self._clear_results_pixmap)
        self.ui.jira_proj_comboBox.currentIndexChanged.connect(self._update_ui)
        self.ui.priority_comboBox.currentIndexChanged.connect(self._update_ui)
        self.ui.open_bug_radioButton.clicked.connect(self._update_ui)
        self.ui.feat_rqst_radioButton.clicked.connect(self._update_ui)
        self.ui.title_lineEdit.editingFinished.connect(self._update_ui)
        self.ui.descrpt_plainTextEdit.textChanged.connect(self._update_ui)
        self.ui.submitPushButton.released.connect(self._create_jira_issue)
        self.ui.log_pushButton.released.connect(self.browse_file)

        self._update_ui()

    def _connect_to_jira_server(self):
        try:
            self.jira = JIRA(options={'server': self.jira_server_url},
                             basic_auth=(self.jira_service_acct, self.jira_server_pw))

        except Exception as err:
            raise IOError(f'Failed to connect to Jira server.\n{err}')

    def update_jira_projects(self):
        projects = self.jira.projects()
        if not projects:
            raise ValueError(f'Unable to retrieve projects from Jira ({self.jira_server_url})')

        for proj in projects:
            for proj_id in self.jira_project_ids:
                if int(proj.id) == proj_id:
                    self.projects.append(proj)

        if not self.projects:
            raise ValueError('Jira Project id(s) defined in app '
                             'settings not found in Jira ({})'.format(', '.join(map(str, self.jira_project_ids))))

        if len(self.projects) < 2:
            self.ui.jira_proj_comboBox.clear()

        for proj in self.projects:
            self.ui.jira_proj_comboBox.addItem(proj.name, proj.id)

    def _create_jira_issue(self):
        project_id = self.ui.jira_proj_comboBox.itemData(self.ui.jira_proj_comboBox.currentIndex())
        title = self.ui.title_lineEdit.text()
        priority = self.ui.priority_comboBox.currentText()
        description = self.ui.descrpt_plainTextEdit.toPlainText()
        log_file = self.ui.log_lineEdit.text()

        issue_type = 'Bug'
        if self.ui.feat_rqst_radioButton.isChecked():
            issue_type = 'Task'

        # Add Toolkit user and context details
        submit_by = f'Submitted by: {self.user["name"]}'
        user = {
            'id': self.context.user['id'],
            'type': self.context.user['type'],
            'name': self.context.user['name'],
            'login': self.context.user.get('login', None),
        }  # strip out extraneous key/values from HumanUser
        description = f'{description}\n\n\n--- Pipeline Details ---\n{submit_by}\n' \
                      f'Project: {str(self.context.project)}\nEntity: {str(self.context.entity)}' \
                      f'\nTask: {str(self.context.task)}\nUser: {str(user)}'

        # Create Jira issue
        issue_dict = {
            'project': {'id': project_id},
            'summary': title,
            'description': description,
            'priority': {'name': priority},
            'issuetype': {'name': issue_type},
        }
        issue = self.jira.create_issue(fields=issue_dict)

        # upload log file from UI
        if self.ui.open_bug_radioButton.isChecked() and log_file and os.path.exists(log_file):
            self.jira.add_attachment(issue=issue, attachment=log_file)

        # read and upload a file (note binary mode for opening, it's important)
        if self.screen_grab:
            with open(self.screen_grab, 'rb') as fh:
                self.jira.add_attachment(issue=issue, attachment=fh)

        self._overlay_widget.show_message(f'<h1 style="color:#4383a8">Jira Ticket Created ({issue})</h1>'
                                          '<h2>Thank you, the team will review your request shortly')

    def _update_ui(self):
        if 'Select Jira Project' in self.ui.jira_proj_comboBox.currentText():
            self.ui.form_widget.setEnabled(False)
            self.ui.open_bug_radioButton.setEnabled(False)
            self.ui.feat_rqst_radioButton.setEnabled(False)

        else:
            self.ui.submitPushButton.setEnabled(False)
            self.ui.open_bug_radioButton.setEnabled(True)
            self.ui.feat_rqst_radioButton.setEnabled(True)

            if not self.ui.open_bug_radioButton.isChecked() and not self.ui.feat_rqst_radioButton.isChecked():
                self.ui.form_widget.setEnabled(False)

            else:
                if self.ui.open_bug_radioButton.isChecked():
                    self.ui.log_lineEdit.setEnabled(True)
                    self.ui.log_pushButton.setEnabled(True)

                else:
                    self.ui.log_lineEdit.setEnabled(False)
                    self.ui.log_pushButton.setEnabled(False)

                self.ui.form_widget.setEnabled(True)

                if self.ui.title_lineEdit.text != '' and self.ui.descrpt_plainTextEdit.toPlainText() != '' and \
                        self.ui.priority_comboBox.currentIndex() != 0:
                    self.ui.submitPushButton.setEnabled(True)

    def browse_file(self):
        file_name = QtGui.QFileDialog.getOpenFileName()
        self.ui.log_lineEdit.setText(file_name[0])

    def _on_screen_capture_btn_clicked(self):
        """Modally displays the screen capture tool"""

        # capture the screen and show the results
        pixmap = screen_grab.screen_capture()
        self._set_results_pixmap(pixmap, self.ui.results_pixmap)

        # Save screen grab to temp file
        self.screen_grab = tempfile.mktemp(suffix='_screen_grab.png')
        pixmap.save(self.screen_grab)

    def _clear_results_pixmap(self):
        self.screen_grab = None
        self.ui.results_pixmap.clear()
        self.ui.results_pixmap.setText('(Optional)')

    def _set_results_pixmap(self, pixmap, widget):
        pixmap = pixmap.scaled(self.ui.results_pixmap.width(), self.ui.results_pixmap.height(),
                               QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        widget.setPixmap(pixmap)
