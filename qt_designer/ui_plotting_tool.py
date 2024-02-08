# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_plotting.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import qt_designer.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(701, 590)
        icon = QIcon()
        icon.addFile(u":/resources/images/redbird_ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_vertical_layout = QVBoxLayout()
        self.main_vertical_layout.setObjectName(u"main_vertical_layout")
        self.welcome_label = QLabel(self.centralwidget)
        self.welcome_label.setObjectName(u"welcome_label")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(10)
        font.setBold(True)
        self.welcome_label.setFont(font)

        self.main_vertical_layout.addWidget(self.welcome_label)

        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setFont(font)

        self.main_vertical_layout.addWidget(self.info_label, 0, Qt.AlignTop)

        self.select_file_horizontal_layout = QHBoxLayout()
        self.select_file_horizontal_layout.setObjectName(u"select_file_horizontal_layout")
        self.file_path_line_edit = QLineEdit(self.centralwidget)
        self.file_path_line_edit.setObjectName(u"file_path_line_edit")
        self.file_path_line_edit.setEnabled(False)

        self.select_file_horizontal_layout.addWidget(self.file_path_line_edit, 0, Qt.AlignTop)

        self.browse_file_button = QPushButton(self.centralwidget)
        self.browse_file_button.setObjectName(u"browse_file_button")

        self.select_file_horizontal_layout.addWidget(self.browse_file_button, 0, Qt.AlignTop)

        self.plot_data_button = QPushButton(self.centralwidget)
        self.plot_data_button.setObjectName(u"plot_data_button")

        self.select_file_horizontal_layout.addWidget(self.plot_data_button, 0, Qt.AlignTop)

        self.integrate_button = QPushButton(self.centralwidget)
        self.integrate_button.setObjectName(u"integrate_button")

        self.select_file_horizontal_layout.addWidget(self.integrate_button, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.select_file_horizontal_layout.addItem(self.horizontalSpacer)

        self.select_file_horizontal_layout.setStretch(0, 3)
        self.select_file_horizontal_layout.setStretch(1, 3)
        self.select_file_horizontal_layout.setStretch(2, 3)
        self.select_file_horizontal_layout.setStretch(3, 3)
        self.select_file_horizontal_layout.setStretch(4, 4)

        self.main_vertical_layout.addLayout(self.select_file_horizontal_layout)


        self.verticalLayout_2.addLayout(self.main_vertical_layout)

        self.checkbox_horizontal_layout = QHBoxLayout()
        self.checkbox_horizontal_layout.setObjectName(u"checkbox_horizontal_layout")
        self.plot_type_label = QLabel(self.centralwidget)
        self.plot_type_label.setObjectName(u"plot_type_label")
        self.plot_type_label.setFont(font)

        self.checkbox_horizontal_layout.addWidget(self.plot_type_label)

        self.plot_scatter_checkbox = QCheckBox(self.centralwidget)
        self.plot_scatter_checkbox.setObjectName(u"plot_scatter_checkbox")

        self.checkbox_horizontal_layout.addWidget(self.plot_scatter_checkbox)

        self.plot_line_checkbox = QCheckBox(self.centralwidget)
        self.plot_line_checkbox.setObjectName(u"plot_line_checkbox")
        self.plot_line_checkbox.setChecked(True)

        self.checkbox_horizontal_layout.addWidget(self.plot_line_checkbox)

        self.plot_grid_checkbox = QCheckBox(self.centralwidget)
        self.plot_grid_checkbox.setObjectName(u"plot_grid_checkbox")
        self.plot_grid_checkbox.setFont(font)

        self.checkbox_horizontal_layout.addWidget(self.plot_grid_checkbox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.checkbox_horizontal_layout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.checkbox_horizontal_layout)

        self.plot_horizontal_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.plot_horizontal_spacer)

        self.integration_label = QLabel(self.centralwidget)
        self.integration_label.setObjectName(u"integration_label")
        self.integration_label.setFont(font)

        self.verticalLayout_2.addWidget(self.integration_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 701, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"S-PlottingTool", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"Welcome to Simo Plotting Tool", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"Please select path to .CSV file, containing X,Y data.", None))
        self.browse_file_button.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.plot_data_button.setText(QCoreApplication.translate("MainWindow", u"Plot Data", None))
        self.integrate_button.setText(QCoreApplication.translate("MainWindow", u"Integrate", None))
        self.plot_type_label.setText(QCoreApplication.translate("MainWindow", u"Plot Type:", None))
        self.plot_scatter_checkbox.setText(QCoreApplication.translate("MainWindow", u"Scatter", None))
        self.plot_line_checkbox.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.plot_grid_checkbox.setText(QCoreApplication.translate("MainWindow", u"Plot Grid", None))
        self.integration_label.setText(QCoreApplication.translate("MainWindow", u"Area under the curve:", None))
    # retranslateUi

