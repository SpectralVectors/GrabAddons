# https://github.com/salaivv/modifier-stack-manager/releases/download/0.2/modifier_stack_manager.zip
# https://github.com/BlenderCN/add_mesh_SpaceshipGenerator/archive/refs/heads/master.zip
# https://github.com/Jim-Kroovy/Mr-Mannequins-Tools/releases/download/v1.4/MrMannequinsTools-1.4.zip
# https://github.com/xavier150/Blender-For-UnrealEngine-Addons/releases/download/v0.2.8/blender-for-unrealengine.zip
# https://github.com/jayanam/jbake-tools/archive/refs/heads/main.zip
# https://github.com/curtisjamesholt/BY-GEN-public/archive/refs/heads/master.zip
# https://github.com/nutti/Screencast-Keys/releases/download/v3.5/screencast_keys.zip
# https://github.com/SavMartin/TexTools-Blender/releases/download/v1.4.4/TexTools_1_4_4.zip

import os, urllib.request, bpy

addons = []

addon = {
    'addon_name':'',
    'url':'',
    }
    
addon1 = addon.copy()
addon1['addon_name'] = 'jbake-tools-main'
addon1['url'] = 'https://github.com/jayanam/jbake-tools/archive/refs/heads/main.zip'
addons.append(addon1)

addon2 = addon.copy()
addon2['addon_name'] = 'BY-GEN-public-master'
addon2['url'] = 'https://github.com/curtisjamesholt/BY-GEN-public/archive/refs/heads/master.zip'
addons.append(addon2)

addon3 = addon.copy()
addon3['addon_name'] = 'TexTools_1_4_4'
addon3['url'] = 'https://github.com/SavMartin/TexTools-Blender/releases/download/v1.4.4/TexTools_1_4_4.zip'
addons.append(addon3)

addon4 = addon.copy()
addon4['addon_name'] = 'modifier_stack_manager'
addon4['url'] = 'https://github.com/salaivv/modifier-stack-manager/releases/download/0.2/modifier_stack_manager.zip'
addons.append(addon4)

for addon in addons:
    
    url_file = bpy.path.basename(addon['url'])
    module_name = bpy.path.display_name_from_filepath(addon['url'])
    filepath = str(os.path.expanduser('~/Downloads/') + url_file)
    file = urllib.request.urlretrieve(addon['url'], filepath)

    overwrite_setting = True
    bpy.ops.preferences.addon_install(overwrite=overwrite_setting, filepath=filepath)

    try:
        bpy.ops.preferences.addon_enable(module=module_name)
    except: # ModuleNotFoundError
        bpy.ops.preferences.addon_enable(module=addon['addon_name'])