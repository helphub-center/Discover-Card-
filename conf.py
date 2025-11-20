# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Discover Card Activation Guide'
copyright = '2025, Discover'
author = 'Discover Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (leave blank or add as needed)
extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# Basic page info
html_title = "How to Activate Your Discover Card – Complete Guide"
html_short_title = "Discover Card Activation"
html_favicon = 'favicon.ico'  # Ensure favicon.ico exists in _static or root folder

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (optional)
# html_static_path = ['_static']
