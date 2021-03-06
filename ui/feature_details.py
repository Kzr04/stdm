# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : Feature Details Viewer
Description          : GUI widget for viewing details of a feature on
                        the map canvas.
Date                 : 10/October/2016
copyright            : (C) 2016 by UN-Habitat and implementing partners.
                       See the accompanying file CONTRIBUTORS.txt in the root
email                : stdm@unhabitat.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import re
from collections import OrderedDict

from PyQt4.QtCore import Qt, QDateTime, QDate
from PyQt4.QtGui import (
    QDockWidget,
    QMessageBox,
    QTreeView,
    QStandardItem,
    QAbstractItemView,
    QStandardItemModel,
    QIcon,
    QApplication,
    QColor
)

from qgis.gui import (
    QgsHighlight
)
from qgis.core import (
    QgsFeatureRequest,
    QgsExpression,
    QgsMapLayer,
    NULL
)

from stdm.settings import current_profile

from stdm.settings.registryconfig import (
    selection_color
)

from stdm.data.configuration import (
    entity_model
)
from stdm.data.pg_utils import (
    spatial_tables,
    pg_views
)

from stdm.data.supporting_documents import (
    supporting_doc_tables,
    document_models
)
from stdm.ui.forms.editor_dialog import EntityEditorDialog

from stdm.ui.forms.widgets import ColumnWidgetRegistry
from stdm.utils.util import (
    format_name,
    entity_id_to_model,
    profile_spatial_tables
)

from stdm.ui.social_tenure.str_editor import EditSTREditor

from ui_feature_details import Ui_DetailsDock


class LayerSelectionHandler(object):
    """
     Handles all tasks related to the layer.
    """
    def __init__(self, iface):
        """
        Initializes the LayerSelectionHandler.
        :param iface: The QGIS Interface object
        :type iface: Object
        :param plugin: The STDM plugin object
        :type plugin: Object
        """
        self.layer = None
        self.iface = iface
        self.sel_highlight = None
        self.current_profile = current_profile()

    def selected_features(self):
        """
        Returns a selected feature spatial unit
        id and code as key and value.
        :return: Dictionary
        """
        if self.layer is None:
            return None
        if self.stdm_layer(self.layer):
            selected_features = self.layer.selectedFeatures()
            features = []
            field_names = [
                field.name()
                for field in self.layer.pendingFields()]
            for feature in selected_features:
                if 'id' in field_names:
                    features.append(feature['id'])
            if len(features) > 40:
                max_error = QApplication.translate(
                    'LayerSelectionHandler',
                    'You have exceeded the maximum number of features that \n'
                    'can be selected and queried by Spatial Entity Details. \n'
                    'Please select a maximum of 40 features.'
                )

                QMessageBox.warning(
                    self.iface.mainWindow(),
                    QApplication.translate(
                        'LayerSelectionHandler', 'Maximum Features Error'
                    ),
                    max_error
                )
                return None
            return features
        else:
            return None

    def non_stdm_layer_error(self):
        """
        Shows an error if the layer is not an STDM entity layer.
        """
        not_feature_msg = QApplication.translate(
            'LayerSelectionHandler',
            'You have selected a non-STDM layer. \n'
            'Please select an STDM layer to view \n'
            'the details.'
        )

        QMessageBox.warning(
            self.iface.mainWindow(),
            QApplication.translate(
                'LayerSelectionHandler', 'Invalid Layer Error'
            ),
            not_feature_msg
        )

    def get_layer_source(self, layer):
        """
        Get the layer table name if the source is from the database.
        :param layer: The layer for which the source is checked
        :type layer: QgsVectorLayer
        :return: The table name or none if no table name found.
        :rtype: String or None
        """
        if layer is None:
            return None
        source = layer.source()
        if source is None:
            return
        vals = dict(re.findall('(\S+)="?(.*?)"? ', source))
        try:
            table = vals['table'].split('.')

            table_name = table[1].strip('"')
            if table_name in pg_views():
                return table_name

            entity_table = self.current_profile.entity_by_name(table_name)
            if entity_table is None:
                return None
            return table_name
        except KeyError:
            return None

    def active_layer_check(self):
        """
        Check if there is active layer and if not, displays
        a message box to select a feature layer.
        """
        active_layer = self.iface.activeLayer()
        if active_layer is None:
            no_layer_msg = QApplication.translate(
                'LayerSelectionHandler',
                'Please select a spatial entity '
                'layer to view feature details.'
            )
            QMessageBox.critical(
                self.iface.mainWindow(),
                QApplication.translate(
                    'LayerSelectionHandler', 'Layer Error'
                ),
                no_layer_msg
            )

    def stdm_layer(self, active_layer):
        """
        Check whether the layer is feature layer or not.
        :param active_layer: The layer to be checked
        :type active_layer: QGIS VectorLayer
        :return: True if the active layer is STDM layer or False if it is not.
        :rtype: Boolean
        """
        layer_source = self.get_layer_source(active_layer)
        
        if layer_source is not None:
            return True
        else:
            return False

    def clear_feature_selection(self):
        """
        Clears selection of layer(s).
        """
        map = self.iface.mapCanvas()
        for layer in map.layers():
            if layer.type() == layer.VectorLayer:
                layer.removeSelection()
        map.refresh()

    def activate_select_tool(self):
        """
        Enables the select tool to be used to select features.
        """
        self.iface.actionSelect().trigger()
        layer_select_tool = self.iface.mapCanvas().mapTool()
        layer_select_tool.activate()

    def clear_sel_highlight(self):
        """
        Removes sel_highlight from the canvas.
        """
        if self.sel_highlight is not None:
            self.sel_highlight = None

    def refresh_layers(self):
        """
        Refresh all database layers.
        """
        layers = self.iface.legendInterface().layers()
        for layer in layers:
            layer.dataProvider().forceReload()
            layer.triggerRepaint()
        if not self.iface.activeLayer() is None:
            canvas = self.iface.mapCanvas()
            canvas.setExtent(
                self.iface.activeLayer().extent()
            )
            self.iface.mapCanvas().refresh()

    def multi_select_highlight(self, index):
        """
        Highlights a feature with rubberBald
        class when selecting
        features are more than one.
        :param index: Selected QTreeView item index
        :type index: Integer
        """
        pass

