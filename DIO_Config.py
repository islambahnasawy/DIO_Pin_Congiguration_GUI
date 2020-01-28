# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Print.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import os
import sys
import time

DIO = {'PORTA': {'PIN0': 'DIO_u8PORTA_PIN0_MODE    DIO_u8INPUT_HIGH_IMPEDANCE', 
'PIN1': 'DIO_u8PORTA_PIN1_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN2': 'DIO_u8PORTA_PIN2_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN3': 'DIO_u8PORTA_PIN3_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN4': 'DIO_u8PORTA_PIN4_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN5': 'DIO_u8PORTA_PIN5_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN6': 'DIO_u8PORTA_PIN6_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN7': 'DIO_u8PORTA_PIN7_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',},
'PORTB': {'PIN0': 'DIO_u8PORTB_PIN0_MODE    DIO_u8INPUT_HIGH_IMPEDANCE', 
'PIN1': 'DIO_u8PORTB_PIN1_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN2': 'DIO_u8PORTB_PIN2_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN3': 'DIO_u8PORTB_PIN3_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN4': 'DIO_u8PORTB_PIN4_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN5': 'DIO_u8PORTB_PIN5_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN6': 'DIO_u8PORTB_PIN6_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN7': 'DIO_u8PORTB_PIN7_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',},
'PORTC': {'PIN0': 'DIO_u8PORTC_PIN0_MODE    DIO_u8INPUT_HIGH_IMPEDANCE', 
'PIN1': 'DIO_u8PORTC_PIN1_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN2': 'DIO_u8PORTC_PIN2_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN3': 'DIO_u8PORTC_PIN3_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN4': 'DIO_u8PORTC_PIN4_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN5': 'DIO_u8PORTC_PIN5_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN6': 'DIO_u8PORTC_PIN6_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN7': 'DIO_u8PORTC_PIN7_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',},
'PORTD': {'PIN0': 'DIO_u8PORTD_PIN0_MODE    DIO_u8INPUT_HIGH_IMPEDANCE', 
'PIN1': 'DIO_u8PORTD_PIN1_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN2': 'DIO_u8PORTD_PIN2_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN3': 'DIO_u8PORTD_PIN3_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN4': 'DIO_u8PORTD_PIN4_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN5': 'DIO_u8PORTD_PIN5_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN6': 'DIO_u8PORTD_PIN6_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',
'PIN7': 'DIO_u8PORTD_PIN7_MODE    DIO_u8INPUT_HIGH_IMPEDANCE',}
}
MFIC = {'PORTA': {'PIN0': 'DIO_u8PORTA_PIN0  0', 
'PIN1': 'DIO_u8PORTA_PIN1  0',
'PIN2': 'DIO_u8PORTA_PIN2  0',
'PIN3': 'DIO_u8PORTA_PIN3  0',
'PIN4': 'DIO_u8PORTA_PIN4  0',
'PIN5': 'DIO_u8PORTA_PIN5  0',
'PIN6': 'DIO_u8PORTA_PIN6  0',
'PIN7': 'DIO_u8PORTA_PIN7  0',},
'PORTB': {'PIN0': 'DIO_u8PORTB_PIN0  0', 
'PIN1': 'DIO_u8PORTB_PIN1  0',
'PIN2': 'DIO_u8PORTB_PIN2  0',
'PIN3': 'DIO_u8PORTB_PIN3  0',
'PIN4': 'DIO_u8PORTB_PIN4  0',
'PIN5': 'DIO_u8PORTB_PIN5  0',
'PIN6': 'DIO_u8PORTB_PIN6  0',
'PIN7': 'DIO_u8PORTB_PIN7  0',},
'PORTC': {'PIN0': 'DIO_u8PORTC_PIN0  0', 
'PIN1': 'DIO_u8PORTC_PIN1  0',
'PIN2': 'DIO_u8PORTC_PIN2  0',
'PIN3': 'DIO_u8PORTC_PIN3  0',
'PIN4': 'DIO_u8PORTC_PIN4  0',
'PIN5': 'DIO_u8PORTC_PIN5  0',
'PIN6': 'DIO_u8PORTC_PIN6  0',
'PIN7': 'DIO_u8PORTC_PIN7  0',},
'PORTD': {'PIN0': 'DIO_u8PORTD_PIN0  0',
'PIN1': 'DIO_u8PORTD_PIN1  0',
'PIN2': 'DIO_u8PORTD_PIN2  0',
'PIN3': 'DIO_u8PORTD_PIN3  0',
'PIN4': 'DIO_u8PORTD_PIN4  0',
'PIN5': 'DIO_u8PORTD_PIN5  0',
'PIN6': 'DIO_u8PORTD_PIN6  0',
'PIN7': 'DIO_u8PORTD_PIN7  0',}
}
class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 401)
        self.OutputPath_lineEdit = QLineEdit(Form)
        self.OutputPath_lineEdit.setObjectName(u"OutputPath_lineEdit")
        self.OutputPath_lineEdit.setGeometry(QRect(40, 310, 371, 31))
        self.Generate_pushButton = QPushButton(Form)
        self.Generate_pushButton.setObjectName(u"Generate_pushButton")
        self.Generate_pushButton.setGeometry(QRect(430, 310, 93, 28))
        self.PinName_lineEdit = QLineEdit(Form)
        self.PinName_lineEdit.setObjectName(u"PinName_lineEdit_2")
        self.PinName_lineEdit.setEnabled(False)
        self.PinName_lineEdit.setGeometry(QRect(40, 200, 251, 31))
        self.UseDefualtName_checkBox = QCheckBox(Form)
        self.UseDefualtName_checkBox.setObjectName(u"UseDefualtName_checkBox_2")
        self.UseDefualtName_checkBox.setGeometry(QRect(330, 200, 131, 31))
        self.UseDefualtName_checkBox.setChecked(True)
        self.PORT_comboBox = QComboBox(Form)
        self.PORT_comboBox.setObjectName(u"PORT_comboBox")
        self.PORT_comboBox.setGeometry(QRect(40, 40, 73, 22))
        
        self.PORT_comboBox.addItem("PORTA")
        self.PORT_comboBox.addItem("PORTB")
        self.PORT_comboBox.addItem("PORTC")
        self.PORT_comboBox.addItem("PORTD")
        
        self.PIN_comboBox = QComboBox(Form)
        self.PIN_comboBox.setObjectName(u"PIN_comboBox")
        self.PIN_comboBox.setGeometry(QRect(160, 40, 73, 22))
        
        self.PIN_comboBox.addItem("PIN0")
        self.PIN_comboBox.addItem("PIN1")
        self.PIN_comboBox.addItem("PIN2")
        self.PIN_comboBox.addItem("PIN3")
        self.PIN_comboBox.addItem("PIN4")
        self.PIN_comboBox.addItem("PIN5")
        self.PIN_comboBox.addItem("PIN6")
        self.PIN_comboBox.addItem("PIN7")
        
        
        self.InputConfig_groupBox = QGroupBox(Form)
        self.InputConfig_groupBox.setObjectName(u"InputConfig_groupBox")
        self.InputConfig_groupBox.setGeometry(QRect(500, 100, 281, 61))
        self.PullUp_radioButton = QRadioButton(self.InputConfig_groupBox)
        self.PullUp_radioButton.setObjectName(u"PullUp_radioButton")
        self.PullUp_radioButton.setGeometry(QRect(10, 30, 97, 20))
        self.HighImp_radioButton = QRadioButton(self.InputConfig_groupBox)
        self.HighImp_radioButton.setObjectName(u"HighImp_radioButton")
        self.HighImp_radioButton.setGeometry(QRect(130, 30, 131, 20))
        self.HighImp_radioButton.setChecked(True)
        self.OutputConfig_groupBox = QGroupBox(Form)
        self.OutputConfig_groupBox.setObjectName(u"OutputConfig_groupBox")
        self.OutputConfig_groupBox.setEnabled(False)
        self.OutputConfig_groupBox.setGeometry(QRect(250, 100, 231, 61))
        self.High_radioButton = QRadioButton(self.OutputConfig_groupBox)
        self.High_radioButton.setObjectName(u"High_radioButton")
        self.High_radioButton.setGeometry(QRect(10, 30, 97, 20))
        self.Low_radioButton = QRadioButton(self.OutputConfig_groupBox)
        self.Low_radioButton.setObjectName(u"Low_radioButton")
        self.Low_radioButton.setEnabled(True)
        self.Low_radioButton.setGeometry(QRect(130, 30, 97, 20))
        self.Low_radioButton.setChecked(True)
        self.Mode_groupBox = QGroupBox(Form)
        self.Mode_groupBox.setObjectName(u"Mode_groupBox")
        self.Mode_groupBox.setGeometry(QRect(40, 100, 191, 61))
        self.Output_radioButton = QRadioButton(self.Mode_groupBox)
        self.Output_radioButton.setObjectName(u"Output_radioButton")
        self.Output_radioButton.setGeometry(QRect(20, 30, 97, 20))
        self.Input_radioButton = QRadioButton(self.Mode_groupBox)
        self.Input_radioButton.setObjectName(u"Input_radioButton")
        self.Input_radioButton.setGeometry(QRect(120, 30, 97, 20))
        self.Input_radioButton.setChecked(True)
        
        self.SAVE_pushButton = QPushButton(Form)
        self.SAVE_pushButton.setObjectName(u"SAVE_pushButton")
        self.SAVE_pushButton.setGeometry(QRect(510, 200, 101, 31))
        self.State_label = QLabel(Form)
        self.State_label.setObjectName(u"State_label")
        self.State_label.setGeometry(QRect(190, 250, 201, 31))

        self.retranslateUi(Form)
        #self.Output_radioButton.clicked.connect(self.OutputConfig_groupBox.setEnabled)
        QObject.connect(self.Output_radioButton, SIGNAL("clicked(bool)"),self.OutputConfig_groupBox.setEnabled)
        
        #self.Output_radioButton.clicked.connect(self.InputConfig_groupBox.setDisabled)
        QObject.connect(self.Output_radioButton, SIGNAL("clicked(bool)"),self.InputConfig_groupBox.setDisabled)
        
        #self.Input_radioButton.clicked.connect(self.OutputConfig_groupBox.setDisabled)
        QObject.connect(self.Input_radioButton, SIGNAL("clicked(bool)"),self.OutputConfig_groupBox.setDisabled)
        
        #self.Input_radioButton.clicked.connect(self.InputConfig_groupBox.setEnabled)
        QObject.connect(self.Input_radioButton, SIGNAL("clicked(bool)"),self.InputConfig_groupBox.setEnabled)
        
        #self.UseDefualtName_checkBox.clicked.connect(self.PinName_lineEdit.setDisabled)
        
        QObject.connect(self.UseDefualtName_checkBox, SIGNAL("clicked(bool)"),self.PinName_lineEdit.setDisabled)
        
        self.Generate_pushButton.clicked.connect(self.GenerateFunc)
        self.SAVE_pushButton.clicked.connect(self.SaveFunc)

        QMetaObject.connectSlotsByName(Form)
        
    # setupUi
        
    def SaveFunc(self):
   
      c_pin = self.PIN_comboBox.currentText()
      c_port = self.PORT_comboBox.currentText()
      
      
      if self.Output_radioButton.isChecked():
        if self.High_radioButton.isChecked():
          (DIO.get(c_port)).update({c_pin: 'DIO_u8'+c_port+'_'+c_pin+'_MODE    DIO_u8OUTPUT_HIGH'})
        else:
          (DIO.get(c_port)).update({c_pin: 'DIO_u8'+c_port+'_'+c_pin+'_MODE    DIO_u8OUTPUT_LOW'})
          
      else:
        if self.PullUp_radioButton.isChecked():
          (DIO.get(c_port)).update({c_pin: 'DIO_u8'+c_port+'_'+c_pin+'_MODE    DIO_u8INPUT_PULLUP'})

        else:
          (DIO.get(c_port)).update({c_pin: 'DIO_u8'+c_port+'_'+c_pin+'_MODE    DIO_u8INPUT_HIGH_IPEDANCE'})
      
      if self.UseDefualtName_checkBox.isChecked():
        (MFIC.get(c_port)).update({c_pin: 'DIO_u8'+c_port+'_'+c_pin+'  0'})
      else:
        (MFIC.get(c_port)).update({c_pin: self.PinName_lineEdit.text() + '  0'})
      
      self.State_label.setText("")
      #self.State_label.setText("Changes Saved !!")
      
      #self.State_label.setText("You are in configuration mode....")
     
      
      #print(DIO)
    def GenerateFunc(self):
    
      print(self.OutputPath_lineEdit.text())
      if (os.path.isdir(self.OutputPath_lineEdit.text())):
        MFIC_Handler = open(self.OutputPath_lineEdit.text() + r'\_MFIC.h', 'w')
        DIO_Handler = open(self.OutputPath_lineEdit.text() + r'\_DIO.h', 'w')
        
        for port in DIO:
          x= DIO.get(port)
          for pin in x:
            y= x.get(pin)
            DIO_Handler.write('#define  ' + y + "\n")
          DIO_Handler.write("\n")
      
        for port in MFIC:
          x= MFIC.get(port)
          for pin in x:
            y= x.get(pin)
            MFIC_Handler.write('#define  ' + y + "\n")
          MFIC_Handler.write("\n")
        self.State_label.setText("Operatione Done !!")
        MFIC_Handler.close()
        DIO_Handler.close()
      else:
        self.State_label.setText("Failed: non exist path !!")
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"DIO Tool", None))
        self.OutputPath_lineEdit.setText(QCoreApplication.translate("Form", u"Enter Output Path", None))
        self.Generate_pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.PinName_lineEdit.setText(QCoreApplication.translate("Form", u"Enter Pin Name", None))
        self.UseDefualtName_checkBox.setText(QCoreApplication.translate("Form", u"Use Defualt Name", None))
        self.InputConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PullUp_radioButton.setText(QCoreApplication.translate("Form", u"Pull Up", None))
        self.HighImp_radioButton.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.OutputConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.High_radioButton.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_radioButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Mode_groupBox.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.Output_radioButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_radioButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.SAVE_pushButton.setText(QCoreApplication.translate("Form", u"Save Changes", None))
        self.State_label.setText(QCoreApplication.translate("Form", u"You are in configuration mode....", None))
    # retranslateUi


App = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()

#window.repaint()
 
App.exec_()
sys.exit(0)
