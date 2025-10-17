#!/usr/bin/env python
"""Post-generation hook for cookiecutter template."""

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """Remove a file."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dirpath):
    """Remove a directory."""
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))


if __name__ == "__main__":
    # Initialize git repository
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Initial commit from cookiecutter template"')

    print("\n" + "="*60)
    print("✨ Project {{ cookiecutter.project_name }} created successfully!")
    print("="*60)
    print("\n📦 Project includes:")
    print("  • FastAPI for API development")
    print("  • Docker with UV package manager")
    print("  • Python {{ cookiecutter.python_version }}")
    print("  • Pre-commit hooks (ruff, ruff-format, ty)")
    print("\n🚀 Next steps:")
    print("1. cd {{ cookiecutter.project_slug }}")
    print("2. Build Docker image:")
    print("   docker build -t {{ cookiecutter.project_slug }} -f dockerfile .")
    print("3. Run container:")
    print("   docker run -t -d {{ cookiecutter.project_slug }}")
    print("\n💡 For local development with UV:")
    print("   uv sync")
    print("   uv run pre-commit install")
    print("\nHappy coding! 🚀\n")
