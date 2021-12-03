import sys
import struct
import bpy
from bpy.types import Operator
from .panel_pnl import *
import math

class MapImport_OP(Operator):
    bl_idname = "object.import_map"
    bl_label = "Import Map"
    bl_description = "Import Map"

    def load_str(self, file):
        bytes = b''
        b = file.read(1)
        while not b == b'\x00':
            bytes += b
            b = file.read(1)
        return bytes.decode("utf-8")

    def execute(self, context):
        user_prefs = context.preferences.addons[__package__].preferences
        if user_prefs.model_path != '':
            try:
                file = open(bpy.path.abspath(user_prefs.mprt_file), "rb")
            except:
                self.report({"ERROR"}, "Invalid directory.")
                return {'CANCELLED'}
            header = struct.unpack("3I", file.read(0xC))
            if header[0] != 0x7472706D:
                self.report({"ERROR"}, "Invalid file.")
                return {'CANCELLED'}

            scene = bpy.context.scene.props
            NameList = []
            posList = []
            rotList = []
            scaleList = []
            filter = ((scene.filter).replace(" ", "")).split(",")
            radius = scene.radius
            coordinates = scene.coordinates

            for i in range(header[2]):
                name = self.load_str(file)
                fpos = file.tell()
                posrotscale = struct.unpack("7f", file.read(0x1C))
                # XYZ, XYZW
                skip = False
                modPos = (posrotscale[0], posrotscale[1], posrotscale[2])
                if filter[0] != '':
                    for x in filter:
                        if x in name:
                            skip = True
                if radius != 0:
                    distance = math.dist(coordinates,modPos)
                    if distance > radius:
                        skip = True
                if skip == False:
                    scaleList.append((posrotscale[6],posrotscale[6],posrotscale[6]))
                    posList.append((posrotscale[0], posrotscale[1], posrotscale[2]))
                    rotList.append((math.radians(posrotscale[3]), math.radians(posrotscale[4]), math.radians(posrotscale[5])))
                    NameList.append(name)
                progress = (i/((header[2])-1))
                sys.stdout.write("\r{0} ▌{1}▐ {2}% \r".format("Parsing mprt...", "█"*(int(round(50*progress))) + "#"*(50-(int(round(50*progress)))), round(progress*100,2)))
                sys.stdout.flush()
            
            ObjectList=(list(dict.fromkeys(NameList)))
            AssetCollection = bpy.data.collections.new("Assets")
            bpy.context.scene.collection.children.link(AssetCollection)
            bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[AssetCollection.name]
            collections = {}
            print("\n")



            for i in range(len(ObjectList)):
                AName = ObjectList[i]
                progress = (i/((len(ObjectList))-1))
                sys.stdout.write("Importing... ({0}%) {1}...\n".format(round(progress*100,2),AName))
                try:
                    bpy.ops.import_scene.cast(filepath = bpy.path.abspath(bpy.data.scenes[0].props.model_directory + "%s//%s_LOD0.cast" % (AName,AName)))
                except:
                    print('Error loading %s.cast' % (AName))
                    PlaceholderCol = bpy.data.collections.new(AName)
                    AssetCollection.children.link(PlaceholderCol)
                collections[AName] = bpy.context.view_layer.active_layer_collection.collection.children[-1]



            bpy.context.view_layer.layer_collection.children[AssetCollection.name].exclude = True    
            bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection
            MapCollection = bpy.data.collections.new("Map")


            for i in range(len(NameList)):
                obj = bpy.data.objects.new(NameList[i], None)
                bpy.data.collections[MapCollection.name].objects.link(obj)
                obj.instance_type = 'COLLECTION'
                obj.instance_collection = collections[NameList[i]]
                #obj.rotation_mode = 'QUATERNION'
                obj.location = posList[i]
                obj.scale = scaleList[i]
                #obj.rotation_quaternion = rotList[i]
                obj.rotation_euler = rotList[i]
                #obj.rotation_mode = 'XYZ'
                progress = (i/((len(NameList))-1))
                sys.stdout.write("{0} ▌{1}▐ {2}% \r".format("Instancing...", "█"*(int(round(50*progress))) + "#"*(50-(int(round(50*progress)))), round(progress*100,2)))
                sys.stdout.flush()

            bpy.context.scene.collection.children.link(MapCollection)
            print('\nFinished!')
        else:
            self.report({"ERROR"}, "No file selected.")
            return {'CANCELLED'}
        return {'FINISHED'}
