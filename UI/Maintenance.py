# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Maintenance.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
# 俞欣
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime, timedelta

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QHeaderView

from UI.MySearchBatchModelPIM import MySearchTableModelPIM, CheckBoxHeader
from UI.SearchViewPIM import MySearchWidgetPIM
from Utils import openDB


class Maintenance(MySearchWidgetPIM):
    def __init__(self):
        super(Maintenance, self).__init__()
        self.select_conditions = ["FirstTime", "ID"]

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1377, 696)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.dateEdit_2 = QtWidgets.QDateEdit(Form)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        #self.tableView = QtWidgets.QTableView(Form)
        #self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        #self.tableView.setObjectName("tableView")

        # 中间手动代码部分 表格UI构建
        self.db = openDB()
        self.tableView = QTableView()

        # hsj 自动义的tableModel
        #FirstTime需更改为最新一次保养时间+保养间隔天数,涉及级联尚未解决
        slt = "ID,ProductNO,FirstTime,count(*)"
        headerRow = ["产品ID", "产品编号", "维修保养截止时间", "维修保养次数"]
        self.queryModel = MySearchTableModelPIM("MaintenanceWay", headerRow, slt)
        self.tableView.setModel(self.queryModel)
        self.header = CheckBoxHeader()
        self.tableView.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.queryModel.headerClick)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.queryModel)
        self.verticalLayout.addWidget(self.tableView)

        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.jumpEdit = QtWidgets.QLineEdit(Form)
        self.jumpEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.jumpEdit.setMaxLength(9999)
        self.jumpEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.jumpEdit.setObjectName("jumpEdit")
        self.horizontalLayout_2.addWidget(self.jumpEdit)
        self.totalPageLabel = QtWidgets.QLabel(Form)
        self.totalPageLabel.setObjectName("totalPageLabel")
        self.horizontalLayout_2.addWidget(self.totalPageLabel)
        self.jumpButton = QtWidgets.QPushButton(Form)
        self.jumpButton.setObjectName("jumpButton")
        self.horizontalLayout_2.addWidget(self.jumpButton)
        self.previousButton = QtWidgets.QPushButton(Form)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        self.bindButton()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "维修保养"))
        self.label_3.setText(_translate("Form", "时间段"))
        self.label_5.setText(_translate("Form", "——"))
        self.label_4.setText(_translate("Form", "产品ID"))
        self.label_6.setText(_translate("Form", "是否进入维修保养提醒期"))
        self.comboBox.setItemText(0, _translate("Form", "否"))
        self.comboBox.setItemText(1, _translate("Form", "是"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_4.setText(_translate("Form", "重置"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))
        # 更新页码总页数 复制进去
        self.totalPageLabel.setText(_translate("Form", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))

    def bindButton(self):
        """
        hsj 绑定按钮
        :return:
        """
        # 把需要使用的窗体传进去

        # 查看产品
        #self.selectProduct.clicked.connect(lambda :self.selectButtonEvent(SelectSingleProductWidget()))

        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.pushButton_2.clicked.connect(self.searchButtonEventM)

    def searchButtonEventM(self):
        """
        hsj 输入查询条件查询按钮事件
        加一个时间修正函数
        增加一个self.combox的检测
        :return:
        """
        content = []

        if self.dateEdit.text() != "":
            dateEdit = datetime.date(datetime.strptime(self.dateEdit.text(), '%Y/%m/%d')+timedelta(days=0))
            content.append(dateEdit)
        if self.dateEdit_2.text() != "":
            dateEdit_2 = datetime.date(datetime.strptime(self.dateEdit_2.text(), '%Y/%m/%d')+timedelta(days=0))
            content.append(dateEdit_2)
        if self.searchEdit.text() != "":
            content.append(self.searchEdit.text())

        if content == "":
            print(111)
            self.queryModel.refreshPage()
            self.queryModel.update()
        else:
            # n = self.comboBox.currentIndex()
            if len(content) == 1 and self.searchEdit.text() == "":
                if self.dateEdit.text() != "":
                    sql = "WHERE %s >= '%s' group by ID" % (
                        self.select_conditions[0], content[0])
                else:
                    sql = "WHERE %s <= '%s' group by ID" % (
                        self.select_conditions[0], content[0])
            elif len(content) == 2:
                if self.searchEdit.text() == "":
                    sql = "WHERE %s >= '%s' and %s <= '%s' group by ID" % (
                        self.select_conditions[0], content[0], self.select_conditions[0], content[1])
                elif self.dateEdit_2.text() == "":
                    sql = "WHERE %s >= '%s' and %s == '%s' group by ID" % (
                        self.select_conditions[0], content[0], self.select_conditions[1], content[1])
                else:
                    sql = "WHERE %s <= '%s' and %s == '%s' group by ID" % (
                        self.select_conditions[0], content[0], self.select_conditions[1], content[1])
            elif len(content) == 3:
                sql = "WHERE %s >= '%s' and %s <= '%s' and %s = '%s'" % (
                    self.select_conditions[0], content[0], self.select_conditions[0], content[1],
                    self.select_conditions[1], content[2])

            self.queryModel.searchTable(sql)
            self.updateUI()

    #def time(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = Maintenance()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())