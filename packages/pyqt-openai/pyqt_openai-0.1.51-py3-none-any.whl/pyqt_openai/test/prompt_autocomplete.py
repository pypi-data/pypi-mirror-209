import sys
from qtpy.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QCompleter
from qtpy.QtCore import Qt
from qtpy.QtGui import QTextCursor

class AutoCompleteTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(AutoCompleteTextEdit, self).__init__(parent)
        self.completer = None

    def set_completer(self, completer):
        if self.completer:
            self.completer.activated.disconnect()

        self.completer = completer
        self.completer.setWidget(self)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.activated.connect(self.insert_completion)

    def insert_completion(self, completion):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)
        tc.insertText(completion)
        self.setTextCursor(tc)

    def text_under_cursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)
        return tc.selectedText()

    def keyPressEvent(self, event):
        if self.completer and self.completer.popup().isVisible():
            if event.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab):
                event.ignore()
                return

        super(AutoCompleteTextEdit, self).keyPressEvent(event)

        if not self.completer:
            return

        if event.key() == Qt.Key_Slash:  # Activate completer when "/" is pressed
            completionPrefix = self.text_under_cursor()

            if completionPrefix != self.completer.completionPrefix():
                self.completer.setCompletionPrefix(completionPrefix)
                self.completer.popup().setCurrentIndex(self.completer.completionModel().index(0, 0))

            cr = self.cursorRect()
            cr.setWidth(self.completer.popup().sizeHintForColumn(
                0) + self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
        else:
            self.completer.popup().hide()

    # def keyPressEvent(self, event):
    #     if self.completer and self.completer.popup().isVisible():
    #         if event.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab):
    #             event.ignore()
    #             return
    #
    #     isShortcut = (event.modifiers() & Qt.ControlModifier) and event.key() == Qt.Key_E
    #     if not self.completer or not isShortcut:
    #         super(AutoCompleteTextEdit, self).keyPressEvent(event)
    #
    #     ctrlOrShift = event.modifiers() & (Qt.ControlModifier | Qt.ShiftModifier)
    #     if not self.completer or (ctrlOrShift and len(event.text()) == 0):
    #         return
    #
    #     eow = "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="  # end of word characters
    #     hasModifier = (event.modifiers() != Qt.NoModifier) and not ctrlOrShift
    #     completionPrefix = self.text_under_cursor()
    #
    #     if not isShortcut and (hasModifier or len(event.text()) == 0 or len(completionPrefix) < 2 or event.text()[-1] in eow):
    #         self.completer.popup().hide()
    #         return
    #
    #     if completionPrefix != self.completer.completionPrefix():
    #         self.completer.setCompletionPrefix(completionPrefix)
    #         self.completer.popup().setCurrentIndex(self.completer.completionModel().index(0, 0))
    #
    #     cr = self.cursorRect()
    #     cr.setWidth(self.completer.popup().sizeHintForColumn(0) + self.completer.popup().verticalScrollBar().sizeHint().width())
    #     self.completer.complete(cr)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = AutoCompleteTextEdit(self)
        self.init_autocomplete()

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def init_autocomplete(self):
        words = ["apple", "banana", "grape", "application", "orange", "pineapple", "strawberry"]
        completer = QCompleter(words, self)
        self.text_edit.set_completer(completer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