class DetailsDBHandler:
    """
    Handles the database linkage of the spatial entity details.
    """
    def __init__(self):
        """
        Initializes the DetailsDBHandler.
        """
        self._entity = None
        self.column_formatter = OrderedDict()
        self.formatted_columns = OrderedDict()
        self.current_profile = current_profile()
        self._formatted_record = OrderedDict()
        self.display_columns = None
        self._entity_supporting_doc_tables = {}

    def set_entity(self, entity):
        """
        Sets the spatial entity.
        :param entity: The entity object
        :type entity: Object
        """
        self._entity = entity

    def set_formatter(self, entity=None):
        """
        Sets the column widget formatter.
        :param entity: The entity for which the columns are to be formatted.
        :type entity: Object
        """
        self.format_columns(entity)

    def format_columns(self, entity=None):
        """
        Formats the columns using the ColumnWidgetRegistry factory method.
        :param entity: The entity of the columns to be formatted.
        :type entity: Object
        """
        if entity is None:
            entity = self._entity
        if entity is None:
            return
        for col in entity.columns.values():
            col_name = col.name

            # Get widget factory so that we can use the value formatter
            widget_factory = ColumnWidgetRegistry.factory(
                col.TYPE_INFO
            )
            if not widget_factory is None:
                formatter = widget_factory(col)
                self.column_formatter[col_name] = formatter

    def display_column_object(self, entity):
        """
        Returns entity display columns.
        :param entity: Entity
        :type entity: Class
        :return: List of column names.
        :rtype: List
        """
        self.display_columns = [
            c
            for c in
            entity.columns.values()
            if c.TYPE_INFO in [
                'VARCHAR',
                'TEXT',
                'INT',
                'DOUBLE',
                'DATE',
                'DATETIME',
                'BOOL',
                'LOOKUP',
                'ADMIN_SPATIAL_UNIT',
                'PERCENT',
                'AUTO_GENERATED'
            ]
        ]

    def feature_model(self, entity, id):
        """
        Gets the model of an entity based on an id and the entity.
        :param entity: Entity
        :type entity: Object
        :param id: Id of the record
        :type id: Integer
        :return: SQLAlchemy result proxy
        :rtype: Object
        """
        model = entity_model(entity)
        model_obj = model()
        result = model_obj.queryObject().filter(
            model.id == id
        ).all()
        if len(result) > 0:
            return result[0]
        else:
            return None

    def feature_str_link(self, feature_id):
        """
        Gets all STR records linked to a feature, if the layer is a
        spatial unit layer.
        :param feature_id: The feature id/id of the spatial unit
        :type feature_id: Integer
        :return: The list of social tenure records
        :rtype: List
        """
        str_model = entity_model(
            self.current_profile.social_tenure
        )
        model_obj = str_model()
        result = model_obj.queryObject().filter(
            str_model.spatial_unit_id == feature_id
        ).all()

        return result

    def column_widget_registry(self, model, entity):
        """
        Registers the column widgets using the model and the entity.
        :param model: The model of the entity
        :type model: SQLAlchemy model
        :param entity: The entity object
        :type entity: Object
        """
        self._formatted_record.clear()

        self.display_column_object(entity)
        for col in self.display_columns:
            if isinstance(model, OrderedDict):
                col_val = model[col.name]
            else:
                col_val = getattr(model, col.name)
            # Check if there are display formatters and apply if
            # one exists for the given attribute.
            if col_val == NULL:
                col_val = None
            if col.name in self.column_formatter:
                formatter = self.column_formatter[col.name]

                col_val = formatter.format_column_value(col_val)
            if col.header() == QApplication.translate(
                    'DetailsDBHandler', 'Tenure Share'
            ):
                share = '{} (%)'.format(col.header())
                self._formatted_record[share] = col_val
            else:
                self._formatted_record[col.header()] = col_val

    def _supporting_doc_models(self, entity_table, model_obj):
        """
        Creates supporting document models using information from the
        entity table and values in the model object.
        :param entity_table: Name of the entity table.
        :type entity_table: str
        :param model_obj: Model instance.
        :type model_obj: object
        :return: Supporting document models.
        :rtype: list
        """
        #Only one document table per entity for now
        if entity_table in self._entity_supporting_doc_tables:
            doc_table_ref = self._entity_supporting_doc_tables[entity_table]
        else:
            doc_tables = supporting_doc_tables(entity_table)

            if len(doc_tables) > 0:
                doc_table_ref = doc_tables[0]
                self._entity_supporting_doc_tables[entity_table] = doc_table_ref

            else:
                return []

        doc_link_col, doc_link_table = doc_table_ref[0], doc_table_ref[1]

        if not hasattr(model_obj, 'id'):
            return []

        return document_models(
            self.current_profile.social_tenure,
            doc_link_col,
            model_obj.id
        )

