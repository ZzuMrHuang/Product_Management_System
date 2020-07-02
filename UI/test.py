import sys

from PyQt5.QtWidgets import QApplication, QWidget

from UI.SearchView import MySearchWidget


class MyView(MySearchWidget):
    def __init__(self):
        super(MyView, self).__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = MyView()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())