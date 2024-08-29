# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PlainTools'
copyright = '2024, gabrielmsilva00'
author = 'gabrielmsilva00'
release = '1.0.24828b'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autosectionlabel',
              'sphinx_collapse',
              ]

templates_path = ['_templates']
exclude_patterns = []

rst_prolog = """
.. role:: orange

.. role:: fuchsia

.. role:: magenta

.. role:: gray

"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
#html_theme_options = {
{
    'display_version': True,
    'vcs_pageview_mode': '',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}
html_permalinks_icon = '<span>§</span>'
html_static_path = ['_static']
html_css_files = ['font.css']
