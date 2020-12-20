# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
#
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------

project = 'dreamtools'
copyright = '2020, Couleur West IT'
author = 'dreamgeeker'

# The full version, including alpha/beta/rc tags
version = '1.0'
release = '1.0.1'

# -- General configuration ---------------------------------------------------

extensions = [
'rinoh.frontend.sphinx', 'sphinx.ext.autodoc', 'sphinx.ext.viewcode','sphinx.ext.autosummary'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix=['.rst', '.md']
language = 'fr'
exclude_patterns = []
html_show_sphinx= False
add_module_names=False

autosummary_generate = True
autosummary_imported_members = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_logo='favicon2.png'
html_show_sphinx= False
html_search_language= 'fr'
html_theme = 'haiku'
html_sidebars = {
    '**':[
        'about.html', 'navigation.html','relations.html', 'searchbox.html','donate.html'
    ]
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']