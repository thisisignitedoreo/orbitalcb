# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)
import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(381, 528)
        icon = QIcon()
        icon.addFile(u":/assets/assets/icon-1024x1024-nobg-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionSelect_Macro = QAction(MainWindow)
        self.actionSelect_Macro.setObjectName(u"actionSelect_Macro")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.hspacer_00 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.hspacer_00)

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")

        self.title_layout.addWidget(self.title_label)

        self.hspacer_01 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.hspacer_01)


        self.verticalLayout.addLayout(self.title_layout)

        self.hline_00 = QFrame(self.centralwidget)
        self.hline_00.setObjectName(u"hline_00")
        self.hline_00.setFrameShape(QFrame.Shape.HLine)
        self.hline_00.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.hline_00)

        self.macro_layout = QHBoxLayout()
        self.macro_layout.setObjectName(u"macro_layout")
        self.macro_path = QLineEdit(self.centralwidget)
        self.macro_path.setObjectName(u"macro_path")

        self.macro_layout.addWidget(self.macro_path)

        self.macro_browse = QToolButton(self.centralwidget)
        self.macro_browse.setObjectName(u"macro_browse")

        self.macro_layout.addWidget(self.macro_browse)


        self.verticalLayout.addLayout(self.macro_layout)

        self.clickpack_layout = QHBoxLayout()
        self.clickpack_layout.setObjectName(u"clickpack_layout")
        self.clickpack_path = QLineEdit(self.centralwidget)
        self.clickpack_path.setObjectName(u"clickpack_path")

        self.clickpack_layout.addWidget(self.clickpack_path)

        self.clickpack_browse_folder = QToolButton(self.centralwidget)
        self.clickpack_browse_folder.setObjectName(u"clickpack_browse_folder")

        self.clickpack_layout.addWidget(self.clickpack_browse_folder)

        self.clickpack_browse_file = QToolButton(self.centralwidget)
        self.clickpack_browse_file.setObjectName(u"clickpack_browse_file")

        self.clickpack_layout.addWidget(self.clickpack_browse_file)


        self.verticalLayout.addLayout(self.clickpack_layout)

        self.hline_01 = QFrame(self.centralwidget)
        self.hline_01.setObjectName(u"hline_01")
        self.hline_01.setFrameShape(QFrame.Shape.HLine)
        self.hline_01.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.hline_01)

        self.macro_info_layout = QVBoxLayout()
        self.macro_info_layout.setObjectName(u"macro_info_layout")
        self.macro_info_label = QLabel(self.centralwidget)
        self.macro_info_label.setObjectName(u"macro_info_label")
        self.macro_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.macro_info_layout.addWidget(self.macro_info_label)

        self.tps_layout = QHBoxLayout()
        self.tps_layout.setObjectName(u"tps_layout")
        self.tps_label = QLabel(self.centralwidget)
        self.tps_label.setObjectName(u"tps_label")

        self.tps_layout.addWidget(self.tps_label)

        self.tps_spinbox = QDoubleSpinBox(self.centralwidget)
        self.tps_spinbox.setObjectName(u"tps_spinbox")
        self.tps_spinbox.setReadOnly(True)
        self.tps_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tps_spinbox.setDecimals(6)
        self.tps_spinbox.setMaximum(1000000000000000042420637374017961984.000000000000000)

        self.tps_layout.addWidget(self.tps_spinbox)


        self.macro_info_layout.addLayout(self.tps_layout)


        self.verticalLayout.addLayout(self.macro_info_layout)

        self.hline_02 = QFrame(self.centralwidget)
        self.hline_02.setObjectName(u"hline_02")
        self.hline_02.setFrameShape(QFrame.Shape.HLine)
        self.hline_02.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.hline_02)

        self.clickpack_info_layout = QVBoxLayout()
        self.clickpack_info_layout.setObjectName(u"clickpack_info_layout")
        self.clickpack_info_label = QLabel(self.centralwidget)
        self.clickpack_info_label.setObjectName(u"clickpack_info_label")
        self.clickpack_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.clickpack_info_layout.addWidget(self.clickpack_info_label)

        self.name_layout = QHBoxLayout()
        self.name_layout.setObjectName(u"name_layout")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)

        self.name_layout.addWidget(self.name_label)

        self.name_lineedit = QLineEdit(self.centralwidget)
        self.name_lineedit.setObjectName(u"name_lineedit")
        self.name_lineedit.setReadOnly(True)

        self.name_layout.addWidget(self.name_lineedit)


        self.clickpack_info_layout.addLayout(self.name_layout)

        self.author_layout = QHBoxLayout()
        self.author_layout.setObjectName(u"author_layout")
        self.author_label = QLabel(self.centralwidget)
        self.author_label.setObjectName(u"author_label")
        sizePolicy.setHeightForWidth(self.author_label.sizePolicy().hasHeightForWidth())
        self.author_label.setSizePolicy(sizePolicy)

        self.author_layout.addWidget(self.author_label)

        self.author_lineedit = QLineEdit(self.centralwidget)
        self.author_lineedit.setObjectName(u"author_lineedit")
        self.author_lineedit.setReadOnly(True)

        self.author_layout.addWidget(self.author_lineedit)


        self.clickpack_info_layout.addLayout(self.author_layout)

        self.description_layout = QHBoxLayout()
        self.description_layout.setObjectName(u"description_layout")
        self.description_label = QLabel(self.centralwidget)
        self.description_label.setObjectName(u"description_label")
        sizePolicy.setHeightForWidth(self.description_label.sizePolicy().hasHeightForWidth())
        self.description_label.setSizePolicy(sizePolicy)

        self.description_layout.addWidget(self.description_label)

        self.description_lineedit = QLineEdit(self.centralwidget)
        self.description_lineedit.setObjectName(u"description_lineedit")
        self.description_lineedit.setReadOnly(True)

        self.description_layout.addWidget(self.description_lineedit)


        self.clickpack_info_layout.addLayout(self.description_layout)


        self.verticalLayout.addLayout(self.clickpack_info_layout)

        self.hline_03 = QFrame(self.centralwidget)
        self.hline_03.setObjectName(u"hline_03")
        self.hline_03.setFrameShape(QFrame.Shape.HLine)
        self.hline_03.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.hline_03)

        self.render_settings = QVBoxLayout()
        self.render_settings.setObjectName(u"render_settings")
        self.end_render_label = QLabel(self.centralwidget)
        self.end_render_label.setObjectName(u"end_render_label")
        self.end_render_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.render_settings.addWidget(self.end_render_label)

        self.softclicks_layout = QHBoxLayout()
        self.softclicks_layout.setObjectName(u"softclicks_layout")
        self.sc_label = QLabel(self.centralwidget)
        self.sc_label.setObjectName(u"sc_label")

        self.softclicks_layout.addWidget(self.sc_label)

        self.sc_checkbox = QCheckBox(self.centralwidget)
        self.sc_checkbox.setObjectName(u"sc_checkbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sc_checkbox.sizePolicy().hasHeightForWidth())
        self.sc_checkbox.setSizePolicy(sizePolicy1)

        self.softclicks_layout.addWidget(self.sc_checkbox)

        self.sc_spinbox = QSpinBox(self.centralwidget)
        self.sc_spinbox.setObjectName(u"sc_spinbox")
        self.sc_spinbox.setEnabled(False)
        self.sc_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sc_spinbox.setMaximum(99999999)
        self.sc_spinbox.setValue(200)

        self.softclicks_layout.addWidget(self.sc_spinbox)


        self.render_settings.addLayout(self.softclicks_layout)

        self.hardclicks_layout = QHBoxLayout()
        self.hardclicks_layout.setObjectName(u"hardclicks_layout")
        self.hc_label = QLabel(self.centralwidget)
        self.hc_label.setObjectName(u"hc_label")

        self.hardclicks_layout.addWidget(self.hc_label)

        self.hc_checkbox = QCheckBox(self.centralwidget)
        self.hc_checkbox.setObjectName(u"hc_checkbox")
        sizePolicy1.setHeightForWidth(self.hc_checkbox.sizePolicy().hasHeightForWidth())
        self.hc_checkbox.setSizePolicy(sizePolicy1)

        self.hardclicks_layout.addWidget(self.hc_checkbox)

        self.hc_spinbox = QSpinBox(self.centralwidget)
        self.hc_spinbox.setObjectName(u"hc_spinbox")
        self.hc_spinbox.setEnabled(False)
        self.hc_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.hc_spinbox.setMaximum(100000000)
        self.hc_spinbox.setValue(500)

        self.hardclicks_layout.addWidget(self.hc_spinbox)


        self.render_settings.addLayout(self.hardclicks_layout)

        self.end_silence = QHBoxLayout()
        self.end_silence.setObjectName(u"end_silence")
        self.end_label = QLabel(self.centralwidget)
        self.end_label.setObjectName(u"end_label")

        self.end_silence.addWidget(self.end_label)

        self.end_spinbox = QDoubleSpinBox(self.centralwidget)
        self.end_spinbox.setObjectName(u"end_spinbox")
        self.end_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.end_spinbox.setDecimals(6)
        self.end_spinbox.setMaximum(100000.000000000000000)
        self.end_spinbox.setSingleStep(0.100000000000000)
        self.end_spinbox.setValue(3.000000000000000)

        self.end_silence.addWidget(self.end_spinbox)


        self.render_settings.addLayout(self.end_silence)


        self.verticalLayout.addLayout(self.render_settings)

        self.vspacer_00 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.vspacer_00)

        self.render_pushbutton = QPushButton(self.centralwidget)
        self.render_pushbutton.setObjectName(u"render_pushbutton")
        self.render_pushbutton.setEnabled(True)

        self.verticalLayout.addWidget(self.render_pushbutton)

        self.main_progressbar = QProgressBar(self.centralwidget)
        self.main_progressbar.setObjectName(u"main_progressbar")
        self.main_progressbar.setMaximum(1)
        self.main_progressbar.setValue(0)

        self.verticalLayout.addWidget(self.main_progressbar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Orbital ClickBot", None))
        self.actionSelect_Macro.setText(QCoreApplication.translate("MainWindow", u"Select Macro", None))
        self.title_label.setText("")
        self.macro_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Macro path", None))
        self.macro_browse.setText("")
        self.clickpack_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Clickpack path", None))
        self.clickpack_browse_folder.setText("")
        self.clickpack_browse_file.setText("")
        self.macro_info_label.setText(QCoreApplication.translate("MainWindow", u"Macro Info", None))
        self.tps_label.setText(QCoreApplication.translate("MainWindow", u"TPS:", None))
        self.tps_spinbox.setSuffix("")
        self.clickpack_info_label.setText(QCoreApplication.translate("MainWindow", u"Clickpack Info", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.name_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.author_label.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.author_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.description_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.end_render_label.setText(QCoreApplication.translate("MainWindow", u"End render settings", None))
        self.sc_label.setText(QCoreApplication.translate("MainWindow", u"Softclicks:", None))
        self.sc_checkbox.setText("")
        self.sc_spinbox.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.hc_label.setText(QCoreApplication.translate("MainWindow", u"Hardclicks:", None))
        self.hc_checkbox.setText("")
        self.hc_spinbox.setSuffix(QCoreApplication.translate("MainWindow", u" ms", None))
        self.end_label.setText(QCoreApplication.translate("MainWindow", u"End silence:", None))
        self.end_spinbox.setSuffix(QCoreApplication.translate("MainWindow", u" secs", None))
        self.render_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Render", None))
    # retranslateUi

