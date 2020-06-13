# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddOutStorage.ui'
# 许帅
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QWidget, QDialogButtonBox

from Utils import openDB


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 781)
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.outNO = QtWidgets.QLineEdit(Dialog)
        self.outNO.setObjectName("outNO")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.outNO)
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.productNO = QtWidgets.QLineEdit(Dialog)
        self.productNO.setEnabled(True)
        self.productNO.setObjectName("productNO")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.productNO)
        self.iDLabel = QtWidgets.QLabel(Dialog)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.usedDepartmentNO = QtWidgets.QLineEdit(Dialog)
        self.usedDepartmentNO.setEnabled(True)
        self.usedDepartmentNO.setObjectName("usedDepartmentNO")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.usedDepartmentNO)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.outDate = QtWidgets.QDateTimeEdit(Dialog)
        self.outDate.setObjectName("outDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.outDate)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.outStorageNo = QtWidgets.QLineEdit(Dialog)
        self.outStorageNo.setEnabled(True)
        self.outStorageNo.setObjectName("outStorageNo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.outStorageNo)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.inRecorderPerson = QtWidgets.QLineEdit(Dialog)
        self.inRecorderPerson.setEnabled(True)
        self.inRecorderPerson.setObjectName("inRecorderPerson")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.inRecorderPerson)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.outTechState = QtWidgets.QLineEdit(Dialog)
        self.outTechState.setEnabled(True)
        self.outTechState.setObjectName("outTechState")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.outTechState)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_13)
        self.createTime = QtWidgets.QDateTimeEdit(Dialog)
        self.createTime.setMouseTracking(True)
        self.createTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createTime.setAcceptDrops(True)
        self.createTime.setAutoFillBackground(True)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setEnabled(True)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.isReturn = QtWidgets.QComboBox(Dialog)
        self.isReturn.setObjectName("isReturn")
        self.isReturn.addItem("")
        self.isReturn.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.isReturn)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.usedID = QtWidgets.QLineEdit(Dialog)
        self.usedID.setObjectName("usedID")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.usedID)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.outReason = QtWidgets.QLineEdit(Dialog)
        self.outReason.setObjectName("outReason")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.outReason)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "出库信息录入"))
        self.label.setText(_translate("Dialog", "出库信息录入"))
        self.label_2.setText(_translate("Dialog", "出库编号:"))
        self.Label.setText(_translate("Dialog", "产品编号："))
        self.iDLabel.setText(_translate("Dialog", "使用部门:"))
        self.label_3.setText(_translate("Dialog", "出库日期:"))
        self.Label_2.setText(_translate("Dialog", "出库库房:"))
        self.label_4.setText(_translate("Dialog", "是否归还:"))
        self.Label_3.setText(_translate("Dialog", "登  记  人:"))
        self.Label_4.setText(_translate("Dialog", "技术状态:"))
        self.Label_13.setText(_translate("Dialog", "创建时间:"))
        self.Label_12.setText(_translate("Dialog", "备       注："))
        self.isReturn.setItemText(0, _translate("Dialog", "是"))
        self.isReturn.setItemText(1, _translate("Dialog", "否"))
        self.label_5.setText(_translate("Dialog", "使  用  人:"))
        self.label_6.setText(_translate("Dialog", "出库原因"))
        self.createTime.setDateTime(QDateTime.currentDateTime())
        self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        # 设置出库日期
        self.outDate.setDateTime(QDateTime.currentDateTime())
        self.outDate.setDisplayFormat("yyyy-MM-dd")
        # 设置出库编号(日期+三位流水号)
        self.outNO.setText(self.getOutNO())
        # 提交和取消按钮点击事件
        cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)
        ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        cancel_button.setText("取消")
        ok_button.setText("提交")
        # 提交的槽函数
        ok_button.clicked.connect(self.ok_fun)

    # def setWidgetProperty(self):
    #     self.createTime.setDateTime(QDateTime.currentDateTime())
    #     # 设置出库日期
    #     self.outDate.setDateTime(QDateTime.currentDateTime())
    #     # 设置出库编号(日期+三位流水号)
    #     self.outNO.setText(self.getOutNO())
    #     # 提交和取消按钮点击事件
    #     cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)
    #     ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
    #     cancel_button.setText("取消")
    #     ok_button.setText("提交")
    #     # 提交的槽函数
    #     ok_button.clicked.connect(self.ok_fun)

    # 获取出库编号

    def getOutNO(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT OutNO FROM T_Out_Base WHERE ID=(SELECT MAX(ID) FROM T_Out_Base)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[0:8]:
            return date_str + '001'
        else:
            return str(int(max_no) + 1)

        # 处理提交事件

    def ok_fun(self):
        db = openDB()
        q = QSqlQuery()
        insert_sql = "INSERT INTO T_Out_Base(outno, outdate, usedid, useddepartmentid, recorderid, outreason, " \
                     "createid, createtime, updateid, updatetime, remark) VALUES ('%s','%s','%s','%s','%s','%s','%s'," \
                     "'%s','%s','%s','%s')" % \
                     (self.outNO.text(), self.outDate.text(), self.usedID.text(),
                      self.usedDepartmentNO.text(), self.inRecorderPerson.text(), self.outReason.text(),
                      self.outNO.text(), self.createTime.text(),
                      0, self.createTime.text(), self.remark.toPlainText())
        q.exec(insert_sql)
        db.commit()
        insert_sql = "INSERT INTO T_Out_Detail(outno, productno, outstorageno, outtechstate, isreturn, createid, " \
                     "createtime, updateid, updatetime, remark)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
                     "'%s')" % \
                     (self.outNO.text(), self.productNO.text(), self.outStorageNo.text(),
                      self.outTechState.text(), self.isReturn.currentText(), 1, self.createTime.text(),
                      0, self.createTime.text(), self.remark.toPlainText())
        q.exec(insert_sql)
        db.commit()
        db.close()
        confirm = QMessageBox.information(QDialog(), "提示", "出库信息新建成功！", QMessageBox.Yes, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            self.dialog.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../Images/MainWindow_1.png"))
    form = QWidget()
    w = Ui_Dialog()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
