# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '2403 Homework'
copyright = '2026, 颜赏'
author = '颜赏'

release = '1.1'
version = '1.1.0a4'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

# html_theme_options = {
# }

# -- Options for EPUB output
epub_show_urls = 'footnote'

today_fmt = '%b %d, %Y (%H:%M %Z)'

rst_epilog = """
.. |class-name| replace:: 803
.. |page-source| replace:: *来自 https://2403-homework.readthedocs.io/*
"""