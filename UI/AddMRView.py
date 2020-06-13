# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddMRView.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import os
import sqlite3
import time


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog

from Utils import openDB


class AddMRWidget(object):
    def setupUi(self, Dialog):
        # 自己写的
        self.dialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(579, 756)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(50, 30, 50, 30)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")

        self.Label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label.setFont(font)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.mrID = QtWidgets.QLineEdit(Dialog)
        self.mrID.setText("")
        self.mrID.setObjectName("mrID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mrID)

        self.errorMessage = QtWidgets.QLabel(Dialog)
        self.errorMessage.setText("")
        self.errorMessage.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorMessage.setObjectName("errorMessage")
        self.verticalLayout.addWidget(self.errorMessage)

        self.label_20 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.mwID = QtWidgets.QLineEdit(Dialog)
        self.mwID.setObjectName("mwID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mwID)

        self.productModelIDLabel = QtWidgets.QLabel(Dialog)
        self.productModelIDLabel.setFont(font)
        self.productModelIDLabel.setObjectName("productModelIDLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.productModelIDLabel)

        self.mrName = QtWidgets.QLineEdit(Dialog)
        self.mrName.setObjectName("mrName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mrName)

        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setFont(font)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.mrTime = QtWidgets.QLineEdit(Dialog)
        self.mrTime.setObjectName("mrTime")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mrTime)

        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setFont(font)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.mrPart = QtWidgets.QLineEdit(Dialog)
        self.mrPart.setObjectName("mrPart")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mrPart)

        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setFont(font)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.mrLead = QtWidgets.QLineEdit(Dialog)
        self.mrLead.setObjectName("mrLead")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.mrLead)

        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setFont(font)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.mrConfirm = QtWidgets.QLineEdit(Dialog)
        self.mrConfirm.setObjectName("mrConfirm")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.mrConfirm)

        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setFont(font)
        self.Label_6.setObjectName("Label_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.mrResult = QtWidgets.QLineEdit(Dialog)
        self.mrResult.setObjectName("mrResult")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.mrResult)

        self.Label_7 = QtWidgets.QLabel(Dialog)
        self.Label_7.setFont(font)
        self.Label_7.setObjectName("Label_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.creator = QtWidgets.QLineEdit(Dialog)
        self.creator.setObjectName("creator")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.creator)

        self.Label_9 = QtWidgets.QLabel(Dialog)
        self.Label_9.setFont(font)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.createTime = QtWidgets.QLineEdit(Dialog)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.createTime)

        self.Label_10 = QtWidgets.QLabel(Dialog)
        self.Label_10.setFont(font)
        self.Label_10.setObjectName("Label_10")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_10)
        self.updateName = QtWidgets.QLineEdit(Dialog)
        self.updateName.setObjectName("updateName")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.updateName)

        self.Label_11 = QtWidgets.QLabel(Dialog)
        self.Label_11.setFont(font)
        self.Label_11.setObjectName("Label_11")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Label_11)

        self.updateTime = QtWidgets.QLineEdit(Dialog)
        self.updateTime.setObjectName("updateTime")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.updateTime)

        self.remarkLabel = QtWidgets.QLabel(Dialog)
        self.remarkLabel.setFont(font)
        self.remarkLabel.setObjectName("remarkLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.remarkLabel)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        # 自己写的
        self.bindButton(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "维保记录："))
        self.Label.setText(_translate("Dialog", "维保记录ID："))
        self.label_20.setText(_translate("Dialog", "维保方式ID："))
        self.productModelIDLabel.setText(_translate("Dialog", "维保方式名字："))
        self.Label_2.setText(_translate("Dialog", "维保时间："))
        self.Label_3.setText(_translate("Dialog", "维保部位："))
        self.Label_4.setText(_translate("Dialog", "维保负责人："))
        self.Label_5.setText(_translate("Dialog", "维保确认人："))
        self.Label_6.setText(_translate("Dialog", "维保效果："))
        self.Label_7.setText(_translate("Dialog", "创建人员："))
        self.Label_9.setText(_translate("Dialog", "创建时间："))
        self.Label_10.setText(_translate("Dialog", "更新人员："))
        self.Label_11.setText(_translate("Dialog", "更新时间："))
        self.remarkLabel.setText(_translate("Dialog", "备注："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))
        # self.errorMessage.setText(_translate("Dialog", "取消"))
    def bindButton(self, Dialog):
        """
        hsj 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))

    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建产品界面的保存按钮事件
        :return:
        """
        mrID = self.mrID.text()
        mwID = self.mwID.text()
        mrName = self.mrName.text()
        mrTime = self.mrTime.text()
        mrPart = self.mrPart.text()
        mrLead = self.mrLead.text()
        mrConfirm = self.mrConfirm.text()
        mrResult = self.mrResult.text()
        creator = self.creator.text()
        createTime = self.createTime.text()
        updateName = self.updateName.text()
        updateTime = self.updateTime.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if mrID == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(mrID)
            if num == 0:
                return
            # import time
            # createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            # insert_sql = "INSERT INTO MaintenanceRecord VALUES ('%s', '%s', '%s', '%s', '%s'" \
            #              ", '%s', '%s','%s', '%s', '%s',%s,%s)" % \
            #              (mrID, mrName, mrTime, mrPart,
            #               mrLead, mrConfirm, mrResult, creator, createTime, updateName,updateTime,remark)
            # print(insert_sql)
            # a = self.query.exec(insert_sql)
            # print('单条数据里的a',a)
            # self.db.commit()
            # print("成功提交")
            # confirm = QMessageBox.information(QDialog(), "提示", "产品新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            # if confirm == QMessageBox.Yes:
            #     Dialog.close()

            createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect("../db/ProductManagement_new.db")
            cursor = conn.cursor()
            sql = "insert into MaintenanceRecord (MrID, MwID, MrName, MrTime, MrPart,\
                    MrLead, MrConfirm, MrResult, Creator, CreateTime, UpdateName,UpdateTime,Remark) " \
                  "values (?,?,?,?,?,?,?,?,?,?,?,?,?)"
            try:
                cursor.execute(sql, (mrID, mwID, mrName, mrTime, mrPart,
                              mrLead, mrConfirm, mrResult, creator, createTime, updateName,updateTime,remark))
                conn.commit()
                print("成功！！")
                confirm = QMessageBox.information(QDialog(), "提示", "维保记录创建完成！", QMessageBox.Yes, QMessageBox.Yes)
                if confirm == QMessageBox.Yes:
                    Dialog.close()
            except Exception as e:
                print(e)
                self.errorMessage.setText("抱歉，您的输入有误：", e)
                conn.rollback()

    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()

    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """

        # 重要的
        queryModel.delete()

        mrID = self.mrID.text()
        mwID = self.mwID.text()
        mrName = self.mrName.text()
        mrTime = self.mrTime.text()
        mrPart = self.mrPart.text()
        mrLead = self.mrLead.text()
        mrConfirm = self.mrConfirm.text()
        mrResult = self.mrResult.text()
        creator = self.creator.text()
        createTime = self.createTime.text()
        updateName = self.updateName.text()
        updateTime = self.updateTime.text()
        remark = self.remark.toPlainText()

        if mrID == "":
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(mrID)
            if num == 0:
                return
            # createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            # insert_sql = "INSERT INTO MaintenanceRecord VALUES ('%s', '%s', '%s', '%s', '%s'" \
            #              ", '%s', '%s','%s', '%s', '%s',%s,%s)" % \
            #              (mrID, mrName, mrTime, mrPart,
            #               mrLead, mrConfirm, mrResult, creator, createTime, updateName, updateTime, remark)
            # self.query.exec(insert_sql)
            # self.db.commit()
            # confirm = QMessageBox.information(QDialog(), "提示", "维保记录修改成功！", QMessageBox.Yes, QMessageBox.Yes)
            # if confirm == QMessageBox.Yes:
            #     self.dialog.close()

            updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect("../db/ProductManagement_new.db")
            print("success")
            cursor = conn.cursor()
            sql = "insert into MaintenanceRecord (MrID, MwID, MrName, MrTime, MrPart,\
                    MrLead, MrConfirm, MrResult, Creator, CreateTime, UpdateName,UpdateTime,Remark) " \
                  "values (?,?,?,?,?,?,?,?,?,?,?,?,?)"
            try:
                cursor.execute(sql, (mrID, mwID, mrName, mrTime, mrPart,
                              mrLead, mrConfirm, mrResult, creator, createTime, updateName,updateTime,remark))
                conn.commit()
                print("成功！！")
                confirm = QMessageBox.information(QDialog(), "提示", "维保记录修改成功！", QMessageBox.Yes, QMessageBox.Yes)
                if confirm == QMessageBox.Yes:
                    self.dialog.close()
            except Exception as e:
                print(e)
                self.errorMessage.setText("抱歉，您的输入有误：", e)
                conn.rollback()



    def checkOn(self, mrID):
        """
        检查产品号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM MaintenanceRecord WHERE mrID = '%s'" % mrID
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "产品已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.label.setText("修改产品信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda: self.updateButtonEvent(queryModel))
        self.mrID.setText(list[0])
        self.mwID.setText(list[1])
        self.mrName.setText(list[2])
        self.mrTime.setText(list[3])
        self.mrPart.setText(list[4])
        self.mrLead.setText(list[5])
        self.mrConfirm.setText(list[6])
        self.mrResult.setText(list[7])
        self.creator.setText(list[8])
        self.createTime.setText(list[9])
        self.updateName.setText(list[10])
        self.updateTime.setText(list[11])
        self.remark.setText(list[12])