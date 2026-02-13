# 🚀 GAIB H3D: Inteligencia Artificial Generativa Bria con Hunyuan 3D

![Software](https://img.shields.io/badge/Software-Blender_(+4.0)-orange?logo=blender)
![ComfyUI](https://img.shields.io/badge/Backend-ComfyUI-blue)
![Python](https://img.shields.io/badge/Code-Python%203.10-yellow?logo=python)
![Mixamo](https://img.shields.io/badge/Rigging-Mixamo-red)

**GAIB H3D** es un puente directo entre el poder generativo de **Hunyuan3D + Bria AI** y el entorno profesional de **Blender**. Este Add-on permite a los artistas, animadores y a desarrolladores de videojuegos generar modelos 3D texturizados a partir de texto y prepararlos para su exportación a Mixamo para para un proceso automatizado de rigging.

---

## 🎯 Sobre este Proyecto

* 🎨 **Generación de Texto a 3D:** Utiliza Hunyuan3D (v2.1) para geometría de alta fidelidad.
* 🖌️ **Auto-Texturizado:** Integra proyección de texturas vía Juggernaut XL y Bria AI (RMBG) para la eliminación de fondos.
* 🦴 **Listo para Auto-Rig:** Exportación automatizada a formato `.fbx` optimizado para Mixamo.
* 🔒 **Privacidad Local:** Todo el procesamiento ocurre en tu máquina (Localhost), garantizando la privacidad de los datos.

---

## 🛠️ Requisitos Previos

* **SO:** Windows 10/11.
* **GPU:** NVIDIA RTX 3060 o superior (Recomendado 12GB+ VRAM, Mínimo 6GB).
* **Software Base:**
    * [Blender 4.0](https://www.blender.org/) o superior.
    * [ComfyUI](https://github.com/comfyanonymous/ComfyUI) (Instalación Estándar o Portable).

---

## 📦 Guía de Instalación Paso a Paso

### Fase 1: Configuración del Backend (ComfyUI)

1.  **Instalar Nodos Requeridos:**
    Usa el *ComfyUI Manager* para instalar estos nodos si no los tienes:
    * `ComfyUI-Hunyuan3DWrapper`
    * `ComfyUI-Bria_AI-RMBG`

2.  **Descargar Modelos:**
    Coloca los checkpoints en sus carpetas correspondientes (`ComfyUI/models/...`):
    * **Hunyuan3D v2.0:** `models/hunyuan3d/`
    * **Juggernaut XL (o similar):** `models/checkpoints/`
    * **Bria RMBG 1.4:** `models/loras/` o la carpeta designada por el nodo.

### Fase 2: Instalación del Add-on de Blender

1.  Descarga el archivo `.zip` de este repositorio (o comprime juntos `__init__.py` y `workflow.json`).
2.  Abre Blender y ve a **Edit > Preferences > Add-ons**.
3.  Haz clic en **Install...** y selecciona el archivo `.zip`.
4.  Marca la casilla ☑️ **GAIH3D** para activarlo.

---

## ⚙️ Configuración (¡Importante!)

1.  En Blender, ve a la pestaña de **Scripting**.
2.  Si es necesario, edita la variable `COMFY_OUTPUT_DIR` en el script para que apunte a tu carpeta `ComfyUI/output`.
    ```python
    # Ejemplo:
    COMFY_OUTPUT_DIR = r"C:\TuUsuario\ComfyUI\output"
    ```
3.  Asegúrate de que ComfyUI se esté ejecutando en `http://127.0.0.1:8188`.

---

## 🎮 ¿Cómo Usar?

1.  **Iniciar ComfyUI:** Asegúrate de que la consola esté abierta y esperando comandos.
2.  **Abrir Blender:** Presiona la tecla `N` en el Viewport 3D para abrir la barra lateral.
3.  **Pestaña Gen AI:**
    * Introduce tu *prompt* (ej. *"A futuristic robot, metallic, t-pose"*).
    * Haz clic en **Generate Model**.
    * *Espera unos segundos mientras la consola de ComfyUI procesa...*
4.  **Resultados:** El modelo aparecerá en el centro de tu escena.
5.  **Exportar:** Haz clic en **Export for Mixamo Auto-Rig** para obtener el `.fbx` listo en tu carpeta de Descargas.

---

## 🤝 Créditos y Tecnologías

* **Hunyuan3D:** Modelo generativo 3D.
* **Bria AI:** Tecnología de eliminación de fondo.
* **ComfyUI Community:** Ecosistema de nodos.
* **Desarrollado por:** Alejandro González Ferrer, proyecto para la materia: Programación para Herramientas de Modelado 3D y presentado en el FIBO Hackathon, 2025.
