from PyQt5 import QtWidgets
from design import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.setWindowTitle('sevensolve')

    def btnClicked(self):
        if self.ui.text.isChecked():
            pass
        elif self.ui.image.isChecked():
            pass
        elif self.ui.sound.isChecked():
            pass



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())