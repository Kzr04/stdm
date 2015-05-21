from PyQt4.QtCore import *
from PyQt4.QtGui import *

from stdm.data import (geometryType, STDMDb)

from stdm.data.importexport import OGRReader

from ui_gpx_add_attribute_info import Ui_Dialog

import sqlalchemy
from sqlalchemy.schema import (
                               Table,
                               MetaData
                               )
from sqlalchemy.orm import (
                            mapper,
                            class_mapper
                            )


class _ReflectedModel(object):
    """
    Placeholder model for the reflected database table.
    """
    pass

class GPXAttributeInfoDialog(QDialog, Ui_Dialog):

    def __init__(self, iface, non_spatial_columns, sp_table, sp_table_colmn, geom_column_value):
        QDialog.__init__(self, iface.mainWindow())
        self.setupUi(self)
        self._dbSession = STDMDb.instance().session
        self.non_sp_colmns = non_spatial_columns
        self.sp_table = sp_table
        self.sp_table_colmn = sp_table_colmn
        self.geom_column_value = geom_column_value
        self.attribute_dict = {}
        self.geom_type = None
        self.target_geom_col_srid = None
        self.data_reader = None
        self._mapped_class = None

    def _insert_row(self, column_value_mapping):
        """
        Insert a new row using the mapped class instance then mapping column names to the corresponding column values.
        """
        model_instance = self._mapped_class()

        for col, value in column_value_mapping.iteritems():
            if hasattr(model_instance,col):

                setattr(model_instance,col,value)
        #raise NameError(str(dir(modelInstance)))
        try:
            self._dbSession.add(model_instance)
            self._dbSession.commit()
        except Exception as ex:
            raise
        finally:
            self._dbSession.rollback()

    def _map_table(self, dataSourceName):
        """
        Reflect the data source.
        """
        meta = MetaData(bind = STDMDb.instance().engine)
        dsTable = Table(dataSourceName,meta,autoload = True)

        return dsTable

    def create_attribute_info_gui(self):

        self.geom_type, self.target_geom_col_srid = geometryType(self.sp_table, self.sp_table_colmn)

        self.attribute_dict[self.sp_table_colmn] = "SRID={0!s};{1}".format(self.target_geom_col_srid,
                                                                           self.geom_column_value)
        grid_column_count = 0

        for column in self.non_sp_colmns:

            label_name = "label_{0}".format(column)
            line_edit_name = "line_edit_name_{0}".format(column)

            self.label = QLabel()
            self.label.setObjectName(label_name)
            self.label.setText(column)
            self.gridLayout.addWidget(self.label, grid_column_count, 0, 1, 1)

            self.lineEdit = QLineEdit()
            self.lineEdit.setObjectName(line_edit_name)
            self.lineEdit.setPlaceholderText("NULL")
            self.gridLayout.addWidget(self.lineEdit, grid_column_count, 1, 1, 1)

            grid_column_count += 1

            self.attribute_dict[self.label.text()] = self.lineEdit.text()

    def accept(self):
        if self._mapped_class == None:

            try:
                primaryMapper = class_mapper(_ReflectedModel)

            except (sqlalchemy.orm.exc.UnmappedClassError,sqlalchemy.exc.ArgumentError):
                #Reflect table and map it to '_ReflectedModel' class only once
                mapper(_ReflectedModel,self._map_table(self.sp_table))

            self._mapped_class = _ReflectedModel

            self._insert_row(self.attribute_dict)
