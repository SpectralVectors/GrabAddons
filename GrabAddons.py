bl_info = {
    "name": "Grab Addons",
    "author": "Spectral Vectors",
    "version": (0, 0, 3),
    "blender": (2, 90, 0),
    "location": "Preferences > Addons > GrabAddons",
    "description": "Download, install and activate community addons inside Blender",
    "warning": "",
    "doc_url": "",
    "category": "Addons",
}

import bpy, os, urllib.request

addon = {
    'label':'',
    'module_name':'',
    'url':'',
    }

community_addons = []

jbaketools = addon.copy()
jbaketools['label'] = 'JBake Tools by Jayanam'
jbaketools['module_name'] = 'jbake-tools-main'
jbaketools['url'] = 'https://github.com/jayanam/jbake-tools/archive/refs/heads/main.zip'
community_addons.append(jbaketools)

bygen = addon.copy()
bygen['label'] = 'BY-GEN by Curtis Holt'
bygen['module_name'] = 'BY-GEN-public-master'
bygen['url'] = 'https://github.com/curtisjamesholt/BY-GEN-public/archive/refs/heads/master.zip'
community_addons.append(bygen)

addons = community_addons

class GrabAddons(bpy.types.Operator):
    bl_idname = "preferences.grab_addons"
    bl_label = "Grab Addons"
    bl_space_type = 'PREFERENCES'
    bl_description = 'Download, install and activate community addons'

    def execute(self,context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        for addon in addons:
            
            url_file = bpy.path.basename(addon['url'])
            module_name = bpy.path.display_name_from_filepath(addon['url'])
            filepath = str(os.path.expanduser('~/Downloads/') + url_file)
            
            urllib.request.urlretrieve(addon['url'], filepath)

            bpy.ops.preferences.addon_install(overwrite=addon_prefs.overwrite_setting, filepath=filepath)

            try:
                bpy.ops.preferences.addon_enable(module=module_name)
            except: # ModuleNotFoundError
                bpy.ops.preferences.addon_enable(module=addon['module_name'])
        return{'FINISHED'}

class GrabAddon(bpy.types.Operator):
    bl_idname = "preferences.grab_addon"
    bl_label = "Grab Addon"
    bl_space_type = 'PREFERENCES'
    bl_description = 'Download, install and activate chosen addon'

    def execute(self,context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        addon = addon_prefs.addon
            
        url_file = bpy.path.basename(addon['url'])
        module_name = bpy.path.display_name_from_filepath(addon['url'])
        filepath = str(os.path.expanduser('~/Downloads/') + url_file)
        
        urllib.request.urlretrieve(addon['url'], filepath)

        bpy.ops.preferences.addon_install(overwrite=addon_prefs.overwrite_setting, filepath=filepath)

        try:
            bpy.ops.preferences.addon_enable(module=module_name)
        except: # ModuleNotFoundError
            bpy.ops.preferences.addon_enable(module=addon['module_name'])
        return{'FINISHED'}

class GrabAddonsPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    addon = {
    'label':'',
    'module_name':'',
    'url':'',
    }

    overwrite_setting : bpy.props.BoolProperty(
        name='Overwrite',
        default=True,
    )

    def getaddonsinfo(scene,context):
        return {(addon,addon['label'],addon['url']) for addon in addons}

    addonslist : bpy.props.EnumProperty(
        items=getaddonsinfo,
        name='Addons',
    )


    def draw(self,context):
        layout = self.layout

        layout.prop(self,'addonslist')
        row = layout.row()       
        row.label(text='Overwrite Existing Addons?')
        row.prop(self, 'overwrite_setting')
        row.operator('preferences.grab_addon', text='Grab Addon')
        row.operator('preferences.grab_addons', text='Grab Addons')
        

classes = [
    GrabAddonsPreferences,
    GrabAddons,
    GrabAddon,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

#bpy.ops.preferences.grab_addons()