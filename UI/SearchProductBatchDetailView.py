# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchProductBatchDetailView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QTableView, QHeaderView, QMessageBox, QDialog, QWidget, QApplication

from UI.MySearchBatchModel import MySearchBatchTableModel, CheckBoxHeader
from UI.SelectSingleProductView import SelectSingleProductWidget
from UI.addProductBatchView import AddProductBatchWidget


class SelectProductBatchDetailWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 813)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addBatchButton = QtWidgets.QPushButton(Form)
        self.addBatchButton.setObjectName("addBatchButton")
        self.horizontalLayout_5.addWidget(self.addBatchButton)
        self.selectProduct = QtWidgets.QPushButton(Form)
        self.selectProduct.setObjectName("selectProduct")
        self.horizontalLayout_5.addWidget(self.selectProduct)
        self.alterVBatchButton = QtWidgets.QPushButton(Form)
        self.alterVBatchButton.setObjectName("alterVBatchButton")
        self.horizontalLayout_5.addWidget(self.alterVBatchButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.deleteBatchButton = QtWidgets.QPushButton(Form)
        self.deleteBatchButton.setObjectName("deleteBatchButton")
        self.horizontalLayout_3.addWidget(self.deleteBatchButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # 中间手动代码部分 表格UI构建
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("./db/ProductManagement_new.db")
        self.db.open()
        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # hsj 自动义的tableModel
        self.queryModel = MySearchBatchTableModel()

        # self.queryModel.setTable("T_Product_BatchDetail")
        # # self.queryModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        # self.queryModel.select()
        #
        # self.queryModel.setHeaderData(0, Qt.Horizontal, "ID")
        # self.queryModel.setHeaderData(1, Qt.Horizontal, "产品ID")
        # self.queryModel.setHeaderData(2, Qt.Horizontal, "批次号")
        # self.queryModel.setHeaderData(3, Qt.Horizontal, "交付日期")
        # self.queryModel.setHeaderData(4, Qt.Horizontal, "交付人员")
        # self.queryModel.setHeaderData(5, Qt.Horizontal, "接收单位")
        # self.queryModel.setHeaderData(6, Qt.Horizontal, "接收人员")
        # self.queryModel.setHeaderData(8, Qt.Horizontal, "创建人员ID")
        # self.queryModel.setHeaderData(9, Qt.Horizontal, "创建时间")
        # self.queryModel.setHeaderData(10, Qt.Horizontal, "修改人员ID")
        # self.queryModel.setHeaderData(11, Qt.Horizontal, "修改时间")
        # self.queryModel.setHeaderData(12, Qt.Horizontal, "备注")


        self.tableView.setModel(self.queryModel)
        self.header = CheckBoxHeader()
        self.tableView.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.queryModel.headerClick)
        self.tableView.setModel(self.queryModel)
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
        self.label.setText(_translate("Form", "产品批次查询"))
        self.addBatchButton.setText(_translate("Form", "新建批次"))
        self.selectProduct.setText(_translate("Form", "查看产品"))
        self.alterVBatchButton.setText(_translate("Form", "修改批次"))
        self.deleteBatchButton.setText(_translate("Form", "删除批次"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按批次号查询"))
        self.comboBox.setItemText(1, _translate("Form", "按产品编号查询"))
        self.comboBox.setItemText(2, _translate("Form", "按接收单位查询"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))
        self.totalPageLabel.setText(_translate("Form", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))

    def updateUI(self):
        """
        hsj 跳转的后更新
        :return:
        """
        self.jumpEdit.setText(str(self.queryModel.currentPage + 1))


    def bindButton(self):
        """
        hsj 绑定按钮
        :return:
        """
        # 删除按钮
        self.deleteBatchButton.clicked.connect(self.deleteButtonEvent)
        # 新建按钮
        self.addBatchButton.clicked.connect(self.addButtonEvent)
        # 查看产品
        self.selectProduct.clicked.connect(self.selectDetailProductButtonEvent)
        # 修改批次
        self.alterVBatchButton.clicked.connect(self.updateButtonEvent)
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)


    def deleteButtonEvent(self):
        """
        hsj 删除批次按钮绑定事件
        :return:
        """
        # print(self.queryModel.checkList.count("Checked"))
        # 如果没有选中数据，则提示无数据
        if self.queryModel.checkList.count("Checked") == 0:
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return
        a = QMessageBox.information(QDialog(), "提示", "是否确认删除？", QMessageBox.Yes, QMessageBox.No)
        if a == QMessageBox.No:
            return
        self.queryModel.delete()
        self.queryModel.update()

    def addButtonEvent(self):
        """
        hsj 新建产品批次
        :return:
        """
        form = QDialog()
        w = AddProductBatchWidget()
        w.setupUi(form)
        form.show()
        a = form.exec_()
        # 如果对话框关闭，则对查询数据进行更行
        if a == 0:
            self.queryModel.refreshPage()
            self.queryModel.update()

    def selectDetailProductButtonEvent(self):
        """
        hsj 根据批次中的产品Id查询产品详细信息
        :return:
        """
        a = self.isCorrect()
        if a == 0:
            return
        result = self.queryModel.selectSingleProduct()
        productDiglog = SelectSingleProductWidget()
        form = QDialog()
        productDiglog.setupUi(form)
        productDiglog.setData(result)
        form.show()
        form.exec()


    def updateButtonEvent(self):
        """
        hsj 修改产品批次信息
        :return:
        """
        a = self.isCorrect()
        if a == 0:
            return
        result = self.queryModel.selectSingleBatch()
        batchDialog = AddProductBatchWidget()
        form = QDialog()
        batchDialog.setupUi(form)
        batchDialog.updateData(result, self.queryModel)
        form.show()
        a = form.exec()
        # 如果对话框关闭，则对查询数据进行更行
        if a == 0:
            self.queryModel.update()

    def isCorrect(self):
        """
        hsj 判断复选框是否选中一个数据
        :return:
        """
        if self.queryModel.checkList.count("Checked") == 0:
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return 0
        elif self.queryModel.checkList.count("Checked") > 1:
            QMessageBox.warning(QDialog(), "警告", "数据过多，请选中一条后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return 0
        else:
            return 1

    def preButtonEvent(self):
        """
        hsj 上一页按钮事件
        :return:
        """
        if self.queryModel.currentPage == 0:
            QMessageBox.information(QDialog(), "提示", "已经是第一页！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            self.queryModel.prePage()
            self.queryModel.update()
            self.updateUI()

    def nextButtonEvent(self):
        """
        hsj 下一页按钮事件
        :return:
        """
        if (self.queryModel.currentPage + 1) == self.queryModel.totalPage:
            QMessageBox.information(QDialog(), "提示", "已经是最后一页！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            self.queryModel.nextPage()
            self.queryModel.update()
            self.updateUI()



    def jumpButtonEvent(self):
        """
        hsj 跳转按钮事件
        :return:
        """
        objectPage = self.jumpEdit.text()
        if not objectPage.isdigit():
            QMessageBox.information(QDialog(), "提示", "跳转输入的不是数字，请正确填写后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            objectPage = int(objectPage)
            if objectPage <= 0 or objectPage > self.queryModel.totalPage:
                QMessageBox.information(QDialog(), "提示", "跳转输入超出范围，请正确填写后重试！", QMessageBox.Yes, QMessageBox.Yes)
                return
            else:
                self.queryModel.currentPage = objectPage - 1
                self.queryModel.setCurrentData()
                self.queryModel.update()

    def searchButtonEvent(self):
        """
        hsj 输入查询条件查询按钮事件
        :return:
        """
        content = self.searchEdit.text()
        select_condition = ""
        if content == "":
            print(111)
            self.queryModel.refreshPage()
            self.queryModel.update()
        else:
            n = self.comboBox.currentIndex()
            if n == 0:
                select_condition = "BatchNO"
            elif n == 1:
                select_condition = "ProductID"
            elif n == 2:
                select_condition = "ReceiveCompanyName"
            self.queryModel.selectBatch(select_condition, content)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SelectProductBatchDetailWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())