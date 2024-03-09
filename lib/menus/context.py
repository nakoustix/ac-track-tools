import re
from bpy.types import Menu

from ...utils.constants import SURFACE_VALID_KEY
from ..configs.surface import AC_Surface

class WM_MT_AssignSurface(Menu):
    bl_label = "Assign Surface"
    bl_idname = "WM_MT_AssignSurface"

    def draw(self, context):
        layout = self.layout
        settings = context.scene.AC_Settings
        surface: AC_Surface
        for surface in settings.surfaces:
            if not re.match(SURFACE_VALID_KEY, surface.key):
                layout.label(text=f"Invalid surface key: {surface.key}")
                continue
            op = layout.operator("ac.assign_surface", text=surface.name)
            op.key = surface.key
        if len(settings.surfaces) == 0:
            layout.label(text="No surfaces available")

def surface_menu(self, context):
    if len(context.selected_objects) == 0: # only show the menu if an object is selected
        return
    objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
    if len(objects) == 0: # only show the menu if a mesh object is selected
        return
    layout = self.layout
    layout.separator()
    layout.menu("WM_MT_AssignSurface")
    layout.operator("ac.assign_wall")

