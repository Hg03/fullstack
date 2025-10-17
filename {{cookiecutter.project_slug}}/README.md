# 🚀 Full Stack ML Project Template

### 📑 Table of Contents
1. [✨ Brief](#brief)
2. [🛠️ Utility](#utility)
3. [📋 Prerequisites](#prerequisites)
4. [🎯 Start](#start)

---

### ✨ Brief

Introducing the **Machine Learning Project Template** – your shortcut to production-ready ML projects! 🎉

Let me share the story behind the creation of this. Every time we start a new project, our minds race with endless tasks: 
- 🐳 Need to **dockerize** the entire setup
- ⚙️ Create **reproducible configuration management**
- 🧩 Perform **modularization** efficiently
- ⚡ Set up **shortcuts** to trigger scripts quickly
- 🔄 Configure **GitHub Actions** workflows

This template covers **all of these** to get you started ASAP! No more reinventing the wheel – just clone, customize, and code! 💪

---

### 🛠️ Utility

I've created a powerful template that helps you hit the ground running with all the essential tools. I haven't included `sklearn`, `mlflow`, etc., as these will vary based on your specific use cases. Here's what's included:

- 🐳 **Dockerization and Environment Management**: Docker, UV
- ⚙️ **Configuration Management**: Hydra-Core
- ⚡ **Command-line Shortcuts**: Justfile
- ✅ **Type Checking & Formatting**: Ruff, Typer with pre-commit hooks

---

### 📋 Prerequisites

Make sure you have the following installed:
- 🐳 **Docker**
- 🐍 **Python**
- 📚 **Git**

---

### 🎯 Start

Ready to launch? Follow these simple steps:

1. 📋 Use this repo as a **template**
2. 🚀 Start the Docker service
3. 🏗️ Build the container: 

   ```bash
   docker build -t <container_name> -f dockerfile .
   ```
4. ▶️ Run the container: 

   ```bash
   docker run -t -d <container_name>
   ```
5. 🔗 Once the container is running, right-click and **attach with Visual Studio Code**
6. 🌟 Activate your virtual environment: 

   ```bash
   source .venv/bin/activate
   ```
7. 🎨 Start customizing your project according to your use case!

---
