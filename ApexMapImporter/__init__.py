# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ApexMapImporter",
    "author" : "Ed O'Connell, Andrew Simon",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 3),
    "location" : "",
    "warning" : "",
    "category" : "Object"
}

from . preferences import *
from . panel_op import *
from . panel_pnl import *

import bpy


classes = (PanelProperties, MapImp_PT_Panel, MapImport_OP, ApexMapImporterPreferences)

def register():
    for c in classes:
        bpy.utils.register_class(c)
        bpy.types.Scene.props = bpy.props.PointerProperty(type= PanelProperties)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.props

