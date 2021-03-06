# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_view_str.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmManageSTR(object):
    def setupUi(self, frmManageSTR):
        frmManageSTR.setObjectName(_fromUtf8("frmManageSTR"))
        frmManageSTR.resize(968, 638)
        frmManageSTR.setDocumentMode(False)
        frmManageSTR.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(frmManageSTR)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(380, 0))
        self.frame.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame)
        self.gridLayout_5.setMargin(1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 250))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tbSTREntity = QtGui.QTabWidget(self.groupBox)
        self.tbSTREntity.setObjectName(_fromUtf8("tbSTREntity"))
        self.gridLayout_4.addWidget(self.tbSTREntity, 0, 0, 1, 2)
        self.btnSearch = QtGui.QPushButton(self.groupBox)
        self.btnSearch.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.gridLayout_4.addWidget(self.btnSearch, 1, 0, 1, 1)
        self.btnClearSearch = QtGui.QPushButton(self.groupBox)
        self.btnClearSearch.setMinimumSize(QtCore.QSize(0, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/reset.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClearSearch.setIcon(icon1)
        self.btnClearSearch.setObjectName(_fromUtf8("btnClearSearch"))
        self.gridLayout_4.addWidget(self.btnClearSearch, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolbarVBox = QtGui.QVBoxLayout()
        self.toolbarVBox.setSpacing(0)
        self.toolbarVBox.setObjectName(_fromUtf8("toolbarVBox"))
        self.verticalLayout.addLayout(self.toolbarVBox)
        self.tvSTRResults = QtGui.QTreeView(self.groupBox_2)
        self.tvSTRResults.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tvSTRResults.setAlternatingRowColors(True)
        self.tvSTRResults.setRootIsDecorated(True)
        self.tvSTRResults.setObjectName(_fromUtf8("tvSTRResults"))
        self.tvSTRResults.header().setCascadingSectionResizes(False)
        self.tvSTRResults.header().setDefaultSectionSize(0)
        self.verticalLayout.addWidget(self.tvSTRResults)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.splitter)
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setMargin(1)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.toolBox = QtGui.QToolBox(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.toolBox.setFont(font)
        self.toolBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.toolBox.setFrameShape(QtGui.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtGui.QFrame.Sunken)
        self.toolBox.setLineWidth(1)
        self.toolBox.setMidLineWidth(1)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_1 = QtGui.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 486, 475))
        self.page_1.setObjectName(_fromUtf8("page_1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tbPropertyPreview = SpatialPreview(self.page_1)
        self.tbPropertyPreview.setObjectName(_fromUtf8("tbPropertyPreview"))
        self.verticalLayout_2.addWidget(self.tbPropertyPreview)
        self.toolBox.addItem(self.page_1, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 486, 475))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tbSupportingDocs = QtGui.QTabWidget(self.page_2)
        self.tbSupportingDocs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tbSupportingDocs.setObjectName(_fromUtf8("tbSupportingDocs"))
        self.verticalLayout_3.addWidget(self.tbSupportingDocs)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.toolBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.vl_notification = QtGui.QVBoxLayout()
        self.vl_notification.setObjectName(_fromUtf8("vl_notification"))
        self.gridLayout.addLayout(self.vl_notification, 0, 0, 1, 1)
        frmManageSTR.setCentralWidget(self.centralwidget)
        self.tb_actions = QtGui.QToolBar(frmManageSTR)
        self.tb_actions.setMovable(False)
        self.tb_actions.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tb_actions.setFloatable(False)
        self.tb_actions.setObjectName(_fromUtf8("tb_actions"))
        frmManageSTR.addToolBar(QtCore.Qt.TopToolBarArea, self.tb_actions)

        self.retranslateUi(frmManageSTR)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), frmManageSTR.close)
        QtCore.QMetaObject.connectSlotsByName(frmManageSTR)

    def retranslateUi(self, frmManageSTR):
        frmManageSTR.setWindowTitle(_translate("frmManageSTR", "View Social Tenure Relationship", None))
        self.groupBox.setTitle(_translate("frmManageSTR", "Search By:", None))
        self.btnSearch.setText(_translate("frmManageSTR", "Search", None))
        self.btnClearSearch.setText(_translate("frmManageSTR", "Clear Results", None))
        self.groupBox_2.setTitle(_translate("frmManageSTR", "Search Results:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), _translate("frmManageSTR", "Spatial Unit Preview", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("frmManageSTR", "Supporting Documents", None))
        self.tb_actions.setWindowTitle(_translate("frmManageSTR", "toolBar", None))

from .property_preview import SpatialPreview
from stdm import resources_rc