class DetailsDockWidget(QDockWidget, Ui_DetailsDock, LayerSelectionHandler):
    """
    The logic for the spatial entity details dock widget.
    """
    def __init__(self, iface, plugin):
        """
        Initializes the DetailsDockWidget.
        :param iface: The QGIS interface
        :type iface: Object
        :param plugin: The STDM plugin object
        :type plugin: Object
        """
        QDockWidget.__init__(self, iface.mainWindow())
        self.setupUi(self)
        self.plugin = plugin
        self.iface = iface
        self.edit_btn.setDisabled(True)
        self.delete_btn.setDisabled(True)
        self.view_document_btn.setDisabled(True)
        LayerSelectionHandler.__init__(self, iface)
        self.setBaseSize(300,5000)

    def init_dock(self):
        """
        Creates dock on right dock widget area and set window title.
        """
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self)

        self.setWindowTitle(
            QApplication.translate(
                'DetailsDockWidget', 'Spatial Entity Details'
            )
        )

    def close_dock(self, tool):
        """
        Closes the dock by replacing select tool with pan tool,
        clearing feature selection, and hiding the dock.
        :param tool: Feature detail tool button
        :type tool: QAction
        """
        self.iface.actionPan().trigger()
        tool.setChecked(False)
        self.clear_feature_selection()
        self.clear_sel_highlight()
        self.hide()

    def closeEvent(self, event):
        """
        On close of the dock window, this event is executed
        to run close_dock method
        :param event: The close event
        :type event: QCloseEvent
        :return: None
        """
        self.close_dock(
            self.plugin.feature_details_act
        )

    def hideEvent(self, event):
        """
        Listens to the hide event of the dock and properly close the dock
        using the close_dock method.
        :param event: The close event
        :type event: QCloseEvent
        """
        self.close_dock(
            self.plugin.feature_details_act
        )

