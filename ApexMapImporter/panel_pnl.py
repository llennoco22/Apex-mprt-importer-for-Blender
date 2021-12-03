import bpy
from bpy.types import Panel
import os

class PanelProperties(bpy.types.PropertyGroup):
    filter : bpy.props.StringProperty(name= 'Filter', description='Exclude certain file names on import',)
    mprt_directory : bpy.props.StringProperty(name='MPRT File', subtype='FILE_PATH')
    coordinates : bpy.props.FloatVectorProperty(name='Coordinates', subtype='XYZ', precision=2, description='Map coordinates')
    radius : bpy.props.FloatProperty(name='Radius', description='Radius dependent on selected coordinates', min=0)

class MapImp_PT_Panel(Panel):
    bl_label = "Apex Map Importer"
    bl_idname = "OBJECT_PT_map_import"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Apex Map Importer"


    def draw(self, context):
        user_prefs = context.preferences.addons[__package__].preferences
        scene = context.scene
        panelprops = scene.props

        layout = self.layout

        row = layout.row()
        row.label(text="Map Selection", icon='RESTRICT_SELECT_OFF')
        box = layout.box()
        if os.path.isfile(bpy.path.abspath(user_prefs.mprt_file)) == False:
            box.prop(user_prefs, 'mprt_file')
            box.label(text="No valid file selected.", icon='ERROR')
        else:
            box.prop(user_prefs, 'mprt_file')
        if os.path.isdir(bpy.path.abspath(user_prefs.model_path)) == False:
            box.prop(user_prefs, 'model_path',)
            box.label(text="No valid directory selected.", icon='ERROR')
        else:
            box.prop(user_prefs, 'model_path',)
        layout.separator(factor= 1)
        row = layout.row()
        row.label(text="Import Settings", icon='PREFERENCES')
        box = layout.box()
        box.prop(panelprops, 'filter', icon='FILTER')
        box.prop(panelprops, 'coordinates')
        box.prop(panelprops, 'radius')
        layout.separator(factor= 1)
        col = layout.column()
        col.scale_y = 2.0
        col.operator("object.import_map", text="Import Map")
