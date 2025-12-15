# =================================================================================================
# ADDON METADATA / METADATOS DEL ADDON
# =================================================================================================

bl_info = {
    "name": "GAIB_H3D",
    "author": "Alejandro González Ferrer",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Gen AI",
    "description": "Generate 3D models via ComfyUI and export to FBX for auto-rig in Mixamo",
    "category": "Development",
}

# =================================================================================================
# LIBRARIES / LIBRERÍAS
# =================================================================================================

import bpy
import json
import urllib.request
import urllib.parse
import urllib.error
import random
import os
import time
import glob

# =================================================================================================
# CONFIGURATION / CONFIGURACIÓN
# =================================================================================================

# 1. COMFYUI OUTPUT PATH 
COMFY_OUTPUT_DIR = r"C:\Users\Aleja\Documents\Programas Varios\ComfyUI_windows_portable\ComfyUI\output"

# 2. JSON PATH 
ADDON_DIR = os.path.dirname(os.path.abspath(__file__))
WORKFLOW_PATH = os.path.join(ADDON_DIR, "workflow.json")

# Nodes Configuration 
ID_NODO_TEXTO = "20"
ID_NODO_SAMPLER = "27"
URL_BASE = "http://127.0.0.1:8188"

# =================================================================================================
# OPERATOR 1: GENERATE / GENERAR
# =================================================================================================

class IA_OT_Generar(bpy.types.Operator):
    bl_idname = "ia.generar"
    bl_label = "Generate Base Model"
    
    _timer = None
    prompt_id = None
    start_time = 0
    
    def modal(self, context, event):
        if event.type == 'TIMER':
            status = self.check_status()
            if status == "LISTO":
                self.report({'INFO'}, "Finished! Scanning folder... / ¡Terminado! Escaneando...")
                time.sleep(1.0) 
                if self.buscar_e_importar_ultimo_glb():
                    context.window_manager.event_timer_remove(self._timer)
                    return {'FINISHED'}
                else:
                    self.report({'ERROR'}, "New GLB not found / No se encontró GLB nuevo.")
                    context.window_manager.event_timer_remove(self._timer)
                    return {'CANCELLED'}
            elif status == "ERROR":
                self.report({'ERROR'}, "Connection Error / Error de conexión.")
                context.window_manager.event_timer_remove(self._timer)
                return {'CANCELLED'}
        return {'PASS_THROUGH'}

    def execute(self, context):
        self.start_time = time.time()
        pid = self.enviar_a_comfyui(context.scene.ia_prompt_text)
        if not pid:
            self.report({'ERROR'}, "Error sending. Is ComfyUI running?")
            return {'CANCELLED'}
        
        self.prompt_id = pid
        self.report({'INFO'}, f"Generating ID: {pid}...")
        self._timer = context.window_manager.event_timer_add(1.0, window=context.window)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def enviar_a_comfyui(self, texto):
        if not os.path.exists(WORKFLOW_PATH): 
            self.report({'ERROR'}, f"JSON not found at: {WORKFLOW_PATH}")
            return None
            
        with open(WORKFLOW_PATH, 'r', encoding='utf-8') as f: data = json.load(f)
        data[ID_NODO_TEXTO]["inputs"]["text"] = texto
        data[ID_NODO_SAMPLER]["inputs"]["seed"] = random.randint(1, 999999999)
        p = {"prompt": data}
        try:
            req = urllib.request.Request(f"{URL_BASE}/prompt", data=json.dumps(p).encode('utf-8'))
            with urllib.request.urlopen(req) as response: return json.loads(response.read())['prompt_id']
        except: return None

    def check_status(self):
        try:
            with urllib.request.urlopen(f"{URL_BASE}/history/{self.prompt_id}") as response:
                history = json.loads(response.read())
                if self.prompt_id in history: return "LISTO"
        except: pass
        return "PROCESANDO"

    def buscar_e_importar_ultimo_glb(self):
        search_paths = [
            os.path.join(COMFY_OUTPUT_DIR, "*.glb"),
            os.path.join(COMFY_OUTPUT_DIR, "mesh", "*.glb")
        ]
        archivos_encontrados = []
        for path in search_paths:
            archivos_encontrados.extend(glob.glob(path))
            
        if not archivos_encontrados: return False
        archivos_encontrados.sort(key=os.path.getmtime, reverse=True)
        ultimo_archivo = archivos_encontrados[0]
        
        try:
            bpy.ops.import_scene.gltf(filepath=ultimo_archivo)
            if bpy.context.selected_objects:
                obj = bpy.context.selected_objects[0]
                bpy.ops.object.shade_smooth()
                obj.location = (0,0,0)
                obj.scale = (1, 1, 1) 
            return True
        except: return False

# =================================================================================================
# OPERATOR 2: EXPORT FBX / EXPORTAR FBX
# =================================================================================================

class IA_OT_ExportFBX(bpy.types.Operator):
    bl_idname = "ia.export_fbx"
    bl_label = "Export to FBX"
    bl_description = "Export active model to Downloads folder / Exporta a Descargas"

    def execute(self, context):
        obj = context.active_object
        if not obj:
            self.report({'ERROR'}, "Select a model first! / ¡Selecciona un modelo!")
            return {'CANCELLED'}

       
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        
       
        home = os.path.expanduser("~")
        downloads_folder = os.path.join(home, "Downloads")
        fbx_path = os.path.join(downloads_folder, "model_for_mixamo.fbx")
        
        
        try:
            bpy.ops.export_scene.fbx(
                filepath=fbx_path,
                use_selection=True,
                axis_forward='-Z',
                axis_up='Y'
            )
            self.report({'INFO'}, f"Saved in Downloads: model_for_mixamo.fbx")
        except Exception as e:
            self.report({'ERROR'}, f"Export failed: {e}")
            return {'CANCELLED'}

        
        try:
            os.startfile(downloads_folder)
        except: pass
        
        return {'FINISHED'}

# =================================================================================================
# UI PANEL / PANEL DE INTERFAZ
# =================================================================================================

class ESCENA_PT_PanelIA(bpy.types.Panel):
    bl_label = "GAIB H3D"
    bl_idname = "ESCENA_PT_panel_ia"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "GAIB H3D"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Section 1: Generation
        layout.label(text="1. Generation:", icon='MESH_DATA')
        layout.prop(scene, "ia_prompt_text", text="")
        layout.operator("ia.generar", text="Generate Model", icon='SHADING_RENDERED')
        
        layout.separator()
        
        # Section 2: Export
        layout.label(text="2. Animation Prep:", icon='ARMATURE_DATA')
        row = layout.row()
        row.scale_y = 1.5
        layout.operator("ia.export_fbx", text="Export for Mixamo Auto-Rig", icon='EXPORT')

# =================================================================================================
# REGISTRATION / REGISTRO
# =================================================================================================

def register():
    bpy.types.Scene.ia_prompt_text = bpy.props.StringProperty(name="Prompt", default="")
    bpy.utils.register_class(ESCENA_PT_PanelIA)
    bpy.utils.register_class(IA_OT_Generar)
    bpy.utils.register_class(IA_OT_ExportFBX)

def unregister():
    bpy.utils.unregister_class(IA_OT_ExportFBX)
    bpy.utils.unregister_class(IA_OT_Generar)
    bpy.utils.unregister_class(ESCENA_PT_PanelIA)
    del bpy.types.Scene.ia_prompt_text

if __name__ == "__main__":
    register()