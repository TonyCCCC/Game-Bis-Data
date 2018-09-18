from huiyiyou import hyyCPI
from mifei import MifeiLogin
from flexion import FlexionLogin
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time
import os

class DateDialog(QDialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)
        label1 = QLabel(self.tr('Start Date'))
        label2 = QLabel(self.tr('End Date'))
        self.syear = QSpinBox()
        self.syear.setRange(1970, 2100)
        self.syear.setValue(2018)
        self.smonth = QSpinBox()
        self.smonth.setRange(1, 12)
        self.smonth.setValue(6)
        self.sday = QSpinBox()
        self.sday.setRange(1, 31)
        self.sday.setValue(15)
        self.eyear = QSpinBox()
        self.eyear.setRange(1970, 2100)
        self.eyear.setValue(2018)
        self.emonth = QSpinBox()
        self.emonth.setRange(1, 12)
        self.emonth.setValue(6)
        self.eday = QSpinBox()
        self.eday.setRange(1, 31)
        self.eday.setValue(15)
        date_button = QPushButton("Submit Date")
        self.connect(date_button, SIGNAL("clicked()"), self.getdata)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.syear, 0, 1)
        layout.addWidget(self.smonth, 0, 2)
        layout.addWidget(self.sday, 0, 3)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.eyear, 1, 1)
        layout.addWidget(self.emonth, 1, 2)
        layout.addWidget(self.eday, 1, 3)
        layout.addWidget(date_button, 2, 1)

        self.setLayout(layout)

        self.setWindowTitle(self.tr("Game Biz Data"))

    def getdata(self):
        start_date = "%s-%s-%s" % (self.syear.value(), self.smonth.value(), self.sday.value())
        end_date = "%s-%s-%s" % (self.eyear.value(), self.emonth.value(), self.eday.value())
        # hyy = hyyCPI(start_date, end_date)
        # hyy.captcha()
        # cap, ok = QInputDialog.getText(self, self.tr("CAPTCHA"), self.tr("Enter CAPTCHA:"), QLineEdit.Normal)
        # if ok and cap is not None:
        #     hyy.get_data(cap)
        # os.system("taskkill /F /IM KanKan.exe")
        mf = MifeiLogin(start_date, end_date)
        mf.login()
        flx = FlexionLogin(start_date, end_date)
        flx.login()
        time.sleep(3)
        self.close()


def main():
    app = QApplication(sys.argv)
    window = DateDialog()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
