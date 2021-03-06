# -*- coding: utf-8 -*-

from __future__ import unicode_literals


needs_sphinx = '1.8'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
    'sphinx_gallery.gen_gallery',
]

autodoc_default_options = {'members': None, 'inherited-members': None}

sphinx_gallery_conf = {
    'examples_dirs': '../../examples',
    'gallery_dirs': 'auto_examples'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# generate autosummary even if no references
# autosummary_generate = False

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# Generate the plots for the gallery
#plot_gallery = True

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'hmmlearn'
copyright = '2010-present, hmmlearn developers (BSD License)'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# The full version, including alpha/beta/rc tags.
import hmmlearn
version = release = hmmlearn.__version__

language = 'en'

exclude_trees = ['_build', 'includes']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_sidebars = {'**': ['about.html', 'navigation.html', 'localtoc.html']}
html_theme_options = {
    'description': 'Unsupervised learning and inference of Hidden Markov Models',
    'github_user': 'hmmlearn',
    'github_repo': 'hmmlearn',
    'github_banner': True,
    'github_button': False,
    'code_font_size': '80%',
}

htmlhelp_basename = 'hmmlearn_doc'

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['themes']


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = 'hmmlearn'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = 'logos/scikit-learn-logo-small.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = 'logos/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'hmmlearndoc'

# -- Options for LaTeX output ------------------------------------------------

latex_documents = [('index', 'user_guide.tex', 'hmmlearn user guide',
                    'hmmlearn developers', 'manual'), ]

# -- Misc. configuration --------------------------------------------------

trim_doctests_flags = True
