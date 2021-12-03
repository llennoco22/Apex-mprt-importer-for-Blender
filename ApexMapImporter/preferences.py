import bpy
from bpy.props import StringProperty

class ApexMapImporterPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    model_path: StringProperty(
        name="Model Directory",
        subtype='DIR_PATH'
    )

    mprt_file: StringProperty(
        name="MPRT File",
        subtype='FILE_PATH'
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Import Settings")
        layout.prop(self, "mprt_file")
        layout.prop(self, "model_path")
