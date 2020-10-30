import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from decimal import Decimal
# load the ui file
ui_file = 'simple_sales_tax_calculator.ui'
ui_main_window, ui_base_class = uic.loadUiType(ui_file)
class MyWindow(QtWidgets.QMainWindow, ui_main_window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        ui_main_window.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.calc_tax)
        self.setWindowIcon(QtGui.QIcon('calc_icon.png'))
    def calc_tax(self):
        price = Decimal(self.price_box.text())
        tax = Decimal(self.tax_rate.value())
        total_price = price + ((tax/100) * price)
        self.results_output.setText(str(total_price))
        self.results_output.adjustSize()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())