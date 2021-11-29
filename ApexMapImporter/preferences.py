import bpy
from bpy.props import StringProperty

class ApexMapImporterPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    model_path: StringProperty(
        name="Model Directory",
        subtype='FILE_PATH'
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Import Settings")
        layout.prop(self, "model_path")