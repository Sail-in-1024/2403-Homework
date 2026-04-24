# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '2403 Homework'
copyright = '2026, 颜赏'
author = '颜赏'

release = '1.1'
version = '1.1.0rc2'

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

today_fmt = '%b %d, %Y (%H:%M %Z)'

rst_prolog = '''
.. role:: del(line)
   :class: strikethrough
'''
rst_epilog = '''
.. |class-name| replace:: 803
.. |page-source| replace:: *来自 https://2403-homework.readthedocs.io/ ，PDF格式可以在网页下载*
'''

# -- Options for HTML output

html_theme = 'sphinx_book_theme'
html_theme_options = {
    'repository_url': 'https://github.com/Sail-in-1024/2403-Homework.git',
    'use_repository_button': True,
}

html_css_files = ['custom_homework.css']

html_static_path = ['_static']

html_last_updated_fmt = '%b %d, %Y (%H:%M %Z)'

# -- Options for EPUB output
epub_show_urls = 'footnote'