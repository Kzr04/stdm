# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stdm_config.ui'
#
# Created: Tue Jun 21 07:53:49 2016
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_STDMWizard(object):
    def setupUi(self, STDMWizard):
        STDMWizard.setObjectName(_fromUtf8("STDMWizard"))
        STDMWizard.setWindowModality(QtCore.Qt.WindowModal)
        STDMWizard.resize(647, 542)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(STDMWizard.sizePolicy().hasHeightForWidth())
        STDMWizard.setSizePolicy(sizePolicy)
        STDMWizard.setMinimumSize(QtCore.QSize(255, 100))
        STDMWizard.setBaseSize(QtCore.QSize(0, 460))
        STDMWizard.setModal(True)
        STDMWizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        self.wpLicense = QtGui.QWizardPage()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wpLicense.setFont(font)
        self.wpLicense.setObjectName(_fromUtf8("wpLicense"))
        self.gridLayout_2 = QtGui.QGridLayout(self.wpLicense)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_16 = QtGui.QGroupBox(self.wpLicense)
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.gridLayout_20 = QtGui.QGridLayout(self.groupBox_16)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.rbAccpt = QtGui.QRadioButton(self.groupBox_16)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rbAccpt.setFont(font)
        self.rbAccpt.setChecked(False)
        self.rbAccpt.setObjectName(_fromUtf8("rbAccpt"))
        self.gridLayout_20.addWidget(self.rbAccpt, 2, 0, 1, 1)
        self.rbReject = QtGui.QRadioButton(self.groupBox_16)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rbReject.setFont(font)
        self.rbReject.setCheckable(True)
        self.rbReject.setChecked(False)
        self.rbReject.setObjectName(_fromUtf8("rbReject"))
        self.gridLayout_20.addWidget(self.rbReject, 2, 1, 1, 1)
        self.txtLicense = QtGui.QTextEdit(self.groupBox_16)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtLicense.setFont(font)
        self.txtLicense.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtLicense.setFrameShadow(QtGui.QFrame.Raised)
        self.txtLicense.setObjectName(_fromUtf8("txtLicense"))
        self.gridLayout_20.addWidget(self.txtLicense, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_16, 0, 0, 1, 1)
        STDMWizard.addPage(self.wpLicense)
        self.wpPathSetting = QtGui.QWizardPage()
        self.wpPathSetting.setObjectName(_fromUtf8("wpPathSetting"))
        self.formLayout_2 = QtGui.QFormLayout(self.wpPathSetting)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout.setVerticalSpacing(100)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnTemplates = QtGui.QPushButton(self.wpPathSetting)
        self.btnTemplates.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/open_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTemplates.setIcon(icon)
        self.btnTemplates.setObjectName(_fromUtf8("btnTemplates"))
        self.gridLayout.addWidget(self.btnTemplates, 2, 2, 1, 1)
        self.btnDocOutput = QtGui.QPushButton(self.wpPathSetting)
        self.btnDocOutput.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDocOutput.setIcon(icon)
        self.btnDocOutput.setObjectName(_fromUtf8("btnDocOutput"))
        self.gridLayout.addWidget(self.btnDocOutput, 1, 2, 1, 1)
        self.edtTemplatePath = QtGui.QLineEdit(self.wpPathSetting)
        self.edtTemplatePath.setMinimumSize(QtCore.QSize(0, 30))
        self.edtTemplatePath.setReadOnly(True)
        self.edtTemplatePath.setObjectName(_fromUtf8("edtTemplatePath"))
        self.gridLayout.addWidget(self.edtTemplatePath, 2, 1, 1, 1)
        self.label_37 = QtGui.QLabel(self.wpPathSetting)
        self.label_37.setMinimumSize(QtCore.QSize(0, 0))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout.addWidget(self.label_37, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.wpPathSetting)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_31 = QtGui.QLabel(self.wpPathSetting)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout.addWidget(self.label_31, 1, 0, 1, 1)
        self.edtOutputPath = QtGui.QLineEdit(self.wpPathSetting)
        self.edtOutputPath.setMinimumSize(QtCore.QSize(0, 30))
        self.edtOutputPath.setReadOnly(True)
        self.edtOutputPath.setObjectName(_fromUtf8("edtOutputPath"))
        self.gridLayout.addWidget(self.edtOutputPath, 1, 1, 1, 1)
        self.btnDocPath = QtGui.QPushButton(self.wpPathSetting)
        self.btnDocPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDocPath.setIcon(icon)
        self.btnDocPath.setObjectName(_fromUtf8("btnDocPath"))
        self.gridLayout.addWidget(self.btnDocPath, 0, 2, 1, 1)
        self.edtDocPath = QtGui.QLineEdit(self.wpPathSetting)
        self.edtDocPath.setMinimumSize(QtCore.QSize(0, 30))
        self.edtDocPath.setToolTip(_fromUtf8(""))
        self.edtDocPath.setText(_fromUtf8(""))
        self.edtDocPath.setReadOnly(True)
        self.edtDocPath.setObjectName(_fromUtf8("edtDocPath"))
        self.gridLayout.addWidget(self.edtDocPath, 0, 1, 1, 1)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.SpanningRole, self.gridLayout)
        STDMWizard.addPage(self.wpPathSetting)
        self.wpProfile = QtGui.QWizardPage()
        self.wpProfile.setObjectName(_fromUtf8("wpProfile"))
        self.formLayout_5 = QtGui.QFormLayout(self.wpProfile)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.groupBox_18 = QtGui.QGroupBox(self.wpProfile)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_18.sizePolicy().hasHeightForWidth())
        self.groupBox_18.setSizePolicy(sizePolicy)
        self.groupBox_18.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_18.setMaximumSize(QtCore.QSize(800, 400))
        self.groupBox_18.setStyleSheet(_fromUtf8("font: 75 9pt \"Myriad Web Pro\";"))
        self.groupBox_18.setObjectName(_fromUtf8("groupBox_18"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_18)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnNewEntity = QtGui.QPushButton(self.groupBox_18)
        self.btnNewEntity.setMinimumSize(QtCore.QSize(20, 20))
        self.btnNewEntity.setMaximumSize(QtCore.QSize(30, 25))
        self.btnNewEntity.setBaseSize(QtCore.QSize(30, 25))
        self.btnNewEntity.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNewEntity.setIcon(icon1)
        self.btnNewEntity.setObjectName(_fromUtf8("btnNewEntity"))
        self.horizontalLayout.addWidget(self.btnNewEntity)
        self.btnEditEntity = QtGui.QPushButton(self.groupBox_18)
        self.btnEditEntity.setMinimumSize(QtCore.QSize(20, 20))
        self.btnEditEntity.setMaximumSize(QtCore.QSize(30, 25))
        self.btnEditEntity.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditEntity.setIcon(icon2)
        self.btnEditEntity.setObjectName(_fromUtf8("btnEditEntity"))
        self.horizontalLayout.addWidget(self.btnEditEntity)
        self.btnDeleteEntity = QtGui.QPushButton(self.groupBox_18)
        self.btnDeleteEntity.setMinimumSize(QtCore.QSize(20, 20))
        self.btnDeleteEntity.setMaximumSize(QtCore.QSize(30, 25))
        self.btnDeleteEntity.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeleteEntity.setIcon(icon3)
        self.btnDeleteEntity.setObjectName(_fromUtf8("btnDeleteEntity"))
        self.horizontalLayout.addWidget(self.btnDeleteEntity)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        self.pftableView = QtGui.QTableView(self.groupBox_18)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pftableView.sizePolicy().hasHeightForWidth())
        self.pftableView.setSizePolicy(sizePolicy)
        self.pftableView.setMaximumSize(QtCore.QSize(16777215, 600))
        self.pftableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.pftableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.pftableView.setObjectName(_fromUtf8("pftableView"))
        self.pftableView.horizontalHeader().setStretchLastSection(True)
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.pftableView)
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.SpanningRole, self.groupBox_18)
        self.groupBox_17 = QtGui.QGroupBox(self.wpProfile)
        self.groupBox_17.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_17.setMaximumSize(QtCore.QSize(800, 300))
        self.groupBox_17.setObjectName(_fromUtf8("groupBox_17"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_17)
        self.gridLayout_5.setContentsMargins(-1, 3, -1, 9)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_17)
        self.label_3.setMargin(0)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_17)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.cboProfile = QtGui.QComboBox(self.groupBox_17)
        self.cboProfile.setMinimumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cboProfile.setFont(font)
        self.cboProfile.setObjectName(_fromUtf8("cboProfile"))
        self.gridLayout_5.addWidget(self.cboProfile, 0, 1, 1, 1)
        self.lblDesc = QtGui.QLabel(self.groupBox_17)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDesc.sizePolicy().hasHeightForWidth())
        self.lblDesc.setSizePolicy(sizePolicy)
        self.lblDesc.setObjectName(_fromUtf8("lblDesc"))
        self.gridLayout_5.addWidget(self.lblDesc, 1, 1, 1, 1)
        self.widget = QtGui.QWidget(self.groupBox_17)
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_24 = QtGui.QGridLayout(self.widget)
        self.gridLayout_24.setContentsMargins(-1, 2, -1, 5)
        self.gridLayout_24.setVerticalSpacing(8)
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.btnPDelete = QtGui.QPushButton(self.widget)
        self.btnPDelete.setMinimumSize(QtCore.QSize(25, 30))
        self.btnPDelete.setMaximumSize(QtCore.QSize(150, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/stdm/images/icons/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPDelete.setIcon(icon4)
        self.btnPDelete.setObjectName(_fromUtf8("btnPDelete"))
        self.gridLayout_24.addWidget(self.btnPDelete, 1, 4, 1, 1)
        self.btnNewP = QtGui.QPushButton(self.widget)
        self.btnNewP.setMinimumSize(QtCore.QSize(0, 30))
        self.btnNewP.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnNewP.setIcon(icon1)
        self.btnNewP.setObjectName(_fromUtf8("btnNewP"))
        self.gridLayout_24.addWidget(self.btnNewP, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 0, 2, 1, 1)
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_17)
        STDMWizard.addPage(self.wpProfile)
        self.wpEntityCustom = QtGui.QWizardPage()
        self.wpEntityCustom.setObjectName(_fromUtf8("wpEntityCustom"))
        self.gridLayout_3 = QtGui.QGridLayout(self.wpEntityCustom)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.wpEntityCustom)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lvEntities = QtGui.QListView(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lvEntities.sizePolicy().hasHeightForWidth())
        self.lvEntities.setSizePolicy(sizePolicy)
        self.lvEntities.setMinimumSize(QtCore.QSize(0, 0))
        self.lvEntities.setMaximumSize(QtCore.QSize(16777215, 180))
        self.lvEntities.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lvEntities.setObjectName(_fromUtf8("lvEntities"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.lvEntities)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.wpEntityCustom)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.btnAddColumn = QtGui.QPushButton(self.groupBox_2)
        self.btnAddColumn.setMinimumSize(QtCore.QSize(20, 20))
        self.btnAddColumn.setMaximumSize(QtCore.QSize(30, 25))
        self.btnAddColumn.setText(_fromUtf8(""))
        self.btnAddColumn.setIcon(icon1)
        self.btnAddColumn.setIconSize(QtCore.QSize(20, 20))
        self.btnAddColumn.setObjectName(_fromUtf8("btnAddColumn"))
        self.gridLayout_4.addWidget(self.btnAddColumn, 0, 0, 1, 1)
        self.btnEditColumn = QtGui.QPushButton(self.groupBox_2)
        self.btnEditColumn.setMinimumSize(QtCore.QSize(20, 20))
        self.btnEditColumn.setMaximumSize(QtCore.QSize(30, 25))
        self.btnEditColumn.setText(_fromUtf8(""))
        self.btnEditColumn.setIcon(icon2)
        self.btnEditColumn.setIconSize(QtCore.QSize(20, 20))
        self.btnEditColumn.setObjectName(_fromUtf8("btnEditColumn"))
        self.gridLayout_4.addWidget(self.btnEditColumn, 0, 1, 1, 1)
        self.btnDeleteColumn = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteColumn.sizePolicy().hasHeightForWidth())
        self.btnDeleteColumn.setSizePolicy(sizePolicy)
        self.btnDeleteColumn.setMinimumSize(QtCore.QSize(20, 20))
        self.btnDeleteColumn.setMaximumSize(QtCore.QSize(30, 25))
        self.btnDeleteColumn.setText(_fromUtf8(""))
        self.btnDeleteColumn.setIcon(icon3)
        self.btnDeleteColumn.setObjectName(_fromUtf8("btnDeleteColumn"))
        self.gridLayout_4.addWidget(self.btnDeleteColumn, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.tbvColumns = QtGui.QTableView(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tbvColumns.sizePolicy().hasHeightForWidth())
        self.tbvColumns.setSizePolicy(sizePolicy)
        self.tbvColumns.setMinimumSize(QtCore.QSize(0, 0))
        self.tbvColumns.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tbvColumns.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tbvColumns.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tbvColumns.setObjectName(_fromUtf8("tbvColumns"))
        self.tbvColumns.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.tbvColumns)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.wpEntityCustom)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnAddLookup = QtGui.QPushButton(self.groupBox_5)
        self.btnAddLookup.setMinimumSize(QtCore.QSize(10, 25))
        self.btnAddLookup.setText(_fromUtf8(""))
        self.btnAddLookup.setIcon(icon1)
        self.btnAddLookup.setObjectName(_fromUtf8("btnAddLookup"))
        self.horizontalLayout_3.addWidget(self.btnAddLookup)
        self.btnEditLookup = QtGui.QPushButton(self.groupBox_5)
        self.btnEditLookup.setMinimumSize(QtCore.QSize(20, 25))
        self.btnEditLookup.setText(_fromUtf8(""))
        self.btnEditLookup.setIcon(icon2)
        self.btnEditLookup.setObjectName(_fromUtf8("btnEditLookup"))
        self.horizontalLayout_3.addWidget(self.btnEditLookup)
        self.btnDeleteLookup = QtGui.QPushButton(self.groupBox_5)
        self.btnDeleteLookup.setMinimumSize(QtCore.QSize(20, 25))
        self.btnDeleteLookup.setText(_fromUtf8(""))
        self.btnDeleteLookup.setIcon(icon3)
        self.btnDeleteLookup.setObjectName(_fromUtf8("btnDeleteLookup"))
        self.horizontalLayout_3.addWidget(self.btnDeleteLookup)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.lvLookups = QtGui.QListView(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lvLookups.sizePolicy().hasHeightForWidth())
        self.lvLookups.setSizePolicy(sizePolicy)
        self.lvLookups.setMinimumSize(QtCore.QSize(0, 0))
        self.lvLookups.setMaximumSize(QtCore.QSize(16777215, 150))
        self.lvLookups.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lvLookups.setObjectName(_fromUtf8("lvLookups"))
        self.verticalLayout_3.addWidget(self.lvLookups)
        self.gridLayout_3.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.wpEntityCustom)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btnAddLkupValue = QtGui.QPushButton(self.groupBox_6)
        self.btnAddLkupValue.setMinimumSize(QtCore.QSize(10, 25))
        self.btnAddLkupValue.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnAddLkupValue.setText(_fromUtf8(""))
        self.btnAddLkupValue.setIcon(icon1)
        self.btnAddLkupValue.setObjectName(_fromUtf8("btnAddLkupValue"))
        self.horizontalLayout_4.addWidget(self.btnAddLkupValue)
        self.btnEditLkupValue = QtGui.QPushButton(self.groupBox_6)
        self.btnEditLkupValue.setMinimumSize(QtCore.QSize(10, 25))
        self.btnEditLkupValue.setText(_fromUtf8(""))
        self.btnEditLkupValue.setIcon(icon2)
        self.btnEditLkupValue.setObjectName(_fromUtf8("btnEditLkupValue"))
        self.horizontalLayout_4.addWidget(self.btnEditLkupValue)
        self.btnDeleteLkupValue = QtGui.QPushButton(self.groupBox_6)
        self.btnDeleteLkupValue.setMinimumSize(QtCore.QSize(10, 25))
        self.btnDeleteLkupValue.setMaximumSize(QtCore.QSize(45, 16777215))
        self.btnDeleteLkupValue.setText(_fromUtf8(""))
        self.btnDeleteLkupValue.setIcon(icon3)
        self.btnDeleteLkupValue.setObjectName(_fromUtf8("btnDeleteLkupValue"))
        self.horizontalLayout_4.addWidget(self.btnDeleteLkupValue)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.lvLookupValues = QtGui.QListView(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lvLookupValues.sizePolicy().hasHeightForWidth())
        self.lvLookupValues.setSizePolicy(sizePolicy)
        self.lvLookupValues.setMinimumSize(QtCore.QSize(0, 0))
        self.lvLookupValues.setMaximumSize(QtCore.QSize(16777215, 150))
        self.lvLookupValues.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lvLookupValues.setObjectName(_fromUtf8("lvLookupValues"))
        self.verticalLayout_4.addWidget(self.lvLookupValues)
        self.gridLayout_3.addWidget(self.groupBox_6, 1, 1, 1, 1)
        STDMWizard.addPage(self.wpEntityCustom)
        self.wpSTR = QtGui.QWizardPage()
        self.wpSTR.setObjectName(_fromUtf8("wpSTR"))
        self.formLayout_9 = QtGui.QFormLayout(self.wpSTR)
        self.formLayout_9.setObjectName(_fromUtf8("formLayout_9"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(80, 50, -1, 5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.wpSTR)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.cboParty = QtGui.QComboBox(self.wpSTR)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboParty.sizePolicy().hasHeightForWidth())
        self.cboParty.setSizePolicy(sizePolicy)
        self.cboParty.setMinimumSize(QtCore.QSize(0, 30))
        self.cboParty.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cboParty.setObjectName(_fromUtf8("cboParty"))
        self.verticalLayout.addWidget(self.cboParty)
        self.cbMultiParty = QtGui.QCheckBox(self.wpSTR)
        self.cbMultiParty.setObjectName(_fromUtf8("cbMultiParty"))
        self.verticalLayout.addWidget(self.cbMultiParty)
        self.formLayout_9.setLayout(0, QtGui.QFormLayout.FieldRole, self.verticalLayout)
        self.lblPartyDesc = QtGui.QLabel(self.wpSTR)
        self.lblPartyDesc.setText(_fromUtf8(""))
        self.lblPartyDesc.setObjectName(_fromUtf8("lblPartyDesc"))
        self.formLayout_9.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lblPartyDesc)
        self.lblSpDesc = QtGui.QLabel(self.wpSTR)
        self.lblSpDesc.setText(_fromUtf8(""))
        self.lblSpDesc.setObjectName(_fromUtf8("lblSpDesc"))
        self.formLayout_9.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblSpDesc)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(80, 50, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(self.wpSTR)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.cboSPUnit = QtGui.QComboBox(self.wpSTR)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboSPUnit.sizePolicy().hasHeightForWidth())
        self.cboSPUnit.setSizePolicy(sizePolicy)
        self.cboSPUnit.setMinimumSize(QtCore.QSize(0, 30))
        self.cboSPUnit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cboSPUnit.setObjectName(_fromUtf8("cboSPUnit"))
        self.verticalLayout_2.addWidget(self.cboSPUnit)
        self.formLayout_9.setLayout(2, QtGui.QFormLayout.FieldRole, self.verticalLayout_2)
        STDMWizard.addPage(self.wpSTR)
        self.wpSaveProfile = QtGui.QWizardPage()
        self.wpSaveProfile.setObjectName(_fromUtf8("wpSaveProfile"))
        self.formLayout_10 = QtGui.QFormLayout(self.wpSaveProfile)
        self.formLayout_10.setObjectName(_fromUtf8("formLayout_10"))
        self.label_2 = QtGui.QLabel(self.wpSaveProfile)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_10.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtHtml = QtGui.QTextEdit(self.wpSaveProfile)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.txtHtml.sizePolicy().hasHeightForWidth())
        self.txtHtml.setSizePolicy(sizePolicy)
        self.txtHtml.setReadOnly(True)
        self.txtHtml.setObjectName(_fromUtf8("txtHtml"))
        self.formLayout_10.setWidget(1, QtGui.QFormLayout.SpanningRole, self.txtHtml)
        STDMWizard.addPage(self.wpSaveProfile)

        self.retranslateUi(STDMWizard)
        QtCore.QMetaObject.connectSlotsByName(STDMWizard)
        STDMWizard.setTabOrder(self.rbAccpt, self.cboProfile)
        STDMWizard.setTabOrder(self.cboProfile, self.rbReject)
        STDMWizard.setTabOrder(self.rbReject, self.btnPDelete)
        STDMWizard.setTabOrder(self.btnPDelete, self.btnNewP)
        STDMWizard.setTabOrder(self.btnNewP, self.pftableView)
        STDMWizard.setTabOrder(self.pftableView, self.btnNewEntity)
        STDMWizard.setTabOrder(self.btnNewEntity, self.btnEditEntity)
        STDMWizard.setTabOrder(self.btnEditEntity, self.btnDeleteEntity)
        STDMWizard.setTabOrder(self.btnDeleteEntity, self.btnDeleteColumn)
        STDMWizard.setTabOrder(self.btnDeleteColumn, self.btnEditColumn)
        STDMWizard.setTabOrder(self.btnEditColumn, self.btnAddColumn)
        STDMWizard.setTabOrder(self.btnAddColumn, self.tbvColumns)
        STDMWizard.setTabOrder(self.tbvColumns, self.lvLookups)
        STDMWizard.setTabOrder(self.lvLookups, self.btnEditLookup)
        STDMWizard.setTabOrder(self.btnEditLookup, self.btnDeleteLookup)
        STDMWizard.setTabOrder(self.btnDeleteLookup, self.btnAddLookup)
        STDMWizard.setTabOrder(self.btnAddLookup, self.lvLookupValues)
        STDMWizard.setTabOrder(self.lvLookupValues, self.btnDeleteLkupValue)
        STDMWizard.setTabOrder(self.btnDeleteLkupValue, self.btnEditLkupValue)
        STDMWizard.setTabOrder(self.btnEditLkupValue, self.btnAddLkupValue)
        STDMWizard.setTabOrder(self.btnAddLkupValue, self.cboParty)
        STDMWizard.setTabOrder(self.cboParty, self.cboSPUnit)
        STDMWizard.setTabOrder(self.cboSPUnit, self.txtLicense)

    def retranslateUi(self, STDMWizard):
        STDMWizard.setWindowTitle(_translate("STDMWizard", "Configuration Wizard", None))
        self.wpLicense.setTitle(_translate("STDMWizard", "End User License Agreement", None))
        self.wpLicense.setSubTitle(_translate("STDMWizard", "Read carefully before you proceed", None))
        self.groupBox_16.setTitle(_translate("STDMWizard", "Terms and Conditions", None))
        self.rbAccpt.setText(_translate("STDMWizard", "I Agree", None))
        self.rbReject.setText(_translate("STDMWizard", "Decline", None))
        self.wpPathSetting.setTitle(_translate("STDMWizard", "Directory Settings", None))
        self.wpPathSetting.setSubTitle(_translate("STDMWizard", "Specify configuration and documents directory path", None))
        self.btnTemplates.setText(_translate("STDMWizard", "Change", None))
        self.btnDocOutput.setText(_translate("STDMWizard", "Change", None))
        self.edtTemplatePath.setPlaceholderText(_translate("STDMWizard", "Specify path to save document templates", None))
        self.label_37.setText(_translate("STDMWizard", "<html><head/><body><p>Supporting documents path</p></body></html>", None))
        self.label_4.setText(_translate("STDMWizard", "Documents template path", None))
        self.label_31.setText(_translate("STDMWizard", "Documents output path", None))
        self.edtOutputPath.setPlaceholderText(_translate("STDMWizard", "Specify path to save generated documents", None))
        self.btnDocPath.setText(_translate("STDMWizard", "Change", None))
        self.edtDocPath.setPlaceholderText(_translate("STDMWizard", "Specify path to save entity supporting documents", None))
        self.wpProfile.setTitle(_translate("STDMWizard", "Profile", None))
        self.wpProfile.setSubTitle(_translate("STDMWizard", "Manage profile and related entities.  A profile represents a collection of logically related entities, some of which represent the party and spatial unit. Examples of profiles include individual, household, neighbourhood or even city-wide profiles.   ", None))
        self.groupBox_18.setTitle(_translate("STDMWizard", "Profile entities ", None))
        self.groupBox_17.setTitle(_translate("STDMWizard", "Profile", None))
        self.label_3.setText(_translate("STDMWizard", "Description", None))
        self.label.setText(_translate("STDMWizard", "Select", None))
        self.lblDesc.setText(_translate("STDMWizard", "TextLabel", None))
        self.btnPDelete.setText(_translate("STDMWizard", "Delete profile", None))
        self.btnNewP.setText(_translate("STDMWizard", "New profile", None))
        self.wpEntityCustom.setTitle(_translate("STDMWizard", "Entity Customization", None))
        self.wpEntityCustom.setSubTitle(_translate("STDMWizard", "Add or edit entity columns, lookups and lookup values", None))
        self.groupBox.setTitle(_translate("STDMWizard", "Entities", None))
        self.groupBox_2.setTitle(_translate("STDMWizard", "Columns", None))
        self.groupBox_5.setTitle(_translate("STDMWizard", "Lookups", None))
        self.groupBox_6.setTitle(_translate("STDMWizard", "Values", None))
        self.wpSTR.setTitle(_translate("STDMWizard", "Defining Social Tenure Tables", None))
        self.wpSTR.setSubTitle(_translate("STDMWizard", "Define entities to participate in Social Tenure Relations views", None))
        self.label_5.setText(_translate("STDMWizard", "Party entity in the STR definition", None))
        self.cbMultiParty.setText(_translate("STDMWizard", "Allow party to be linked to multiple spatial unit in social tenure relationship", None))
        self.label_6.setText(_translate("STDMWizard", "Spatial unit entity in the STR definition", None))
        self.wpSaveProfile.setTitle(_translate("STDMWizard", "Save configuration", None))
        self.wpSaveProfile.setSubTitle(_translate("STDMWizard", "Click finish to save changes in your configuration to the database.  ", None))
        self.label_2.setText(_translate("STDMWizard", "Save status will be displayed in the window below.", None))

