# Full Stack ML Project Template

### Table of Content
1. [Brief](#brief)
2. [Utility](#utility)
3. [Prerequisites](#prerequisites)
4. [Start](#start)

### Brief

Introducing Machine Learning Project Template. Let me share you the reason behind creating this. Everytime, when we are start with project, so much things travel around our cute little brain i.e. I need to **dockerize** the whole project, create **reproducible configuration management**, perform the **modularization** in an efficient way, make some **shortcuts** through which we can trigger some scripts quickly, creating **github actions** workflow. In this template, I covered all of these to get you started asap.

### Utility

I only created a template which helps you get started with all of the above steps. I haven't included __sklearn, mlflow__ etc. This will vary based on your separate usecases. I added utilities as below:

- **Dockerization and Environment Management**: Docker, UV
- **Configuration Management**: Hydra-Core
- **Commandline Shortcuts**: Justfile
- **Type Checking & Formatting**: Ruff, Ty with pre commit

### Prerequisites

Make sure, you have **docker** and **python** installed.

### Start

- Use this repo as **template**.
- Start the docker service.
- Build the containter: `docker build -t <container_name> -f dockerfile .`.
- Run the container: `docker run -t -d <container_name>`.
- Once container is in running state, right click and **attach with visual studio code**.
- Activate your virtual environment: `source .venv/bin/activate`.
- Start customizing your project as per your usecase.