import qdarkstyle
import sys

import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import QSize, Qt

from FaultDiagnosis import FaultDiagnosis
from FunctionManageView import FunctionManageWidget
from InStorageView import InStorageWidget
from LifeReminder import LifeReminder
from MR_SearchMRView import SelectMRWidget
from Maintenance import Maintenance
from OutInputDBTimes import OutInputDBTimes
from OutStorageView import OutStorageWidget
from ProductDeliveryRegistration import ProductDeliveryRegistration
from ProductInventory import ProductInventory
from SearchMWView import SearchMWWidget
from UI.AddProductView import AddProductWidget
from UI.KnowledgeBaseManage import KnowledgeBaseManage
from UI.SearchProductBatchDetailView import SelectProductBatchDetailWidget
from Thread.SearchProductBatchThread import SearchProductBatchDetailThread
from UI.SearchProductComponentTypeView import SearchProductComponentTypeWidget
from UI.SearchProductComponentView import SearchProductComponentWidget
from UI.SearchProductView import SelectProductWidget
from UserManageView import UserManageWidget
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QTreeWidget, QTreeWidgetItem,
                             QGroupBox, QStackedWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize



class AdminHome(QWidget):
    def  __init__(self):
        super(AdminHome, self).__init__()
        self.setMinimumHeight(600);
        self.setMinimumWidth(800);
        self.setWindowTitle("欢迎使用产品管理系统")
        ##main_layout.setMargin(5)
        ##main_layout.setSpace(5)
        with open("./leftMenuStyle.qss", 'r', encoding='utf-8') as f:
            self.list_style = f.read()
        self.creat_main_layout()
        self.creat_bar_navigation()
        self.creat_left_box()
        self.setStyleSheet(self.list_style)


    def get_bar_list(self):
        bar_list_item = []
        self.data = []

        bar_list_1 = ["产品信息管理",["产品批次查询", "产品信息查询", "产品组件查询", "组件类型查询",  '产品入库', '产品出库', '产品出入库', '维修保养', '产品交付登记', '产品库存', '寿命到期提醒']]
        bar_list_2 = ["预防性维修保养管理",['维护方式管理', '维护记录管理']]
        bar_list_3 = ["故障诊断与知识库管理", ['故障诊断与处理', '知识库管理']]
        bar_list_4 = ["系统管理", ['业务管理', '用户管理']]
        len1 = len(bar_list_1[1])
        len2 = len(bar_list_2[1]) + len1
        len3 = len(bar_list_3[1]) + len2
        self.data = [0, len1, len2, len3]
        bar_list_item.append(bar_list_1)
        bar_list_item.append(bar_list_2)
        bar_list_item.append(bar_list_3)
        bar_list_item.append(bar_list_4)
        return bar_list_item

    def creat_main_layout(self):
        self.main_layout = QHBoxLayout()
        self.setLayout( self.main_layout)

    def creat_bar_list(self, data):

        for item in data:
            item_1 =  QTreeWidgetItem( self. left_widget)
            item_1.setText(0, item[0])
            ##item_1.setText(0,item[0])
            ## 设置节点的打开/关闭状态下的不同的图片
            icon = QIcon()
            ##节点打开状态
            icon.addPixmap(QPixmap("./Images/"+ self.item_iamges[item[0]] +".png"), QIcon.Normal, QIcon.On)
            item_1.setIcon(0, icon)

            for item_item in item[1]:
                item_1_1 =  QTreeWidgetItem( item_1);
                icon = QIcon()
                ##节点打开状态
                icon.addPixmap(QPixmap("./Images/"+ self.item_iamges[item_item] +".png"), QIcon.Normal, QIcon.On)
                item_1_1.setIcon(0, icon)
                item_1_1.setText(0,item_item)
            self. left_widget.addTopLevelItem(item_1);

    def creat_bar_navigation(self):
        self.item_iamges = {"产品批次查询": "batchsearch",
                       "产品信息查询": "batchsearch",
                       "产品组件查询": "batchsearch",
                       "组件类型查询": "batchsearch",
                       "产品入库": "产品入库",
                       "产品出库": "产品出库",
                       "产品出入库": "产品出入库",
                       "维修保养": "维修保养",
                       "产品交付登记": "维修记录",
                       "产品库存": "产品出入库",
                       "寿命到期提醒": "寿命到期提醒",
                       "维护方式管理": "维修方式",
                       "维护记录管理": "维修记录",
                       "故障诊断与处理": "故障诊断",
                       "知识库管理": "知识库管理",
                       "业务管理": "业务管理",
                       "用户管理": "用户管理",
                       "产品信息管理": "1",
                       "预防性维修保养管理": "维修保养",
                       "故障诊断与知识库管理": "故障诊断",
                       "系统管理": "用户管理",
                       }
        self. left_widget = QTreeWidget()
        self.left_widget.setMinimumWidth(300)
        self.left_widget.setHeaderLabel("左侧导航栏")
        self.left_widget.setColumnCount(1)
        self.left_widget.setMaximumWidth(150)
        self.left_widget.setFocusPolicy(Qt.NoFocus)
        # self.left_widget.setRootIsDecorated(False)

        icon_size = QSize(20, 20)
        self. left_widget.setIconSize(icon_size)

        ##如果treewidget就一列，该列的宽度默认等于treewidget的宽度,两列以上的话才起作用.
        ##self. left_widget.setColumnWidth(0,100);
        data = self.get_bar_list()
        self.creat_bar_list(data)
        self.main_layout.addWidget(self. left_widget)
        ## QModelIndex
        ##self. left_widget.doubleClicked.connect(self.showModelSelected)
        ## QTreeWidgetItem
        # self. left_widget.itemDoubleClicked.connect(self.showSelected)
        self. left_widget.itemClicked.connect(self.showSelected)


    ## itemObj:QTreeWidgetItem
    def showSelected(self, item, column):
        # 获得父节点
        parent = item.parent()

        index_top = 0
        index_row = -1

        if parent is None:
            index_top = self.left_widget.indexOfTopLevelItem(item)
        else:
            index_top = self.left_widget.indexOfTopLevelItem(parent)
            index_row = parent.indexOfChild(item)


        if index_row != -1:
            self.display(self.data[index_top] + index_row)

    def creat_left_box(self):
        self.right_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.right_widget)
        self.__setUpUI()

    def __setUpUI(self):
        """加载界面UI"""
        # # list和右边窗口的index对应绑定
        # self.left_widget.currentRowChanged.connect(self.display)
        # # 去掉边框
        # self.left_widget.setFrameShape(QListWidget.NoFrame)
        # # 隐藏滚动条
        # self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['产品批次查询', '产品信息新建', '产品组件查询', '组件类型查询', '产品入库', '产品出库', '产品出入库', '维修保养', '产品交付登记', '产品库存', '寿命到期提醒', '维护方式管理', '维护记录管理', '故障诊断与处理', '知识库管理', '业务管理', '用户管理']
        # 根据list_str设置对应UI
        url_list = ["self.setSearchBatchView",                  #1
                    "self.setSearchProductView",                #2
                    "self.setSearchProductConponentView",       #3
                    "self.setSearchProductConponentTypeView",   #4
                    "self.setInStorageView",
                    "self.setOutStorageView",
                    "self.setOutInputDBTimes",                  #6
                    "self.setMaintenance",                      #7
                    "self.setProductDeliveryRegistration",      #8
                    "self.setProductInventory",
                    "self.setLifeReminder",
                    "self.setMaintenanceWayView",               #8
                    "self.setMaintenanceRecordView",            #9
                    "self.FaultDiagnosis",
                    "self.setKnowledgeBaseManageWidget",        #5
                    "self.setFunctionManageView",
                    "self.setUserManageView" ]               #12

        for i in range(len(list_str)):
            # # 左侧选项的添加
            # self.item = QListWidgetItem(list_str[i], self.left_widget)
            # self.item.setSizeHint(QSize(30, 60))
            # self.item.setTextAlignment(Qt.AlignCenter)
            # 根据对应函数设置右侧显示内容
            eval(url_list[i] + "()")


    def display(self, i):
        # print(self.right_widget.widget(i))
        # self.a.queryModel.update()
        # self.b.queryModel.update()
        # self.c.queryModel.update()
        self.right_widget.setCurrentIndex(i)


    def setRightWidget(self, layout):
        """
        设置右部QStackWidget中的内容
        :param layout: 含有相应视图的右部布局
        :return:
        """
        widget = QWidget()
        widget.setLayout(layout)
        self.right_widget.addWidget(widget)

    def setRightWidget1(self, myWidget):
        """
        设置右部QStackWidget中的内容
        :param layout: 含有相应视图的右部布局
        :return:
        """
        widget = QWidget()
        myWidget.setupUi(widget)
        self.right_widget.addWidget(widget)

    def addProductView(self):
        """产品信息添加的UI"""
        self.tt = AddProductWidget()
        self.setRightWidget1(self.tt)

    def setSearchBatchView(self):
        """设置产品批次查询的UI"""
        self.a = SelectProductBatchDetailWidget()
        self.setRightWidget1(self.a)

    def setSearchProductView(self):
        """设置产品查询的UI"""
        self.b = SelectProductWidget()
        self.setRightWidget1(self.b)

    def setSearchProductConponentTypeView(self):
        """设置产品组件类型查询的UI"""
        self.c = SearchProductComponentTypeWidget()
        self.setRightWidget1(self.c)

    def setSearchProductConponentView(self):
        """设置产品组件查询的UI"""
        self.d = SearchProductComponentWidget()
        self.setRightWidget1(self.d)

    def setInStorageView(self):
        """设置入库管理的UI"""
        self.r = InStorageWidget()
        self.setRightWidget1(self.r)

    def setOutStorageView(self):
        """设置出库管理的UI"""
        self.s = OutStorageWidget()
        self.setRightWidget1(self.s)

    def setKnowledgeBaseManageWidget(self):
        """设置知识库管理UI"""
        self.e = KnowledgeBaseManage()
        self.setRightWidget1(self.e)

    # 设置右侧的业务管理功能
    def setFunctionManageView(self):
        self.f = FunctionManageWidget()
        self.setRightWidget1(self.f)

    # 设置右侧的用户管理界面
    def setUserManageView(self):
        self.e = UserManageWidget()
        self.setRightWidget1(self.e)
        # print("UserManageWidget初始化完成")

    def updateSearchProductBatchDetailWidget(self):
        """
        更新产品批次查询的视图
        :return:
        """
        print(11111)
        # self.myWidget.update()
        self.myWidget.queryModel.update()

    def setOutInputDBTimes(self):
        '''产品出入库'''
        self.o = OutInputDBTimes()
        self.setRightWidget1(self.o)

    def setMaintenance(self):
        '''维修保养'''
        self.m = Maintenance()
        self.setRightWidget1(self.m)

    def setProductDeliveryRegistration(self):
        '''产品交付登记'''
        self.d = ProductDeliveryRegistration()
        self.setRightWidget1(self.d)

    def setProductInventory(self):
        '''产品库存'''
        self.i = ProductInventory()
        self.setRightWidget1(self.i)

    def setLifeReminder(self):
        '''寿命到期提醒'''
        self.l = LifeReminder()
        self.setRightWidget1(self.l)

    def setMaintenanceWayView(self):
        """设置维保方式的UI"""
        self.h = SearchMWWidget()
        self.setRightWidget1(self.h)

    def setMaintenanceRecordView(self):
        """设置维保方式的UI"""
        self.j = SelectMRWidget()
        self.setRightWidget1(self.j)

    def FaultDiagnosis(self):
        """
        xcy 设置故障诊断界面
        :return:
        """
        self.k = FaultDiagnosis()
        self.setRightWidget1(self.k)
        print("设置故障诊断界面")


    def test(self):
        pass


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = AdminHome()
    window.show()

    sys.exit(app.exec_())