class DetailsTreeView(DetailsDBHandler, DetailsDockWidget):
    """
    Avails the treeview dock widget. This class must be called
    to add the widget.
    """
    def __init__(self, iface, plugin):
        """
        The method initializes the dockwidget.
        :param iface: QGIS user interface class
        :type iface: Object
        :param plugin: The STDM plugin
        :type plugin: class
        """
        from stdm.ui.entity_browser import _EntityDocumentViewerHandler
        DetailsDockWidget.__init__(self, iface, plugin)

        DetailsDBHandler.__init__(self)

        self.plugin = plugin

        self.view = QTreeView()
        self.view.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.layer_table = None
        self.entity = None
        self.feature_models = {}
        self.party_models = {}
        self.str_models = {}
        self.feature_str_model = {}
        self.removed_feature = None
        self.selected_root = None
        self.party_items = {}

        self.model = QStandardItemModel()
        self.view.setModel(self.model)
        self.view.setUniformRowHeights(True)
        self.view.setRootIsDecorated(True)
        self.view.setAlternatingRowColors(True)
        self.view.setWordWrap(True)
        self.view.setHeaderHidden(True)
        self.view.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.str_text = QApplication.translate(
            'DetailsTreeView',
            'Social Tenure Relationship'
        )
        self.view.setStyleSheet(
            '''
            QTreeView:!active {
                selection-background-color: #72a6d9;
            }
            '''
        )
        self.current_profile = current_profile()
        if self.current_profile is None:
            return
        self.social_tenure = self.current_profile.social_tenure
        self.spatial_unit = self.social_tenure.spatial_unit

        self.view.setMinimumWidth(250)
        self.doc_viewer_title = QApplication.translate(
            'DetailsTreeView',
            'Document Viewer'
        )
        self.doc_viewer = _EntityDocumentViewerHandler(
            self.doc_viewer_title, self.iface.mainWindow()
        )
        self.view_selection = self.view.selectionModel()

        self.view_selection.currentChanged.connect(
            self.on_tree_view_item_clicked
        )

    def on_tree_view_item_clicked(self, current, previous):
        """
        Disables the delete button if the party node is clicked and enable it
        if other items are clicked.
        :param current: The newly clicked item index
        :type current: QModelIndex
        :param previous: The previous item index
        :type previous: QModelIndex
        """
        selected_item = self.model.itemFromIndex(current)
        if selected_item is None:
            return
        if selected_item in self.party_items.keys():
            self.delete_btn.setEnabled(False)
        else:
            self.delete_btn.setEnabled(True)

    def set_layer_entity(self):
        """
        Sets the entity property using the layer table.
        """
        self.layer_table = self.get_layer_source(
            self.iface.activeLayer()
        )
        if self.layer_table is None:
            return

        if self.layer_table in spatial_tables() and \
                        self.layer_table not in pg_views():
            self.entity = self.current_profile.entity_by_name(
                self.layer_table
            )

    def activate_feature_details(self, button_clicked=True):
        """
        A slot raised when the feature details button is clicked.
        :param button_clicked: A boolean to identify if it is activated
        because of button click or because of change in the active layer.
        :type button_clicked: Boolean
        """
        # Get and set the active layer.
        self.layer = self.iface.activeLayer()
        # if no active layer, show error message
        # and uncheck the feature tool
        if self.layer is None:
            if button_clicked:
                self.active_layer_check()
            self.plugin.feature_details_act.setChecked(False)
            return
        # If the button is unchecked, close dock.
        if not self.plugin.feature_details_act.isChecked():
            self.close_dock(self.plugin.feature_details_act)
            self.feature_details = None
            return
        # if the selected layer is not an STDM layer,
        # show not feature layer.
        if not self.stdm_layer(self.layer):
            if button_clicked and self.isHidden():
                # show popup message if dock is hidden and button clicked
                self.non_stdm_layer_error()
                self.plugin.feature_details_act.setChecked(False)
            elif not button_clicked and not self.isHidden():
                # show tree message if dock is open and button clicked
                not_feature_msg = QApplication.translate(
                    'FeatureDetails',
                    'Please select an STDM layer to view \n'
                    'the details.'
                )
                self.model.clear()
                self.treeview_error(not_feature_msg)
        # If the selected layer is feature layer, get data and
        # display treeview in a dock widget
        else:
            self.prepare_for_selection()

    def prepare_for_selection(self):
        """
        Prepares the dock widget for data loading.
        """
        select_feature = 'Please select a feature ' \
                         'to view their details.'
        self.init_dock()
        self.add_tree_view()
        self.model.clear()
        self.treeview_error(select_feature)
        # enable the select tool
        self.activate_select_tool()
        self.update_tree_source(self.layer)

    def update_tree_source(self, active_layer):
        """
        Updates the treeview source in case of layer change.
        :param active_layer: The active layer on the canvas.
        :type active_layer: QgsVectorLayer
        """
        if active_layer.type() != QgsMapLayer.VectorLayer:
            return
        # set entity from active layer in the child class
        self.set_layer_entity()
        # set entity for the super class DetailModel
        self.set_entity(self.entity)
        # Registry column widget
        self.set_formatter()
        # set formatter for social tenure relationship.
        self.set_formatter(self.social_tenure)
        for party in self.social_tenure.parties:
            self.set_formatter(party)
        # pull data, show treeview
        active_layer.selectionChanged.connect(
            self.show_tree
        )
        self.steam_signals(self.entity)

    def add_tree_view(self):
        """
        Adds tree view to the dock widget and sets style.
        """
        self.tree_scrollArea.setWidget(self.view)

    def reset_tree_view(self, features=None):
        """
        Resets the treeview by clearing feature highlights,
        disabling edit, delete, and view document buttons,
        and adding an empty treeview if a feature is selected.
        """
        #clear feature_ids list, model and highlight
        self.model.clear()

        self.clear_sel_highlight() # remove sel_highlight
        self.disable_buttons(False)
        if self.removed_feature is None:
            self.str_models.clear()
            self.feature_models.clear()
            self.party_items.clear()
        else:
            self.removed_feature = None

        # if the selected feature is over 1,
        # activate multi_select_highlight
        if features is not None:
            self.view.clicked.connect(
                self.multi_select_highlight
            )
        if features is None:
            return
        # if there is at least one selected feature
        if len(features) > 0:
            self.add_tree_view()

    def disable_buttons(self, bool):
        """
        Disables or enables the edit, delete, and view document buttons on
        the dock widget.
        :param bool: A boolean setting the disabled status. True disables it.
        :type bool: Boolean
        """
        self.edit_btn.setDisabled(bool)
        self.delete_btn.setDisabled(bool)
        self.view_document_btn.setDisabled(bool)

    def show_tree(self):
        """
        Shows the treeview.
        """
        selected_features = self.selected_features()
        if selected_features is None:
            self.reset_tree_view()

            not_supported = QApplication.translate(
                'DetailsTreeView',
                'Spatial Entity Details is not supported for this layer.'
            )
            self.treeview_error(not_supported)
            return

        if len(selected_features) < 1:
            self.reset_tree_view(selected_features)
            self.disable_buttons(True)
            return
        layer_icon = QIcon(':/plugins/stdm/images/icons/layer.gif')
        ### add non entity layer for views.
        if not self.entity is None:
            self.reset_tree_view(selected_features)
            roots = self.add_parent_tree(
                layer_icon, format_name(self.entity.short_name)
            )
            if roots is None:
                return
            for id, root in roots.iteritems():
                str_records = self.feature_str_link(id)
                if len(str_records) > 0:
                    db_model = getattr(str_records[0], self.entity.name)

                else:
                    data = self.features_data(id)
                    if len(self.features_data(id)) > 0:
                        db_model = data[0]
                    else:
                        db_model = self.feature_model(self.entity, id)

                self.add_root_children(db_model, root, str_records)

        else:
            self.reset_tree_view(selected_features)
            self.disable_buttons(True)
            self.add_non_entity_parent(layer_icon)

    def add_non_entity_parent(self, layer_icon):
        """
        Adds details of layers that are view based.
        :param layer_icon: The icon of the tree node.
        :type layer_icon: QIcon
        """
        for feature_map in self.features_data():
            parent = QStandardItem(
                layer_icon,
                format_name(self.layer.name())
            )
            for k, v, in feature_map.iteritems():
                if isinstance(v, QDate):
                    v = v.toPyDate()
                if isinstance(v, QDateTime):
                    v = v.toPyDateTime()
                if k != 'id':
                    child = QStandardItem('{}: {}'.format(
                        format_name(k, False), v)
                    )
                    child.setSelectable(False)
                    parent.appendRow([child])
            self.model.appendRow(parent)
            self.set_bold(parent)
            self.expand_node(parent)

    def features_data(self, feature_id=None):
        """
        Gets data column and value of a feature from
        the selected layer and features.
        :param feature_id: The feature id
        :type feature_id: Integer
        :return: List of feature data with column and value
        :rtype: List
        """
        selected_features = self.layer.selectedFeatures()
        field_names = [field.name() for field in self.layer.pendingFields()]
        feature_data = []

        for elem in selected_features:
            if not feature_id is None:
                if elem.id() == feature_id:
                    feature_map = OrderedDict(
                        zip(field_names, elem.attributes())
                    )
                    feature_data.append(feature_map)
                    break
            else:
                feature_map = OrderedDict(
                    zip(field_names, elem.attributes())
                )
                feature_data.append(feature_map)
        return feature_data

    def add_parent_tree(self, icon, title):
            """
            Adds the top root of the treeview into the model.
            :param icon: The icon of the item
            :type icon: QIcon
            :param title: The title of the item
            :type title: String
            :return: The root QStandardItem with the feature id
            :rtype: OrderedDict
            """
            roots = OrderedDict()
            selected_features = self.selected_features()
            if selected_features is None:
                return None
            for feature_id in selected_features:
                root = QStandardItem(icon, title)
                root.setData(feature_id)
                self.set_bold(root)
                self.model.appendRow(root)
                roots[feature_id] = root
            return roots

    def add_root_children(self, model, parent, str_records):
        """
        Adds the root children.
        :param model: The entity model
        :type model: SQL Alchemy model
        :param parent: The root of the children
        :type parent: QStandardItem
        :param str_records: STR record models linked to the spatial unit.
        :type str_records: List
        """

        if model is None:
            return
        if isinstance(model, OrderedDict):
            feature_id = model['id']
        else:
            feature_id = model.id
        self.feature_models[feature_id] = model

        self.column_widget_registry(model, self.entity)
        for i, (col, row) in enumerate(self._formatted_record.iteritems()):
            child = QStandardItem('{}: {}'.format(col, row))
            child.setSelectable(False)
            try:
                parent.appendRow([child])
            except RuntimeError:
                pass
            # Add Social Tenure Relationship steam as a last child
            if i == len(self._formatted_record) - 1:
                if len(str_records) > 0:
                    self.add_str_child(parent, str_records, feature_id)
                else:
                    self.add_no_str_steam(parent)
        self.expand_node(parent)

    def add_str_steam(self, parent, str_id):
        """
        Adds the STR parent into the treeview.
        :param parent: The parent of the STR item, which is the
         child of the root.
        :type parent: QStandardItem
        :param str_id: The id of the STR record
        :type str_id: Integer
        :return: The STR root item
        :rtype: QStandardItem
        """
        str_icon = QIcon(
            ':/plugins/stdm/images/icons/social_tenure.png'
        )

        str_root = QStandardItem(str_icon, self.str_text)
        str_root.setData(str_id)
        self.set_bold(str_root)
        try:
            parent.appendRow([str_root])
        except RuntimeError:
            pass
        return str_root

    def add_no_str_steam(self, parent):
        """
        Adds NO STR Defined steam.
        :param parent: The root node.
        :type parent: QStandardItem
        """
        if self.entity.name == self.spatial_unit.name:
            no_str_icon = QIcon(
                ':/plugins/stdm/images/icons/remove.png'
            )
            title = 'No STR Defined'
            no_str_root = QStandardItem(no_str_icon, title)
            self.set_bold(no_str_root)
            parent.appendRow([no_str_root])

    def current_party(self, record):
        """
        Gets the current party column name in STR
        table by finding party column with value
        other than None.
        :param record: The STR record or result.
        :type record: Dictionary
        :return: The party column name with value.
        :rtype: String
        """
        parties = self.social_tenure.parties

        for party in parties:
            party_name = party.short_name.lower()
            party_id = '{}_id'.format(party_name)
            if not party_id in record:
                return None, None
            if record[party_id] != None:
                return party, party_id

    def add_str_child(self, parent, str_records, feature_id):
        """
        Adds STR children into the treeview.
        :param parent: The root node.
        :type parent: QStandardItem
        :param str_records: STR record models linked to the spatial unit.
        :type str_records: List
        :param feature_id: The selected feature id.
        :type feature_id: Integer
        """
        if self.layer_table is None:
            return
        # If the layer table is not spatial unit table, don't show STR node.
        if self.layer_table != self.spatial_unit.name:
            return
        if str_records is None:
            return
        for record in str_records:
            self.str_models[record.id] = record
            str_root = self.add_str_steam(parent, record.id)
            # add STR children
            self.column_widget_registry(record, self.social_tenure)

            for i, (col, row) in enumerate(self._formatted_record.iteritems()):
                str_child = QStandardItem(
                    '{}: {}'.format(col, row)
                )
                str_child.setSelectable(False)
                try:
                    str_root.appendRow([str_child])
                except RuntimeError:
                    pass
                record_dict = record.__dict__
                party, party_id = self.current_party(record_dict)
                party_model = getattr(record, party.name)

                if i == len(self._formatted_record) - 1:
                    party_root = self.add_party_child(
                        str_root, party, party_model
                    )
                    self.party_items[party_root] = party

        self.feature_str_model[feature_id] = self.str_models.keys()

    def add_party_steam(self, parent, party_entity, party_id):
        """
        Add party steam with table icon and entity short name.
        :param parent: The parent of the party steam - STR steam.
        :type parent: QStandardItem
        :param party_entity: The party entity object.
        :type party_entity: Object
        :param party_id: The id of the party entity
        :type party_id: Integer
        :return: The party root item
        :rtype: QStandardItem
        """
        party_icon = QIcon(
            ':/plugins/stdm/images/icons/table.png'
        )
        title = format_name(party_entity.short_name)
        party_root = QStandardItem(party_icon, title)
        party_root.setData(party_id)
        self.set_bold(party_root)

        parent.appendRow([party_root])
        party_root.setEditable(False)
        return party_root

    def add_party_child(self, parent, party_entity, party_model):
        """
        Add party children to the treeview.
        :param parent: The parent of the tree child
        :type parent: QStandardItem
        :param party_entity: The current party entity object
        :type party_entity: Object
        :param party_model: The model of the party record
        :type party_model: SQLAlchemy Model
        :return: The party root item
        :rtype: QStandardItem
        """
        party_id = party_model.id
        self.party_models[party_id] = party_model
        party_root = self.add_party_steam(
            parent, party_entity, party_id
        )
        # add STR children
        self.column_widget_registry(party_model, party_entity)
        for col, row in self._formatted_record.iteritems():
            party_child = QStandardItem('{}: {}'.format(col, row))
            party_child.setSelectable(False)
            party_root.appendRow([party_child])
        return party_root

    @staticmethod
    def set_bold(standard_item):
        """
        Make a text of QStandardItem to bold.
        :param standard_item: QStandardItem
        :type standard_item: QStandardItem
        """
        font = standard_item.font()
        font.setBold(True)
        standard_item.setFont(font)

    def treeview_error(self, message, icon=None):
        """
        Displays error message in feature details treeview.
        :param title: the title of the treeview.
        :type: String
        :param message: The message to be displayed.
        :type: String
        :param icon: The icon of the item.
        :type: Resource string
        :return: None
        """
        not_feature_ft_msg = QApplication.translate(
            'FeatureDetails', message
        )
        if icon == None:
            root = QStandardItem(not_feature_ft_msg)
        else:
            root = QStandardItem(icon, not_feature_ft_msg)

        self.view.setRootIsDecorated(False)
        self.model.appendRow(root)
        self.view.setRootIsDecorated(True)

    def expand_node(self, parent):
        """
        Make the last tree node expand.
        :param parent: The parent to expand
        :type QStandardItem
        :return:None
        """
        try:
            index = self.model.indexFromItem(parent)
            self.view.expand(index)
        except RuntimeError:
            pass

    def multi_select_highlight(self, index):
        """
        Highlights a feature with rubberBald class when selecting
        features are more than one.
        :param index: Selected QTreeView item index
        :type index: Integer
        """
        map = self.iface.mapCanvas()
        try:

            # Get the selected item text using the index
            selected_item = self.model.itemFromIndex(index)
            # Use multi-select only when more than 1 items are selected.
            if self.layer.selectedFeatures() < 2:
                return
            self.selected_root = selected_item
            # Split the text to get the key and value.
            selected_item_text = selected_item.text()

            selected_value = selected_item.data()
            # If the first word is feature, expand & highlight.
            if selected_item_text == format_name(self.spatial_unit.short_name):
                self.view.expand(index)  # expand the item
                # Clear any existing highlight
                self.clear_sel_highlight()
                # Insert highlight
                # Create expression to target the selected feature
                expression = QgsExpression(
                    "\"id\"='" + str(selected_value) + "'"
                )
                # Get feature iteration based on the expression
                ft_iteration = self.layer.getFeatures(
                    QgsFeatureRequest(expression)
                )

                # Retrieve geometry and attributes
                for feature in ft_iteration:
                    # Fetch geometry
                    geom = feature.geometry()
                    self.sel_highlight = QgsHighlight(map, geom, self.layer)

                    self.sel_highlight.setFillColor(selection_color())
                    self.sel_highlight.setWidth(4)
                    self.sel_highlight.setColor(QColor(212,95,0, 255))
                    self.sel_highlight.show()
                    break
        except AttributeError:
            # escape attribute error on child items such as party
            pass
        except IndexError:
            pass

    def steam_signals(self, entity):
        """
        Connects buttons to the steams in the treeview.
        :param entity: The entity to be edited or its document viewed.
        :type entity: Object
        """
        self.edit_btn.clicked.connect(
            lambda : self.edit_selected_steam(
                entity
            )
        )
        self.delete_btn.clicked.connect(
            self.delete_selected_item
        )
        self.view_document_btn.clicked.connect(
            lambda : self.view_steam_document(
                entity
            )
        )

    def steam_data(self, mode):
        """
        Gets tree item data to be used for editing and deleting a record.
        :param mode: The mode - edit or delete
        :type mode: String
        :return: The item data (the id), and the item - QStandardItem
        :rtype: Tuple
        """
        item = None
        # One item is selected and number of feature is also 1
        if len(self.layer.selectedFeatures()) == 1 and \
                        len(self.view.selectedIndexes()) == 1:
            index = self.view.selectedIndexes()[0]
            item = self.model.itemFromIndex(index)
            result = item.data()

        # One item is selected on the map but not on the treeview
        elif len(self.layer.selectedFeatures()) == 1 and \
                        len(self.view.selectedIndexes()) == 0:
            item = self.model.item(0, 0)
            result = item.data()

        # multiple features are selected but one treeview item is selected
        elif len(self.layer.selectedFeatures()) > 1 and \
                        len(self.view.selectedIndexes()) == 1:
            item = self.selected_root
            result = self.selected_root.data()
        # multiple features are selected but no treeview item is selected
        elif len(self.layer.selectedFeatures()) > 1 and \
             len(self.view.selectedIndexes()) == 0:
            result = 'Please, select an item to {}.'.format(mode)
        else:
            result = 'Please, select at least one feature to {}.'.format(mode)
        if result is None:
            if item is None:
                item = self.model.item(0, 0)
                result = item.data()
            else:
                result = item.parent().data()
        return result, item

    def edit_selected_steam(self, entity):
        """
        Edits the record based on the selected item in the tree view.
        :param entity: The entity of the record.
        :type entity: Object
        """
        id, item = self.steam_data('edit')

        feature_edit = True
        if id is None:
            return
        if isinstance(id, str):
            data_error = QApplication.translate(
                'DetailsTreeView', id
            )
            QMessageBox.warning(
                self.iface.mainWindow(),
                QApplication.translate(
                    'DetailsTreeView', 'Edit Error'
                ),
                data_error
            )
            return
        # STR steam - edit social tenure relationship
        if item.text() == self.str_text:

            str_model = self.str_models[item.data()]
            documents = self._supporting_doc_models(
                self.social_tenure.name, str_model
            )
            node_data = str_model, documents

            feature_edit = False
            edit_str = EditSTREditor(node_data)
            edit_str.exec_()

        # party steam - edit party
        elif item in self.party_items.keys():

            party = self.party_items[item]

            model = self.feature_model(self.party_items[item], id)
            editor = EntityEditorDialog(
                party, model, self.iface.mainWindow()
            )
            editor.exec_()
         # Edit spatial entity
        else:
            model = self.feature_model(entity, id)

            editor = EntityEditorDialog(
                entity, model, self.iface.mainWindow()
            )
            editor.exec_()

        self.view.expand(item.index())
        if feature_edit:
            self.update_edited_steam(entity, id)
        else:
            self.update_edited_steam(self.social_tenure, id)

    def delete_selected_item(self):
        """
        Deletes the selected item.
        """
        str_edit = False
        id, item = self.steam_data('delete')

        if isinstance(id, str):
            data_error = QApplication.translate(
                'DetailsTreeView', id
            )
            QMessageBox.warning(
                self.iface.mainWindow(),
                QApplication.translate('DetailsTreeView', 'Delete Error'),
                data_error
            )
            return

        if item.text() == self.str_text:
            str_edit = True
            db_model = self.str_models[id]

        elif item.text() == format_name(self.spatial_unit.short_name) and \
            id not in self.feature_str_model.keys():
            db_model = self.feature_model(self._entity, id)

        # if spatial unit is linked to STR, don't allow delete
        elif item.text() == format_name(self.spatial_unit.short_name) and \
                        id in self.feature_str_model.keys():


            delete_warning = QApplication.translate(
                'DetailsTreeView',
                'You have to first delete the social tenure \n'
                'relationship to delete the {} record.'.format(
                    item.text()
                )

            )
            QMessageBox.warning(
                self.iface.mainWindow(),
                QApplication.translate('DetailsTreeView', 'Delete Error'),
                delete_warning
            )
            return
        else:
            return
        if str_edit:
            del_msg = QApplication.translate(
                'DetailsTreeView',
                 "This action will remove the social tenure relationship "
                 "and dependent supporting documents from the database and "
                 "the documents folder. This action cannot be undone and "
                 "once removed, it can only be recreated through"
                 " the 'New Social Tenure Relationship' wizard."
                 "Would you like to proceed?"
                 "\nClick Yes to proceed or No to cancel."
            )
            delete_question = QMessageBox.critical(
                self.parentWidget(),
                QApplication.translate(
                    'DetailsTreeView',
                    'Delete Social Tenure Relationship'
                ),
                del_msg,
                QMessageBox.Yes | QMessageBox.No
            )

        else:
            delete_warning = QApplication.translate(
                'DetailsTreeView',
                'Are you sure you want to delete '
                'the selected record(s)?\n'
                'This action cannot be undone.'
            )

            delete_question = QMessageBox.warning(
                self.iface.mainWindow(),
                QApplication.translate('DetailsTreeView', 'Delete Warning'),
                delete_warning,
                QMessageBox.Yes | QMessageBox.No
            )
        if delete_question == QMessageBox.Yes:
            db_model.delete()

            if str_edit:
                del self.str_models[id]
                del self.feature_str_model[id]
            else:
                self.removed_feature = id
                del self.feature_models[id]


            remaining_str = len(self.str_models)

            self.updated_removed_steam(str_edit, item, remaining_str)
        else:
            return

    def update_edited_steam(self, entity, feature_id):
        """
        Updates the treeview show the changes in the data.
        :param entity: The entity of the steam edited
        :type entity: Object
        :param feature_id: The feature id
        :type feature_id: Integer
        """
        # remove rows before adding the updated ones.
        self.layer.setSelectedFeatures(
            self.feature_models.keys()
        )
        root = self.find_root(entity, feature_id)
        if root is None:
            return
        self.view.selectionModel().select(
            root.index(), self.view.selectionModel().Select
        )
        self.expand_node(root)
        self.multi_select_highlight(root.index())

    def find_root(self, entity, feature_id):
        """
        Finds the root item - the spatial entity item using the entity and
        the feature id.
        :param entity: The entity of the root - spatial entity
        :type entity: Object
        :param feature_id: The feature id
        :type feature_id: Integer
        :return: The root item
        :rtype: QStandardItem
        """
        all_roots = self.model.findItems(
            format_name(entity.short_name)
        )
        root = None
        for item in all_roots:
            if item.data() == feature_id:
                root = item
                break
        return root

    def updated_removed_steam(self, str_edit, item, remaining_str=0):
        """
        Updates a removed steam int the treeview by showing No STR defined.
        :param str_edit: A boolean showing if the delete is on STR steam or
        the spatial root.
        :type str_edit: Boolean
        :param item: The root item to be removed
        :type item: QStandardItem
        :param remaining_str: Remaining STR nodes after the delete
        :type remaining_str: Integer
        """
        if not str_edit:
            if len(self.feature_models) > 1:
                self.refresh_layers()
            feature_ids = self.feature_models.keys()
            self.layer.setSelectedFeatures(
                feature_ids
            )
        else:
            item.removeRows(0, 5)
            # No other STR record remains for the spatial unit,
            # show No STR Defined
            if remaining_str == 0:
                item.setText('No STR Defined')
                no_str_icon = QIcon(
                    ':/plugins/stdm/images/icons/remove.png'
                )
                item.setIcon(no_str_icon)
            else:
                row = item.row()
                item.parent().removeRow(row)

    def view_steam_document(self, entity):
        """
        A slot raised when view document button is clicked. It opens document
        viewer and shows a document if a supporting document exists for the
        record.
        :param entity: The entity object
        :type entity: Object
        """
        id, item = self.steam_data('edit')

        if id is None:
            return
        if isinstance(id, str):
            data_error = QApplication.translate('DetailsTreeView', id)
            QMessageBox.warning(
                self.iface.mainWindow(),
                QApplication.translate('DetailsTreeView', 'Edit Error'),
                data_error
            )
            return

        if item.text() == self.str_text:
            db_model = self.str_models[id]
        elif item in self.party_items:
            db_model = self.feature_model(self.party_items[item], id)
        else:
            db_model = self.feature_model(entity, id)
        if not db_model is None:
            docs = db_model.documents
            # Notify there are no documents for the selected doc
            if len(docs) == 0:
                msg = QApplication.translate(
                    'EntityBrowser',
                    'There are no supporting documents '
                    'for the selected record.'
                )

                QMessageBox.warning(
                    self.iface.mainWindow(),
                    self.doc_viewer_title,
                    msg
                )
            else:
                self.doc_viewer.load(docs)
