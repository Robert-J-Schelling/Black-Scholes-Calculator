import sys
import asyncio
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QGridLayout,QLabel, QDateEdit,QLineEdit,QComboBox,QMessageBox
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtCore import pyqtSlot, Qt
import qdarkstyle
from CustomQLineEdit import CustomQLineEdit
from CustomQDateEdit import CustomQDateEdit
from CustomQComboBox import CustomQComboBox
from BlackScholes import BlackScholes
import time
import asyncio
class QGridLayout(QGridLayout):
    def __init__(self):
        super(QGridLayout, self).__init__()
        self.setWidgets()
        self.setPositions()
        self.calculate(None)


    def setWidgets(self):
        self.setLabels()
        self.setLineEditables()
        self.setComboBoxes()
        self.setDateEdits()

    def setPositions(self):
        #row 1
        self.addWidget(self.price_date,0,0,1,4)
        self.addWidget(self.price_date_selector,0,5,1,3)
        self.addWidget(self.current_time_display,0,8,1,1)

        #row 2
        self.addWidget(self.asset,1,0,1,4)
        self.addWidget(self.asset_display,1,5,1,4)

        #row 3
        self.addWidget(self.spot,2,0,1,4)
        self.addWidget(self.spot_price_edit,2,5,1,4)

        #row 4
        self.addWidget(self.style,3,0,1,4)
        self.addWidget(self.option_type,3,5,1,2)
        self.addWidget(self.option_style,3,7,1,2)

        #row 5
        self.addWidget(self.direction,4,0,1,4)
        self.addWidget(self.direction_box1,4,5,1,2)
        self.addWidget(self.direction_box2,4,7,1,2)

        #row 6
        self.addWidget(self.call_put_label,5,0,1,4)
        self.addWidget(self.call_put_currency,5,5,1,2)
        self.addWidget(self.call_put_choose,5,7,1,2)

        #row 7
        self.addWidget(self.expiry,6,0,1,4)
        self.addWidget(self.option_duration,6,5,1,2)
        self.addWidget(self.expiry_date_selector,6,7,1,2)

        #row 8
        self.addWidget(self.delivery,7,0,1,4)
        self.addWidget(self.delivery_time,7,5,1,2)
        self.addWidget(self.delivery_date,7,7,1,2)

        #row 9
        self.addWidget(self.strike,8,0,1,4)
        self.addWidget(self.strike_price_edit,8,5,1,2)
        self.addWidget(self.strike_moneyness,8,7,1,2)

        #row 10
        self.addWidget(self.quantity,9,0,1,4)
        #self.addWidget(self.quantity_currency,9,5,1,2)
        self.addWidget(self.quantity_amount,9,5,1,4)

        #row 11
        self.addWidget(self.model,10,0,1,4)
        self.addWidget(self.model_select,10,5,1,4)

        #row 12
        self.addWidget(self.space,11,0,1,8)
        #row 13
        self.addWidget(self.volatility,12,0,1,4)
        self.addWidget(self.vol_enter,12,5,1,4)
        #row 14
        self.addWidget(self.volatility_spread,13,0,1,4)
        self.addWidget(self.vol_spread,13,5,1,4)
        #row 15
        self.addWidget(self.domestic_interest_rate,14,0,1,4)
        self.addWidget(self.domestic_interest_rate_edit,14,5,1,4)
        #row 16
        self.addWidget(self.foreign_interest_rate,15,0,1,4)
        self.addWidget(self.foreign_interest_rate_edit,15,5,1,4)


        #row 17
        self.addWidget(self.space,16,0,1,8)
        self.addWidget(self.space,16,0,1,8)

        #row 18
        self.addWidget(self.price,17,0,1,4)
        self.addWidget(self.price_amount,17,5,1,4)

        #row 19
        self.addWidget(self.premium,18,0,1,4)
        self.addWidget(self.premium_amount,18,5,1,4)
        #row 20
        self.addWidget(self.prem_date,19,0,1,4)
        self.addWidget(self.prem_date_edit,19,5,1,4)
        #row 21
        self.addWidget(self.delta,20,0,1,4)
        self.addWidget(self.delta_edit,20,5,1,4)
        #row 22
        self.addWidget(self.hedge,21,0,1,4)
        self.addWidget(self.hedge_edit,21,5,1,4)

    def setLabels(self):
        self.space = QLabel("")

        self.price_date = QLabel("Price Date")
        self.asset = QLabel("Asset")
        self.spot = QLabel("Spot (現在の価格)")
        self.style = QLabel("Style")
        self.direction = QLabel("Direction")
        self.call_put_label = QLabel("Call/Put (コールプット)")
        self.expiry = QLabel("Expiry (満期日)")
        self.delivery = QLabel("Delivery")
        self.strike = QLabel("Strike (行使価格)")
        self.quantity = QLabel("Quantity (数量)")
        self.model = QLabel("Model")

        self.volatility = QLabel("Vol (ボラティリティ)")
        self.volatility_spread = QLabel("Vol Spread")
        self.domestic_interest_rate = QLabel("Domestic Interest Rate (国内金利)")
        self.foreign_interest_rate = QLabel("Foreign Interest Rate (外国金利)")

        self.price = QLabel("プレミアム")
        self.premium = QLabel("キャッシュフロー")
        self.prem_date = QLabel("Prem Date")
        self.delta = QLabel("単位デルタ")
        self.hedge = QLabel("ポジションデルタ")

    def setLineEditables(self):
        self.onlyDouble =QDoubleValidator()

        self.asset_display = CustomQLineEdit("XBTJPY",isCentered = True,isDisabled = True,noBorder = True, qGridLayout = self)

        self.spot_price_edit = CustomQLineEdit("1.0",isOrange = True,ID = "spot_price", qGridLayout = self)

        self.strike_moneyness = CustomQLineEdit("ATMF",isCentered = True,isDisabled = True,noBorder = True, qGridLayout = self)

        self.strike_price_edit = CustomQLineEdit("1.0",isOrange = True,ID = "strike_price", qGridLayout = self)

        self.quantity_amount = CustomQLineEdit("5",isOrange = True,ID = "quantity", qGridLayout = self)

        self.vol_enter = CustomQLineEdit("55.0",isOrange = True,ID = "volatility", qGridLayout = self,postfix =  "%")

        self.vol_spread = CustomQLineEdit("0.0", qGridLayout = self,postfix =  "%")

        self.domestic_interest_rate_edit = CustomQLineEdit("0.0",isOrange = True,ID = "domestic_interest", qGridLayout = self)

        self.foreign_interest_rate_edit = CustomQLineEdit("0.0",isOrange = True,ID = "foreign_interest", qGridLayout = self)

        self.price_amount = CustomQLineEdit("0.0", qGridLayout = self,isOrange = True,ID = "premium")

        self.premium_amount =  CustomQLineEdit("0.0", qGridLayout = self,isOrange = True,ID = "cashflow")

        self.delta_edit = CustomQLineEdit("0.0", qGridLayout = self,isOrange = True,ID = "unit_delta", isOnlyReadable = True)

        self.hedge_edit =  CustomQLineEdit("0.0", qGridLayout = self,isOrange = True,ID = "position_delta",isOnlyReadable = True)

        self.option_duration =  CustomQLineEdit("",isCentered = True,isDisabled = True,noBorder = True, qGridLayout = self)

    def setComboBoxes(self):
        self.option_type = CustomQComboBox()
        self.option_type.addItem("European")
        self.option_style = CustomQComboBox()
        self.option_style.addItem("Vanilla")

        self.direction_box1 = CustomQComboBox()
        self.direction_box1.addItem("Client Buys")
        self.direction_box2 = CustomQComboBox()
        self.direction_box2.addItem("Physical")

        self.call_put_currency = CustomQComboBox()
        self.call_put_currency.addItem("XBT")
        self.call_put_choose = CustomQComboBox(isOrange = True,ID = "callput", qGridLayout = self)
        self.call_put_choose.addItem("Call")
        self.call_put_choose.addItem("Put")

        self.delivery_time = CustomQComboBox()
        self.delivery_time.addItem("NY 10:00")

        self.model_select = CustomQComboBox()
        self.model_select.addItem("Black-Scholes")

    def setDateEdits(self):
        self.current_date = QDate.currentDate()
        self.price_date_selector = CustomQDateEdit(isOrange = True,ID = "start_date", qGridLayout = self)
        self.price_date_selector.setDate(self.current_date)
        self.current_time = (QTime.currentTime())
        self.current_time_display = QLabel(self.current_time.toString(Qt.DefaultLocaleLongDate))

        self.expiry_date_selector = CustomQDateEdit(isOrange = True,ID = "expiry_date", qGridLayout = self)
        self.expiry_date_selector.setDate(self.current_date.addMonths(3))


        self.delivery_date = CustomQDateEdit()
        self.delivery_date.setDate(self.current_date.addMonths(3).addDays(2))

        self.prem_date_edit = CustomQDateEdit()
        self.prem_date_edit.setDate(self.current_date.addDays(2))

    def calculate(self,changed):
        self.value_dict = {"changed": changed}
        for index in range(self.count()):
            self.temp = self.itemAt(index).widget()
            try:
                if(self.temp.getID() != None):
                    try:
                        self.value_dict[self.temp.getID()] = self.temp.text()
                    except:
                        self.value_dict[self.temp.getID()] = self.temp.currentText()
            except:
                pass
        try:
            self.setMoneyness()
            loop = asyncio.get_event_loop()
            price,delta,volatility,isInvalid,dayCount = loop.run_until_complete(BlackScholes.set_values(self.value_dict))
            loop.run_until_complete(self.updateUI(price, delta, volatility,dayCount))
            if(isInvalid):
                self.showErrorMessage()
        except:
            pass

    async def updateUI(self,price,delta,volatility,dayCount):
        self.option_duration.setText(str(dayCount) + " Days")
        self.delta_edit.setText(str(delta))
        self.price_amount.setText(str(price))
        self.premium_amount.setText(str(BlackScholes().floatrounding(price*float(self.quantity_amount.text()))))
        self.hedge_edit.setText(str(BlackScholes().floatrounding(delta*float(self.quantity_amount.text()))))
        self.vol_enter.setText(str(volatility))

    def showErrorMessage(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Invalid Input")
        self.msg.setText("Premium you entered is either too high or too low.")
        self.msg.setInformativeText("Implied volatility must be between 0.01 and 400")
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()

    def setMoneyness(self):
        if(self.value_dict["callput"] == "Call"):
            if(float(self.value_dict['spot_price']) < float(self.value_dict['strike_price'])):
                self.strike_moneyness.setText("OTMF")
            elif(float(self.value_dict['spot_price']) > float(self.value_dict['strike_price'])):
                self.strike_moneyness.setText("ITMF")
            else:
                self.strike_moneyness.setText("ATMF")
        else:
            if(float(self.value_dict['spot_price']) < float(self.value_dict['strike_price'])):
                self.strike_moneyness.setText("ITMF")
            elif(float(self.value_dict['spot_price']) > float(self.value_dict['strike_price'])):
                self.strike_moneyness.setText("OTMF")
            else:
                self.strike_moneyness.setText("ATMF")
