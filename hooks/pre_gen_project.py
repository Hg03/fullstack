#!/usr/bin/env python
"""Pre-generation hook for cookiecutter template."""

import re
import sys

# Get the project slug from cookiecutter context
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"


def validate_project_slug():
    """Validate that project slug is a valid Python module name."""
    module_regex = r'^[a-z][a-z0-9_]*$'
    
    if not re.match(module_regex, PROJECT_SLUG):
        print(f"ERROR: '{PROJECT_SLUG}' is not a valid Python module name!")
        print("\nModule names should:")
        print("  - Start with a lowercase letter")
        print("  - Contain only lowercase letters, numbers, and underscores")
        print("  - Not start with a number")
        print("\nExamples of valid names: my_project, churn_prediction, ml_model")
        sys.exit(1)


def validate_python_version():
    """Validate Python version format."""
    version_regex = r'^\d+\.\d+'


if __name__ == "__main__":
    validate_project_slug()
    validate_python_version()
    
    print("✓ Project name validation passed")
    print("✓ Python version validation passed")
    print("\nGenerating project...")

    
    if not re.match(version_regex, PYTHON_VERSION):
        print(f"ERROR: '{PYTHON_VERSION}' is not a valid Python version!")
        print("Please use format: X.Y (e.g., 3.12, 3.11)")
        sys.exit(1)
    
    # Check if version is supported (3.10+)
    major, minor = map(int, PYTHON_VERSION.split('.'))
    if major < 3 or (major == 3 and minor < 10):
        print(f"ERROR: Python {PYTHON_VERSION} is not supported!")
        print("Please use Python 3.10 or higher")
        sys.exit(1)


if __name__ == "__main__":
    validate_project_slug()
    validate_python_version()
    
    print("✓ Project name validation passed")
    print("✓ Python version validation passed")
    print("\nGenerating project...")
