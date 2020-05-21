import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)

from Thread.SearchProductBatchThread import SearchProductBatchDetailThread


class CheckBoxHeader(QHeaderView):
    clicked = pyqtSignal(bool)

    _x_offset = 3
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height()-self._width)/2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                self.clicked.emit(self.isOn)
                self.update()
        super(CheckBoxHeader, self).mousePressEvent(event)


class MySearchBatchTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(MySearchBatchTableModel, self).__init__(parent)

        # 总数据
        self.totalData = self.getData()

        # hsj 每页显示的信息数, 总页数
        self.perPageNum = 10
        self.currentPage = 0
        self.data_list = []
        self.totalPage = self.getTotalPage()
        print(self.totalPage)

        if len(self.totalData) <= self.perPageNum:
            self.data_list = self.totalData
        else:
            self.data_list = self.totalData[:self.perPageNum]

        # self.data_list = self.getData()
        # Keep track of which object are checked
        self.headerRow = ["批次号", "ID", "产品编号", "交付日期", "交付单位", "交付人员", "接收单位", "接收人员", "创建人员ID", "创建时间", "修改人员ID", "修改时间", "备注"]
        self.checkList = ['Unchecked' for i in range(len(self.data_list))]




    def rowCount(self, QModelIndex):
        # print(len(self.data_list))
        return len(self.data_list)

    def columnCount(self, QModelIndex):
        return len(self.headerRow)

    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return self.data_list[row][col]
        elif role == Qt.CheckStateRole:
            if col == 0:
                return Qt.Checked if self.checkList[row] == 'Checked' else Qt.Unchecked
        elif role == Qt.ToolTipRole:
            if col == 0:
                return self.checkList[row]
        elif role == Qt.TextAlignmentRole:
            return QVariant(Qt.AlignCenter)
        return QVariant()

    def setData(self, index, value, role):
        row = index.row()
        col = index.column()
        if role == Qt.CheckStateRole and col == 0:
            self.checkList[row] = 'Checked' if value == Qt.Checked else 'Unchecked'
            # print(self.checkList)
        return True

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        return Qt.ItemIsEnabled

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headerRow[section]

    def headerClick(self, isOn):
        self.update()
        self.beginResetModel()
        if isOn:
            self.checkList = ['Checked' for i in range(len(self.data_list))]
            # print(1111)
        else:
            self.checkList = ['Unchecked' for i in range(len(self.data_list))]
        self.endResetModel()

    def delete(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        # db.setDatabaseName("../db/ProductManagement_new.db")
        db.setDatabaseName("./db/ProductManagement_new.db")  # 整合框架时使用
        db.open()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM T_Product_BatchDetail WHERE BatchNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                # sql = "DELETE FROM T_Product WHERE ProductNO = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
                # sql = "DELETE FROM T_Product_Component WHERE ProductID = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
        db.commit()
        self.refreshPage()

    def selectSingleProduct(self):
        """
        hsj 查询单个产品信息
        :return:
        """
        list = []
        db = QSqlDatabase.addDatabase("QSQLITE")
        # db.setDatabaseName("../db/ProductManagement_new.db")
        db.setDatabaseName("./db/ProductManagement_new.db")  # 整合框架时使用
        db.open()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM T_Product WHERE ProductNO = '%s'" % (self.data_list[i][2])
                query.exec(sql)
                break
        if query.next():
            list = [str(query.value(i)) for i in range(14)]
        # print(list)
        return list

    def selectSingleBatch(self):
        """
        hsj 查询单个批次信息
        :return:
        """
        list = []
        db = QSqlDatabase.addDatabase("QSQLITE")
        # db.setDatabaseName("../db/ProductManagement_new.db")
        db.setDatabaseName("./db/ProductManagement_new.db")  # 整合框架时使用
        db.open()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM T_Product_BatchDetail WHERE BatchNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                break
        if query.next():
            list = [str(query.value(i)) for i in range(13)]
        # print(list)
        return list

    def selectBatch(self, select_condition, content):
        """
        hsj 根据条件查询信息，并返回界面
        :param select_condition: 列名
        :param content: 具体查询条件
        :return:
        """
        list = []
        db = QSqlDatabase.addDatabase("QSQLITE")
        # db.setDatabaseName("../db/ProductManagement_new.db")
        db.setDatabaseName("./db/ProductManagement_new.db")  # 整合框架时使用
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM T_Product_BatchDetail WHERE %s = '%s'" % (select_condition, content)
        print(sql)
        query.exec(sql)
        while query.next():
            list.append([str(query.value(i)) for i in range(13)])
        print(list)
        self.data_list = list
        self.update()


    def getData(self):
        results = []
        db = QSqlDatabase.addDatabase("QSQLITE")
        # db.setDatabaseName("../db/ProductManagement_new.db")
        db.setDatabaseName("./db/ProductManagement_new.db")  # 整合框架时使用
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM T_Product_BatchDetail"
        query.exec(sql)
        # print('已查询')
        while(query.next()):
            results.append([query.value(i) for i in range(13)])
        return results

    def update(self):
        self.beginResetModel()
        self.checkList = ['Unchecked' for i in range(len(self.data_list))]
        # print(self.data_list)
        self.endResetModel()

    def getTotalPage(self):
        """
        hsj 得到总页数
        :return:
        """
        return len(self.totalData) // self.perPageNum + 1

    def prePage(self):
        """
        上一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage - 1
        self.setCurrentData()
        self.update()


    def nextPage(self):
        """
        hsj 下一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage + 1
        self.setCurrentData()
        # print("---------------",len(self.data_list))
        self.update()

    def lastPage(self):
        """
        hsj 最后一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage + 1
        self.data_list = self.totalData[self.currentPage * self.perPageNum:]
        self.update()

    def setCurrentData(self):
        """
        hsj 设置当前页码的数据
        :return:
        """
        self.data_list = self.totalData[self.currentPage * self.perPageNum:(self.currentPage + 1) * self.perPageNum]

    def refreshPage(self):
        """
        hsj 添加，删除后，刷新当前页内的信息
        :return:
        """
        self.totalData = self.getData()
        self.totalPage = self.getTotalPage()
        self.data_list = self.totalData[self.currentPage * self.perPageNum:(self.currentPage + 1) * self.perPageNum]





if __name__ == '__main__':
    a = QApplication(sys.argv)
    tableView = QTableView()
    myModel = MySearchBatchTableModel()
    tableView.setModel(myModel)
    header = CheckBoxHeader()
    tableView.setHorizontalHeader(header)
    header.clicked.connect(myModel.headerClick)
    tableView.showMaximized()
    tableView.show()
    a.exec_()