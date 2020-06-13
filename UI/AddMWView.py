# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddMWView.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
# 李振
#
# WARNING! All changes made in this file will be lost!

import os
import sqlite3
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QWidget

from Utils import openDB


class AddMWWidget(object):
    def setupUi(self, Dialog):

        # 自己添加的，很重要
        self.dialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(566, 787)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(50, 20, 50, -1)
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Label_14 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_14.setFont(font)
        self.Label_14.setObjectName("Label_14")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_14)
        self.maintenanceWayID = QtWidgets.QLineEdit(Dialog)
        self.maintenanceWayID.setObjectName("maintenanceWayID")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.maintenanceWayID)



        self.errorMessage = QtWidgets.QLabel(Dialog)
        self.errorMessage.setText("")
        self.errorMessage.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorMessage.setObjectName("errorMessage")
        self.verticalLayout.addWidget(self.errorMessage)

        self.iDLabel_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.iDLabel_2.setFont(font)
        self.iDLabel_2.setObjectName("iDLabel_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iDLabel_2)
        self.productID = QtWidgets.QLineEdit(Dialog)
        self.productID.setObjectName("productID")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.productID)
        self.Label_15 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_15.setFont(font)
        self.Label_15.setObjectName("Label_15")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_15)
        self.maintenanceWayName = QtWidgets.QLineEdit(Dialog)
        self.maintenanceWayName.setObjectName("maintenanceWayName")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maintenanceWayName)
        self.Label_16 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_16.setFont(font)
        self.Label_16.setObjectName("Label_16")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_16)
        self.firstTime = QtWidgets.QLineEdit(Dialog)
        self.firstTime.setObjectName("firstTime")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.firstTime)
        self.Label_17 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_17.setFont(font)
        self.Label_17.setObjectName("Label_17")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_17)
        self.interval = QtWidgets.QLineEdit(Dialog)
        self.interval.setObjectName("interval")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.interval)
        self.Label_18 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.Label_18.setFont(font)
        self.Label_18.setObjectName("Label_18")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_18)
        self.alterRule = QtWidgets.QLineEdit(Dialog)
        self.alterRule.setObjectName("alterRule")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.alterRule)
        self.Label_26 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_26.setFont(font)
        self.Label_26.setObjectName("Label_26")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_26)
        self.creator = QtWidgets.QLineEdit(Dialog)
        self.creator.setObjectName("creator")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.creator)
        self.Label_19 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_19.setFont(font)
        self.Label_19.setObjectName("Label_19")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_19)
        self.createTime = QtWidgets.QLineEdit(Dialog)
        self.createTime.setObjectName("createTime")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_23 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_23.setFont(font)
        self.Label_23.setObjectName("Label_23")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_23)
        self.updateName = QtWidgets.QLineEdit(Dialog)
        self.updateName.setObjectName("updateName")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.updateName)
        self.Label_24 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_24.setFont(font)
        self.Label_24.setObjectName("Label_24")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_24)
        self.updateTime = QtWidgets.QLineEdit(Dialog)
        self.updateTime.setObjectName("updateTime")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.updateTime)
        self.Label_25 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_25.setFont(font)
        self.Label_25.setObjectName("Label_25")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_25)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.conserveButton.setFont(font)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        # 自己加的
        self.bindButton(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新增维保方式"))
        self.Label_14.setText(_translate("Dialog", "方式ID："))
        self.iDLabel_2.setText(_translate("Dialog", "产品ID："))
        self.Label_15.setText(_translate("Dialog", "方式名字："))
        self.Label_16.setText(_translate("Dialog", "初次维保时间："))
        self.Label_17.setText(_translate("Dialog", "维保间隔时间(天)："))
        self.Label_18.setText(_translate("Dialog", "维保到期前多少天提醒(天)："))
        self.Label_26.setText(_translate("Dialog", "创建人员："))
        self.Label_19.setText(_translate("Dialog", "创建时间："))
        self.Label_23.setText(_translate("Dialog", "修改人员："))
        self.Label_24.setText(_translate("Dialog", "修改时间："))
        self.Label_25.setText(_translate("Dialog", "备注："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))



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
        maintenanceWayID = self.maintenanceWayID.text()
        productID = self.productID.text()
        maintenanceWayName = self.maintenanceWayName.text()
        firstTime = self.firstTime.text()
        interval = self.interval.text()
        alterRule = self.alterRule.text()
        creator = self.creator.text()
        # createTime是默认创建的，下面由系统自动生成
        createTime = self.createTime.text()
        updateName = self.updateName.text()
        updateTime = self.updateTime.text()
        remark = self.remark.toPlainText()


        # 如果必要的信息都不为空
        if maintenanceWayID == "" or productID == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(maintenanceWayID)
            if num == 0:
                return
            # createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            # insert_sql = "INSERT INTO MaintenanceWay VALUES ('%s', '%s', '%s', '%s', '%s'" \
            #              ", '%s', '%s','%s', '%s', '%s',%s)" % \
            #              (maintenanceWayID, productID, maintenanceWayName, firstTime, interval,
            #                 alterRule, creator, createTime, updateName, updateTime,remark)
            # self.query.exec(insert_sql)
            # self.db.commit()
            # confirm = QMessageBox.information(QDialog(), "提示", "维保方式新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            # if confirm == QMessageBox.Yes:
            #     Dialog.close()

            createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect("../db/ProductManagement_new.db")
            cursor = conn.cursor()
            sql = "insert into MaintenanceWay (MaintenanceWayID, ProductID, MaintenanceWayName, FirstTime,\
                    Interva, AlterRule, Creator, CreateTime, UpdateName,UpdateTime,Remark) " \
                  "values (?,?,?,?,?,?,?,?,?,?,?)"
            try:
                cursor.execute(sql, (maintenanceWayID, productID, maintenanceWayName, firstTime, interval,
                            alterRule, creator, createTime, updateName, updateTime,remark))
                conn.commit()
                print("成功！！")
                confirm = QMessageBox.information(QDialog(), "提示", "维保方式新建成功！", QMessageBox.Yes, QMessageBox.Yes)
                if confirm == QMessageBox.Yes:
                    Dialog.close()
            except Exception as e:
                print(e)
                self.errorMessage.setText("抱歉，操作出现错误：",e)
                conn.rollback()


    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()

    def updateButtonEvent(self,  queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """
        # 重要的
        queryModel.delete()

        maintenanceWayID = self.maintenanceWayID.text()
        productID = self.productID.text()
        maintenanceWayName = self.maintenanceWayName.text()
        firstTime = self.firstTime.text()
        interval = self.interval.text()
        alterRule = self.alterRule.text()
        creator = self.creator.text()
        createTime = self.createTime.text()
        updateName = self.updateName.text()
        updateTime = self.updateTime.text()
        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if maintenanceWayID == "" or productID == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(maintenanceWayID)
            if num == 0:
                return
            # updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            # insert_sql = "INSERT INTO MaintenanceWay VALUES ('%s', '%s', '%s', '%s', '%s'" \
            #              ", '%s', '%s','%s', '%s', '%s', %s)" % \
            #              (maintenanceWayID, productID, maintenanceWayName, firstTime, interval,
            #               alterRule, creator, createTime, updateName, updateTime, remark)
            # self.query.exec(insert_sql)
            # self.db.commit()
            # confirm = QMessageBox.information(QDialog(), "提示", "维保方式修改成功！", QMessageBox.Yes, QMessageBox.Yes)
            # if confirm == QMessageBox.Yes:
            #     self.dialog.close()

            updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect("../db/ProductManagement_new.db")
            cursor = conn.cursor()
            sql = "insert into MaintenanceWay (MaintenanceWayID, ProductID, MaintenanceWayName, FirstTime,\
                            Interva, AlterRule, Creator, CreateTime, UpdateName,UpdateTime,Remark) " \
                  "values (?,?,?,?,?,?,?,?,?,?,?)"
            try:
                cursor.execute(sql, (maintenanceWayID, productID, maintenanceWayName, firstTime, interval,
                                     alterRule, creator, createTime, updateName, updateTime, remark))
                conn.commit()
                confirm = QMessageBox.information(QDialog(), "提示", "维保方式修改成功！", QMessageBox.Yes, QMessageBox.Yes)
                if confirm == QMessageBox.Yes:
                    self.dialog.close()
            except Exception as e:
                print(e)
                self.errorMessage.setText("抱歉，您的输入有误：", e)
                conn.rollback()

    def checkOn(self,maintenanceWayID):
        """
        检查维保方式id是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM MaintenanceWay WHERE MaintenanceWayID = '%s'" % maintenanceWayID
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "维保方式ID已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    def updateData(self, list, queryModel):
        """
        修改维保方式信息
        :param list:
        :return:
        """
        self.label.setText("修改维保方式信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))
        print("AddMaintenanceWayView中的updateData方法正常启动！")

        self.maintenanceWayID.setText(list[0])
        self.productID.setText(list[1])
        self.maintenanceWayName.setText(list[2])
        self.firstTime.setText(list[3])
        self.interval.setText(list[4])
        self.alterRule.setText(list[5])
        self.creator.setText(list[6])
        self.createTime.setText(list[7])
        self.updateName.setText(list[8])
        self.updateTime.setText(list[9])
        self.remark.setText(list[10])




