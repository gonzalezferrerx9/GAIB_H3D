# 🚀 GAIB H3D: Generative Artificial Intelligence Bria with Hunyuan 3D

![Blender](https://img.shields.io/badge/Blender-4.0%2B-orange?logo=blender)
![ComfyUI](https://img.shields.io/badge/Backend-ComfyUI-blue)
![Python](https://img.shields.io/badge/Code-Python%203.10-yellow?logo=python)
![Status](https://img.shields.io/badge/Status-Hackathon%20MVP-green)

**GAIB H3D** is a direct bridge between the generative power of **Hunyuan3D + Bria AI** and the professional **Blender** environment. This Add-on allows artists and developers to generate textured 3D models from text and prepare them for animation (Rigging) with a single click, without ever leaving the Blender interface.

---

## 🎯 About This Project

This repository contains the source code and workflow for integrating local Generative AI into professional 3D pipelines. The project solves the friction between asset generation and implementation.

**Key Features:**
* 🎨 **Text-to-3D Generation:** Utilizes Hunyuan3D (v2) for high-fidelity geometry.
* 🖌️ **Auto-Texturing:** Integrates texture projection via Juggernaut XL and Bria AI (RMBG) for background removal.
* 🦴 **Auto-Rig Ready:** Automated export to `.fbx` format optimized for Mixamo.
* 🔒 **Local Privacy:** All processing happens on your machine (Localhost), ensuring data privacy.

---

## 🛠️ Prerequisites

Before installing the Add-on, ensure you meet the following hardware and software requirements:

* **OS:** Windows 10/11.
* **GPU:** NVIDIA RTX 3060 or higher (Recommended 12GB+ VRAM, Minimum 6GB).
* **Base Software:**
    * [Blender 4.0](https://www.blender.org/) or higher.
    * [ComfyUI](https://github.com/comfyanonymous/ComfyUI) (Standard or Portable installation).

---

## 📦 Step-by-Step Installation Guide

### Phase 1: Backend Configuration (ComfyUI)

For Blender to "talk" to the AI, ComfyUI must have the necessary models loaded.

1.  **Install Required Nodes:**
    Use *ComfyUI Manager* to install these nodes if you don't have them:
    * `ComfyUI-Hunyuan3DWrapper`
    * `ComfyUI-Bria_AI-RMBG`
    * `ComfyUI-VideoHelperSuite` (for file loading/management)
    * `KJNodes` (optional, for utilities)

2.  **Download Models:**
    Place the checkpoints in their corresponding folders (`ComfyUI/models/...`):
    * **Hunyuan3D v2.0:** `models/hunyuan3d/`
    * **Juggernaut XL (or similar):** `models/checkpoints/`
    * **Bria RMBG 1.4:** `models/loras/` or the folder designated by the node.

### Phase 2: Blender Add-on Installation

1.  Download the `.zip` file from this repository (or zip `__init__.py` and `workflow.json` together).
2.  Open Blender and go to **Edit > Preferences > Add-ons**.
3.  Click on **Install...** and select the `.zip` file.
4.  Check the box ☑️ **Gen AI Bria3D+H** to enable it.

---

## ⚙️ Critical Configuration (Important!)

Since this is a Hackathon prototype (MVP), verifying the file output path on your local PC is necessary.

1.  In Blender, go to the **Scripting** tab.
2.  If necessary, edit the `COMFY_OUTPUT_DIR` variable in the script to point to your `ComfyUI/output` folder.
    ```python
    # Example:
    COMFY_OUTPUT_DIR = r"C:\YourUser\ComfyUI\output"
    ```
3.  Ensure ComfyUI is running at `http://127.0.0.1:8188`.

---

## 🎮 How to Use

1.  **Start ComfyUI:** Ensure the console is open and waiting for commands.
2.  **Open Blender:** Press the `N` key in the 3D Viewport to open the sidebar.
3.  **Gen AI Tab:**
    * Enter your prompt (e.g., *"A futuristic robot, metallic, t-pose"*).
    * Click on **Generate Model**.
    * *Wait a few seconds while the ComfyUI console processes...*
4.  **Results:** The model will appear in the center of your scene.
5.  **Export:** Click on **Export for Mixamo Auto-Rig** to get the `.fbx` ready in your Downloads folder.

---

## 🧪 Manual Mode / Testing (No Add-on)

If you prefer to test the AI workflow without installing the Blender Add-on, we have included the raw workflow file:

1.  Download the `workflow.json` file included in this repository.
2.  Open ComfyUI in your browser.
3.  Drag and drop the `workflow.json` file into the window.
4.  Done! Now you can generate manually and see the magic behind the scenes.

---

## 🤝 Credits & Technologies

* **Hunyuan3D Team (Tencent):** For the base generative model.
* **Bria AI:** For background removal technology.
* **ComfyUI Community:** For the node ecosystem.
* **Developed by:** Alejandro González Ferrer for FIBO Hackathon 2025.

---

⚖️ *This project is distributed under the MIT License. Use responsibly.*