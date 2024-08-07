from PySide6 import (
    QtWidgets,
    QtGui,
)
from ui_main import Ui_MainWindow
import logic
import sys
import os

class Orbital(QtWidgets.QMainWindow):
    def __init__(self):
        super(Orbital, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.clickpack_valid = False
        self.macro_valid = False

        app.setStyle("Fusion")

        self.ui.title_label.setPixmap(QtGui.QPixmap(":/assets/assets/icon-1024x1024-nobg-white.png").scaled(64, 64, mode=QtGui.Qt.SmoothTransformation))
        self.ui.macro_browse.setIcon(QtGui.QIcon(":/assets/assets/file-black.svg"))
        self.ui.clickpack_browse_file.setIcon(QtGui.QIcon(":/assets/assets/file-black.svg"))
        self.ui.clickpack_browse_folder.setIcon(QtGui.QIcon(":/assets/assets/folder-black.svg"))
        self.ui.clickpack_browse_db.setIcon(QtGui.QIcon(":/assets/assets/cloud-black.svg"))
        self.ui.main_progressbar.setFormat("Push Render to render.")

        self.connect()

    def set_checkbox_enabler(self, checkbox, obj):
        checkbox.clicked.connect(lambda: obj.setEnabled(checkbox.isChecked()))

    def connect(self):
        self.set_checkbox_enabler(self.ui.sc_checkbox, self.ui.sc_spinbox)
        self.set_checkbox_enabler(self.ui.hc_checkbox, self.ui.hc_spinbox)
        
        self.ui.render_pushbutton.clicked.connect(self.render)

        self.ui.macro_path.textChanged.connect(lambda: self.check_macro(self.ui.macro_path.text(), inline=True))
        self.ui.clickpack_path.textChanged.connect(lambda: self.check_clickpack(self.ui.clickpack_path.text(), inline=True))

        self.ui.macro_browse.clicked.connect(self.macro_browse)
        self.ui.clickpack_browse_file.clicked.connect(lambda: self.clickpack_browse(1))
        self.ui.clickpack_browse_folder.clicked.connect(lambda: self.clickpack_browse(0))
        self.ui.clickpack_browse_db.clicked.connect(self.browse_db)
        
        self.ui.search_lineedit.textChanged.connect(self.search_db)
        self.ui.clickpackdb_list.itemDoubleClicked.connect(self.set_cp_from_db)

        self.ui.bg_noise_checkbox.toggled.connect(lambda x: self.ui.bg_noise_checkbox.setText("Yes" if x else "No"))

    def set_cp_from_db(self, item):
        self.ui.clickpack_path.setText("clickpackdb:" + item.text())
        self.ui.main_stwidget.setCurrentIndex(0)

    def search_db(self):
        search_text = self.ui.search_lineedit.text()
        db = logic.clickpackdb()
        # TODO: maybe insert a better search function?
        clickpacks = filter(lambda x: search_text.lower() in x.lower(), db["clickpacks"].keys())
        self.ui.clickpackdb_list.clear()
        self.ui.clickpackdb_list.addItems(list(clickpacks))

    def browse_db(self):
        self.ui.main_stwidget.setCurrentIndex(1)
        db = logic.clickpackdb()
        self.ui.clickpackdb_list.clear()
        self.ui.clickpackdb_list.addItems(list(db["clickpacks"].keys()))

    def clickpack_browse(self, mode):
        if mode == 0:
            text = QtWidgets.QFileDialog.getExistingDirectory(self, "Select clickpack folder")
        elif mode == 1:
            text, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select clickpack file", None, "Clickpack file (*.zip)")

        if text: self.ui.clickpack_path.setText(text)

    def macro_browse(self):
        text, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select macro", None, ";;".join([f"{i[0]} ({i[1]})" for i in logic.macro_types.keys()]))
        if text: self.ui.macro_path.setText(text)
    
    def update_valid(self):
        self.ui.render_pushbutton.setEnabled(self.clickpack_valid and self.macro_valid)

    def check_macro(self, text, inline=False):
        self.ui.tps_spinbox.setValue(0)
        
        self.macro_valid = False
        self.update_valid()

        if not logic.is_macro(text):
            if not inline: self.message_box("Error", f"This file is not a supported macro! (supported: {', '.join(map(lambda x: x[0], logic.macro_types.keys()))})", 1)
            return

        self.ui.macro_path.setText(text)
        tps, = logic.macro_info(text)
        self.ui.tps_spinbox.setValue(tps)
        
        self.macro_valid = True
        self.update_valid()

    def check_clickpack(self, text, inline=False):
        self.ui.name_lineedit.setText("")
        self.ui.author_lineedit.setText("")
        self.ui.description_lineedit.setText("")
        self.ui.noise_checkbox.setText("No")
        self.ui.bg_noise_checkbox.setEnabled(False)
        
        self.clickpack_valid = False
        self.update_valid()
        
        if not logic.is_clickpack(text):
            if not inline: self.message_box("Error", "This file/folder is not a clickpack!", 1)
            return

        self.ui.clickpack_path.setText(text)
        name, author, description, noise = logic.clickpack_info(text)
        self.ui.name_lineedit.setText(name)
        self.ui.author_lineedit.setText(author)
        self.ui.description_lineedit.setText(description)
        self.ui.noise_checkbox.setText("Yes" if noise else "No")
        self.ui.bg_noise_checkbox.setEnabled(noise)

        self.clickpack_valid = True
        self.update_valid()

    def set_progressbar(self, value, maxvalue, text):
        self.ui.main_progressbar.setMaximum(maxvalue)
        self.ui.main_progressbar.setValue(value)
        if text == 0: self.ui.main_progressbar.setFormat("Rendering: %p%")
        if text == 1: self.ui.main_progressbar.setFormat("Downloading clickpack: %p%")
        app.processEvents()

    def render(self):
        self.ui.main_progressbar.setValue(0)
        self.ui.render_pushbutton.setEnabled(False)
        output_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save rendered clicks as...", None, "MP3 compressed audio (*.mp3);;OGG vorbis audio (*.ogg);;WAV uncompressed audio (*.wav);;FLAC uncompressed audio (*.flac)")

        if not output_path.endswith((".wav", ".mp3", ".flac", ".ogg")): output_path += ".wav"

        logic.render(
            self.ui.macro_path.text(),
            self.ui.clickpack_path.text(),
            output_path,
            {
                "softclicks": self.ui.sc_spinbox.value() if self.ui.sc_checkbox.isChecked() else None,
                "hardclicks": self.ui.hc_spinbox.value() if self.ui.hc_checkbox.isChecked() else None,
                "end": self.ui.end_spinbox.value(),
                "progress_callback": self.set_progressbar,
                "noise": self.ui.bg_noise_checkbox.isChecked(),
            }
        )
        
        self.ui.render_pushbutton.setEnabled(True)
        self.ui.main_progressbar.setValue(0)
        self.ui.main_progressbar.setFormat("Push Render to render.")
        self.message_box("Done", "All done", 0)

    def message_box(self, title, text, code):
        [QtWidgets.QMessageBox.information, QtWidgets.QMessageBox.critical][code](self, title, text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Orbital()
    window.show()

    sys.exit(app.exec())


