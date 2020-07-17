# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectInStorage.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery

from Utils import openDB


class SelectINStorage(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 823)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(50, 20, 50, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.ID = QtWidgets.QLineEdit(Dialog)
        self.ID.setEnabled(False)
        self.ID.setObjectName("ID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ID)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.inNO = QtWidgets.QLineEdit(Dialog)
        self.inNO.setEnabled(False)
        self.inNO.setObjectName("inNO")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inNO)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.outNO = QtWidgets.QLineEdit(Dialog)
        self.outNO.setEnabled(False)
        self.outNO.setObjectName("outNO")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.outNO)
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.productNO = QtWidgets.QLineEdit(Dialog)
        self.productNO.setEnabled(False)
        self.productNO.setObjectName("productNO")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.productNO)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.inDate = QtWidgets.QDateTimeEdit(Dialog)
        self.inDate.setEnabled(False)
        self.inDate.setObjectName("inDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inDate)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.inStorageNo = QtWidgets.QLineEdit(Dialog)
        self.inStorageNo.setEnabled(False)
        self.inStorageNo.setObjectName("inStorageNo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inStorageNo)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.isUsed = QtWidgets.QComboBox(Dialog)
        self.isUsed.setEnabled(False)
        self.isUsed.setObjectName("isUsed")
        self.isUsed.addItem("")
        self.isUsed.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.isUsed)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.inRecorderPerson = QtWidgets.QLineEdit(Dialog)
        self.inRecorderPerson.setEnabled(False)
        self.inRecorderPerson.setObjectName("inRecorderPerson")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.inRecorderPerson)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.inTechState = QtWidgets.QLineEdit(Dialog)
        self.inTechState.setEnabled(False)
        self.inTechState.setObjectName("inTechState")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.inTechState)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_13)
        self.createTime = QtWidgets.QDateTimeEdit(Dialog)
        self.createTime.setEnabled(False)
        self.createTime.setMouseTracking(True)
        self.createTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createTime.setAcceptDrops(True)
        self.createTime.setAutoFillBackground(True)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.updateTime = QtWidgets.QDateTimeEdit(Dialog)
        self.updateTime.setEnabled(False)
        self.updateTime.setObjectName("updateTime")
        self.updateTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.updateTime)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.updateID = QtWidgets.QLineEdit(Dialog)
        self.updateID.setEnabled(False)
        self.updateID.setObjectName("updateID")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.updateID)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setEnabled(False)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "入库信息查看"))
        self.label.setText(_translate("Dialog", "入库信息查看"))
        self.label_9.setText(_translate("Dialog", "ID:"))
        self.label_10.setText(_translate("Dialog", "入库编号:"))
        self.label_2.setText(_translate("Dialog", "出库编号:"))
        self.Label.setText(_translate("Dialog", "产品编号："))
        self.label_3.setText(_translate("Dialog", "入库日期:"))
        self.Label_2.setText(_translate("Dialog", "入库库房:"))
        self.label_4.setText(_translate("Dialog", "是否用过:"))
        self.isUsed.setItemText(0, _translate("Dialog", "是"))
        self.isUsed.setItemText(1, _translate("Dialog", "否"))
        self.Label_3.setText(_translate("Dialog", "登  记  人:"))
        self.Label_4.setText(_translate("Dialog", "技术状态:"))
        self.Label_13.setText(_translate("Dialog", "创建时间:"))
        self.label_7.setText(_translate("Dialog", "更新时间"))
        self.label_8.setText(_translate("Dialog", "更新人ID"))
        self.Label_12.setText(_translate("Dialog", "备       注："))

    def setData(self, list):
        self.ID.setText(list[0])
        self.productNO.setText(list[1])
        self.inStorageNo.setText(list[2])
        self.inTechState.setText(list[4])
        self.isUsed.setEditText(list[5])
        self.createTime.setDateTime(datetime.strptime(list[7], "%Y-%m-%d %H:%M:%S"))
        self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.updateID.setText(list[8])
        self.updateTime.setDateTime(datetime.strptime(list[9], "%Y-%m-%d %H:%M:%S"))
        self.remark.setText(list[10])
        db = openDB()
        query = QSqlQuery()
        sql = "SELECT * FROM T_In_Base where ID=%s" % self.ID.text()
        query.exec(sql)
        if query.next():
            self.inNO.setText(query.value(1))
            self.outNO.setText(query.value(2))
            self.inDate.setDate(datetime.strptime(query.value(3), "%Y-%m-%d"))
            self.inDate.setDisplayFormat("yyyy-MM-dd")
            self.inRecorderPerson.setText(query.value(4))
        db.close()
