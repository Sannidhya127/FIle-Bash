# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import pathlib
import tibas.tt
import alabaster
import sphinx_adc_theme
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
import sphinx_theme
import murray

# -- Project information -----------------------------------------------------

project = 'File Bash'
copyright = '2022, Sannnidhya127'
author = '@ github.com/Sannnidhya127'

# The full version, including alpha/beta/rc tags
release = 'v0.7.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_book_theme'
# html_theme_path = [tibas.tt.get_path(), alabaster.get_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# html_logo = "FileBash.png"
extensions = [
    'sphinx.ext.duration',
    "sphinx_copybutton",
    "sphinx_issues",
    "sphinx_removed_in",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.httpdomain", 
    "sphinx.ext.viewcode",
]
