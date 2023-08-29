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

        app.setStyle("Fusion")

        self.ui.title_label.setPixmap(QtGui.QPixmap(":/assets/assets/icon-1024x1024-nobg-white.png").scaled(64, 64, mode=QtGui.Qt.SmoothTransformation))
        self.ui.macro_browse.setIcon(QtGui.QIcon(":/assets/assets/file-black.svg"))
        self.ui.clickpack_browse_file.setIcon(QtGui.QIcon(":/assets/assets/file-black.svg"))
        self.ui.clickpack_browse_folder.setIcon(QtGui.QIcon(":/assets/assets/folder-black.svg"))

        self.connect()

    def set_checkbox_enabler(self, checkbox, obj):
        checkbox.clicked.connect(lambda: obj.setEnabled(checkbox.isChecked()))

    def connect(self):
        self.set_checkbox_enabler(self.ui.sc_checkbox, self.ui.sc_spinbox)
        self.set_checkbox_enabler(self.ui.hc_checkbox, self.ui.hc_spinbox)
        
        self.ui.render_pushbutton.clicked.connect(self.render)

        self.ui.macro_path.returnPressed.connect(lambda: self.check_macro(self.ui.macro_path.text()))
        self.ui.clickpack_path.returnPressed.connect(lambda: self.check_clickpack(self.ui.clickpack_path.text()))

        self.ui.macro_browse.clicked.connect(self.macro_browse)
        self.ui.clickpack_browse_file.clicked.connect(lambda: self.clickpack_browse(1))
        self.ui.clickpack_browse_folder.clicked.connect(lambda: self.clickpack_browse(0))

    def clickpack_browse(self, mode):
        if mode == 0:
            text = QtWidgets.QFileDialog.getExistingDirectory(self, "Select clickpack folder")
        elif mode == 1:
            text, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select clickpack file", None, "Clickpack file (*.zip)")

        if text: self.check_clickpack(text)

    def macro_browse(self):
        text, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select macro", None, ";;".join([f"{i[0]} ({i[1]})" for i in logic.macro_types.keys()]))
        if text: self.check_macro(text)

    def check_macro(self, text):
        if not os.path.isfile(text):
            self.message_box("Error", "This file does not exist!", 1)
            return
            
        if not logic.is_macro(text):
            self.message_box("Error", f"This file is not a supported macro! (supported: {', '.join(map(lambda x: x[0], logic.macro_types.keys()))})", 1)
            return

        self.ui.macro_path.setText(text)
        fps, = logic.macro_info(text)
        self.ui.fps_spinbox.setValue(fps)

    def check_clickpack(self, text):
        if not (os.path.isfile(text) or os.path.isdir(text)):
            self.message_box("Error", "This file/folder does not exist!", 1)
            return
            
        if not logic.is_clickpack(text):
            self.message_box("Error", "This file/folder is not a clickpack!", 1)
            return

        self.ui.clickpack_path.setText(text)
        name, author, description = logic.clickpack_info(text)
        self.ui.name_lineedit.setText(name)
        self.ui.author_lineedit.setText(author)
        self.ui.description_lineedit.setText(description)

    def set_progressbar(self, value, maxvalue):
        self.ui.main_progressbar.setMaximum(maxvalue)
        self.ui.main_progressbar.setValue(value)
        app.processEvents()

    def render(self):
        self.ui.main_progressbar.setValue(0)
        output_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save rendered clicks as...", None, "MP3 compressed audio (*.mp3);;OGG vorbis audio (*.ogg);;WAV uncompressed audio (*.wav);;FLAC uncompressed audio (*.flac)")

        if not output_path.endswith((".wav", ".mp3", ".flac", ".ogg")): output += ".wav"

        logic.render(
            self.ui.macro_path.text(),
            self.ui.clickpack_path.text(),
            output_path,
            {
                "softclicks": self.ui.sc_spinbox.value() if self.ui.sc_checkbox.isChecked() else None,
                "hardclicks": self.ui.hc_spinbox.value() if self.ui.hc_checkbox.isChecked() else None,
                "end": self.ui.end_spinbox.value(),
            },
            [
                self.set_progressbar,
            ]
        )
        
        self.message_box("Done", "All done", 0)

    def message_box(self, title, text, code):
        [QtWidgets.QMessageBox.information, QtWidgets.QMessageBox.critical][code](self, title, text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Orbital()
    window.show()

    sys.exit(app.exec())


