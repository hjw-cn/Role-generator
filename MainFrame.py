# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Roles.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

# 导入PyQt5中用到的类和自己写的角色类
from PyQt5 import QtCore, QtGui, QtWidgets
import Roles
import random


class MainFrame(QtWidgets.QDialog):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.setObjectName("Object")
        self.resize(724, 556)
        self.setSizeGripEnabled(False)
        self.setModal(False)

        # 添加widget
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 724, 556))
        self.widget.setObjectName("widget")

        # 添加背景图片
        bg = QtGui.QPixmap(r'C:\Users\Administrator\Desktop\pyTest\homework\images\bea.jpg')
        pal = QtGui.QPalette()
        pal.setBrush(self.backgroundRole(), QtGui.QBrush(bg))
        self.widget.setPalette(pal)
        self.widget.setAutoFillBackground(True)
        # 添加buttonBox
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(230, 500, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(120, 30, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # 这里添加了一个Qlabel 用来显示角色预览图片
        self.RoleImg = QtWidgets.QLabel(self)
        self.RoleImg.setEnabled(True)
        self.RoleImg.setGeometry(QtCore.QRect(40, 60, 231, 291))  # 预览区大小
        self.RoleImg.setMouseTracking(False)
        self.RoleImg.setText("")
        self.RoleImg.setObjectName("RoleImg")

        #添加QComboBox实现角色选择
        self.Roles = QtWidgets.QComboBox(self)
        self.Roles.setGeometry(QtCore.QRect(420, 110, 191, 22))
        self.Roles.setFrame(True)
        self.Roles.setObjectName("Roles")
        self.Roles.addItem("")
        self.Roles.addItem("")
        self.Roles.addItem("")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(320, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # 添加QLineEdit实现用户输入昵称功能
        self.Nickname = QtWidgets.QLineEdit(self)
        self.Nickname.setGeometry(QtCore.QRect(420, 310, 181, 31))
        self.Nickname.setObjectName("Nickname")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(370, 310, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # 选择种族
        self.Race = QtWidgets.QComboBox(self)
        self.Race.setGeometry(QtCore.QRect(420, 160, 191, 22))
        self.Race.setFrame(True)
        self.Race.setObjectName("Race")
        self.Race.addItem("")
        self.Race.addItem("")
        self.Race.addItem("")
        self.Race.addItem("")
        self.Race.addItem("")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(320, 160, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # 选择职业
        self.Profession = QtWidgets.QComboBox(self)
        self.Profession.setGeometry(QtCore.QRect(420, 210, 191, 22))
        self.Profession.setFrame(True)
        self.Profession.setObjectName("Profession")
        self.Profession.addItem("")
        self.Profession.addItem("")
        self.Profession.addItem("")
        self.Profession.addItem("")
        self.Profession.addItem("")
        self.Profession.addItem("")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(320, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(320, 260, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.Sex = QtWidgets.QComboBox(self)
        self.Sex.setGeometry(QtCore.QRect(420, 260, 191, 22))
        self.Sex.setFrame(True)
        self.Sex.setObjectName("Sex")
        self.Sex.addItem("")
        self.Sex.addItem("")

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 380, 700, 65))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 85, 127))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(89)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(19)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.bind_event()

    def bind_event(self):
        self.Roles.activated[str].connect(self.show_image)
        self.Race.activated[str].connect(self.sel_race)
        self.Profession.activated[str].connect(self.sel_profession)
        self.Sex.activated[str].connect(self.set_sex)

    def retranslateUi(self, Object):
        _translate = QtCore.QCoreApplication.translate
        Object.setWindowTitle(_translate("Object", "初始化角色"))

        self.label.setText(_translate("Object", "角色预览"))
        self.Roles.setItemText(0, _translate("Object", "大蛇丸"))
        self.Roles.setItemText(1, _translate("Object", "角色1"))
        self.Roles.setItemText(2, _translate("Object", "角色2"))
        self.label_2.setText(_translate("Object", "选择角色"))
        self.label_3.setText(_translate("Object", "昵称"))
        self.Race.setItemText(0, _translate("Object", "人类"))
        self.Race.setItemText(1, _translate("Object", "精灵"))
        self.Race.setItemText(2, _translate("Object", "兽人"))
        self.Race.setItemText(3, _translate("Object", "矮人"))
        self.Race.setItemText(4, _translate("Object", "元素"))

        self.Profession.setItemText(0, _translate("Object", "狂战士"))
        self.Profession.setItemText(1, _translate("Object", "圣骑士"))
        self.Profession.setItemText(2, _translate("Object", "刺客"))
        self.Profession.setItemText(3, _translate("Object", "猎手"))
        self.Profession.setItemText(4, _translate("Object", "祭司"))
        self.Profession.setItemText(5, _translate("Object", "巫师"))

        self.label_4.setText(_translate("Object", "选择种族"))

        self.label_5.setText(_translate("Object", "选择职业"))
        self.label_6.setText(_translate("Object", "选择性别"))
        self.Sex.setItemText(0, _translate("Object", "男"))
        self.Sex.setItemText(1, _translate("Object", "女"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Object", "能力值"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Object", "力量"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Object", "敏捷"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Object", "体力"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Object", "智力"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Object", "智慧"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Object", "生命"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Object", "魔法"))

    def all_show(self):
        """
        辅助函数，使职业组合框中的所有职业都显示出来，配合sel_race()使用
        :return:
        """
        self.Profession.view().setRowHidden(0, False)
        self.Profession.view().setRowHidden(1, False)
        self.Profession.view().setRowHidden(2, False)
        self.Profession.view().setRowHidden(3, False)
        self.Profession.view().setRowHidden(4, False)
        self.Profession.view().setRowHidden(5, False)

    def show_image(self, text):
        """
        实现角色图片显示，预览
        :param text:  组合框传入的选中的选项值
        :return:
        """
        pix1 = QtGui.QPixmap(r'C:\Users\Administrator\Desktop\pyTest\homework\images\大蛇丸.png')
        pix2 = QtGui.QPixmap(r'C:\Users\Administrator\Desktop\pyTest\homework\images\1.png')
        pix3 = QtGui.QPixmap(r'C:\Users\Administrator\Desktop\pyTest\homework\images\2.png')
        if text == "大蛇丸":
            self.RoleImg.setPixmap(pix1)
        elif text == "角色1":
            self.RoleImg.setPixmap(pix2)
        else:
            self.RoleImg.setPixmap(pix3)
        self.RoleImg.setScaledContents(True)

    def sel_race(self, text):         # 此方法与CombineBox绑定 根据传入的text选择种族
        """
        实现选择种族的功能
        :param text: 选择种族组合框传入的选中的选项值
        :return:
        """
        if text == "人类":
            role.race = "人类"
            self.all_show()
        elif text == "精灵":
            self.all_show()
            role.race = "精灵"
            self.Profession.view().setRowHidden(0, True)
            self.Profession.view().setRowHidden(1, True)   # 如果种族为精灵 隐藏职业选项里不允许选择的职业
        elif text == "兽人":
            self.all_show()
            role.race = "兽人"
            self.Profession.view().setRowHidden(1, True)
            self.Profession.view().setRowHidden(2, True)
            self.Profession.view().setRowHidden(5, True)
        elif text == "矮人":
            self.all_show()
            role.race = "矮人"
            self.Profession.view().setRowHidden(2, True)
            self.Profession.view().setRowHidden(3, True)
            self.Profession.view().setRowHidden(5, True)
        elif text == "元素":
            self.all_show()
            role.race = "元素"
            self.Profession.view().setRowHidden(0, True)
            self.Profession.view().setRowHidden(1, True)
            self.Profession.view().setRowHidden(2, True)
            self.Profession.view().setRowHidden(3, True)
        print(role.race)

    def sel_profession(self, text):
        """
        用组合框组件实现选择职业功能
        此方法与CombineBox绑定 根据传入的text选择职业
        :param text: 组合框传入参数text
        :return:
        """
        print(text)
        if text == "狂战士":
            role.profession = "狂战士"
        elif text == "圣骑士":
            role.profession = "圣骑士"
        elif text == "刺客":
            role.profession = "刺客"
        elif text == "猎手":
            role.profession = "猎手"
        elif text == "祭司":
            role.profession = "祭司"
        elif text == "巫师":
            role.profession = "巫师"
        print(role.profession)

    def set_sex(self, text):
        if text == "男":
            role.sex = "男"
        else:
            role.sex = "女"
        print(role.sex)

    def accept(self):
        """
        添加角色
        :return:
        """
        role.nickname = self.Nickname.text()
        if role.nickname == "":
            # 如果没有输入昵称，弹窗提示
            QtWidgets.QMessageBox.about(self, "提示", "请输入昵称后确认")
            print(role.nickname)
        else:
            # 弹窗提示角色创建成功
            QtWidgets.QMessageBox.about(self, "提示", "添加角色成功")
            self.set_property()
            self.show_property()

    def set_property(self):
        """
        根据表中初始值的比例
        随机初始化角色的属性值并且属性值的总和为100
        :return:
        """
        if self.Profession.currentText() == "狂战士":
            role.strength = 40+random.randint(-3, 3)
            role.agility = role.strength // 2
            role.power = 3 * role.strength // 4
            role.intelligence = role.strength // 8
            role.wisdom = 100 - (role.strength + role.agility + role.power + role.intelligence)
        elif self.Profession.currentText() == "圣骑士":
            role.strength = 25 + random.randint(-5, 5)
            role.agility = 3 * role.strength // 5
            role.power = 2 * role.agility
            role.intelligence = 2 * role.power // 3
            role.wisdom = 100 - (role.strength + role.agility + role.power + role.intelligence)
        elif self.Profession.currentText() == "刺客":
            role.strength = 20 + random.randint(-2, 2)
            role.agility = 7 * role.strength // 4
            role.power = role.strength + random.randint(-1, 1)
            role.intelligence = role.power // 2
            role.wisdom = 100 - (role.strength + role.agility + role.power + role.intelligence)
        elif self.Profession.currentText() == "猎手":
            role.strength = 15 + random.randint(-2, 2)
            role.agility = 8 * role.strength // 3
            role.power = role.strength + random.randint(-1, 1)
            role.intelligence = role.agility // 4
            role.wisdom = 100 - (role.strength + role.agility + role.power + role.intelligence)
        elif self.Profession.currentText() == "祭司":
            role.strength = 15 + random.randint(-2, 2)
            role.agility = 4 * role.strength // 3
            role.power = role.strength + random.randint(-1, 1)
            role.intelligence = 7 * role.power // 3
            role.wisdom = 100 - (role.strength + role.agility + role.power + role.intelligence)
        elif self.Profession.currentText() == "巫师":
            role.strength = 10 + random.randint(-2, 2)
            role.agility = 2 * role.strength
            role.power = role.strength + random.randint(-1, 1)
            role.intelligence = 2 * role.power
            role.wisdom = 100 - (role.strength + role.agility + role.power + role.intelligence)
        role.life = role.power * 20
        role.magic = (role.intelligence + role.wisdom) * 10

    def show_property(self):
        """
        将角色的5大属性值显示在表格中
        :return:
        """
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(role.strength)))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(role.agility)))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(role.power)))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(role.intelligence)))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(role.wisdom)))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(role.life)))
        self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(str(role.magic)))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    role = Roles.Role()
    # widget = QtWidgets.QDialog()
    ui = MainFrame()
    # ui.setupUi(widget)
    # widget.show()
    ui.show()
    print(role.nickname)
    sys.exit(app.exec_())