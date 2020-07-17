# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddInStorage.ui'
# 许帅
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialogButtonBox, QMessageBox, QDialog, QApplication, QWidget

from Utils import openDB


class AddInStorage(object):
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
        self.inNO = QtWidgets.QLineEdit(Dialog)
        self.inNO.setObjectName("inNO")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inNO)
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
        self.outNO = QtWidgets.QLineEdit(Dialog)
        self.outNO.setEnabled(True)
        self.outNO.setObjectName("outNO")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.outNO)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.inDate = QtWidgets.QDateEdit(Dialog)
        self.inDate.setObjectName("inDate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inDate)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.inStorageNo = QtWidgets.QLineEdit(Dialog)
        self.inStorageNo.setEnabled(True)
        self.inStorageNo.setObjectName("inStorageNo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inStorageNo)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.inRecorderPerson = QtWidgets.QLineEdit(Dialog)
        self.inRecorderPerson.setEnabled(True)
        self.inRecorderPerson.setObjectName("inRecorderPerson")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.inRecorderPerson)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.inTechState = QtWidgets.QLineEdit(Dialog)
        self.inTechState.setEnabled(True)
        self.inTechState.setObjectName("inTechState")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.inTechState)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_13)
        self.createTime = QtWidgets.QDateTimeEdit(Dialog)
        self.createTime.setMouseTracking(True)
        self.createTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createTime.setAcceptDrops(True)
        self.createTime.setAutoFillBackground(True)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setEnabled(True)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.isUsed = QtWidgets.QComboBox(Dialog)
        self.isUsed.setObjectName("isUsed")
        self.isUsed.addItem("")
        self.isUsed.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.isUsed)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.inRecorderPersonNO = QtWidgets.QLineEdit(Dialog)
        self.inRecorderPersonNO.setObjectName("inRecorderPersonNO")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.inRecorderPersonNO)
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
        Dialog.setWindowTitle(_translate("Dialog", "入库信息录入"))
        self.label.setText(_translate("Dialog", "入库信息录入"))
        self.label_2.setText(_translate("Dialog", "入库编号:"))
        self.Label.setText(_translate("Dialog", "产品编号："))
        self.iDLabel.setText(_translate("Dialog", "出库编号:"))
        self.label_3.setText(_translate("Dialog", "入库日期:"))
        self.Label_2.setText(_translate("Dialog", "入库库房:"))
        self.Label_3.setText(_translate("Dialog", "入  库  人:"))
        self.Label_4.setText(_translate("Dialog", "技术状态:"))
        self.Label_13.setText(_translate("Dialog", "创建时间:"))
        self.Label_12.setText(_translate("Dialog", "备       注："))
        self.label_4.setText(_translate("Dialog", "是否用过"))
        self.isUsed.setItemText(0, _translate("Dialog", "是"))
        self.isUsed.setItemText(1, _translate("Dialog", "否"))
        self.label_5.setText(_translate("Dialog", "入库人ID:"))
        # 设置创建时间
        self.createTime.setDateTime(QDateTime.currentDateTime())
        self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        # 设置入库日期
        self.inDate.setDateTime(QDateTime.currentDateTime())
        self.inDate.setDisplayFormat("yyyy-MM-dd")
        # 设置入库编号(日期+三位流水号)
        self.inNO.setText(self.getInNO())
        # 提交和取消按钮点击事件
        cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)
        ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        cancel_button.setText("取消")
        ok_button.setText("提交")
        # 提交的槽函数
        ok_button.clicked.connect(self.ok_fun)
        # 取消的槽函数
        cancel_button.clicked.connect(self.cancel_fun)
        # 设置ProductNO的完成编辑信号和获取数据库中出库编号的槽函数
        self.productNO.editingFinished.connect(self.getOutNO)

        # 获取出库编号

    def getOutNO(self):
        db = openDB()
        q = QSqlQuery()
        product_no = self.productNO.text()
        sql_code = "SELECT OutNO FROM T_Out_Detail WHERE ProductNO='%s'" % product_no
        print(q.exec(sql_code))
        if q.exec(sql_code):
            while q.next():
                self.outNO.setText(q.value(0))
        db.close()

        # 获取入库编号

    def getInNO(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT InNO FROM T_In_Base WHERE ID=(SELECT MAX(ID) FROM T_In_Base)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[0:8]:
            return date_str + '101'
        else:
            return str(int(max_no) + 1)

        # 处理提交事件

    def ok_fun(self):
        db = openDB()
        q = QSqlQuery()
        # 判断所有值均不为空
        if all([self.inNO.text(),
                self.outNO.text(),
                self.inDate.text(),
                self.inRecorderPerson.text(),
                self.createTime.text(),
                self.remark.toPlainText(),
                self.productNO.text(),
                self.inStorageNo.text(),
                self.inTechState.text(),
                self.isUsed.currentText(),
                self.createTime.text()]):
            insert_sql = "INSERT INTO T_IN_Base(InNO, OUTNO, INDATE, INRECODER, CREATEID, CREATETIME, UPDATEID, " \
                         "UPDATETIME, REMARK) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                         (self.inNO.text(), self.outNO.text(), self.inDate.text(),
                          self.inRecorderPerson.text(), 1, self.createTime.text(),
                          0, self.createTime.text(), self.remark.toPlainText())
            q.exec(insert_sql)
            db.commit()
            insert_sql = "INSERT INTO T_In_Detail(InNO,ProductNO, InStorageNO, InRecorderID, InTechState, IsUsed, " \
                         "CreateID, " \
                         "CreateTime, UpdateID, UpdateTime, Remark)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
                         "'%s','%s')" % \
                         (self.inNO.text(), self.productNO.text(), self.inStorageNo.text(), 0,
                          self.inTechState.text(), self.isUsed.currentText(), 1, self.createTime.text(),
                          0, self.createTime.text(), self.remark.toPlainText())
            q.exec(insert_sql)
            db.commit()
            db.close()
            confirm = QMessageBox.information(QDialog(), "提示", "入库信息新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()
        else:
            QMessageBox.information(QDialog(), "错误", "输入值不能为空,请重新检查输入！", QMessageBox.Yes, QMessageBox.Yes)

    def cancel_fun(self):
        self.dialog.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../Images/MainWindow_1.png"))
    form = QWidget()
    w = AddInStorage()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
