from qtpy.QtWidgets import QMainWindow, QToolBar, QAction, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create two toolbar widgets
        toolbar1 = QToolBar("Toolbar 1")
        toolbar2 = QToolBar("Toolbar 2")

        # Add some actions to the toolbars
        action1 = QAction("Action 1", self)
        action2 = QAction("Action 2", self)
        action3 = QAction("Action 3", self)
        action4 = QAction("Action 4", self)

        toolbar1.addAction(action1)
        toolbar1.addAction(action2)

        toolbar2.addAction(action3)
        toolbar2.addAction(action4)

        # Add the toolbars to the main window
        self.addToolBar(toolbar1)
        self.addToolBar(toolbar2)



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
