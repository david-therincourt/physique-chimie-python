#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Test documentation build configuration file, created by
# sphinx-quickstart on Thu Apr 25 16:42:05 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Sciences Physiques & Python'
copyright = '2019, David THERINCOURT'
author = 'David THERINCOURT'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = 'alpha'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pythondoc'


# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'pdflatex'
latex_elements = {
	'papersize': 'a4paper',
	'releasename':" ",
	'fncychap': '\\usepackage{fncychap}',
	'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
	'figure_align':'htbp',
	'pointsize': '10pt',

	'preamble': r'''
	%% %% %% %% %% %% %% %% %% %% Meher %% %% %% %% %% %% %% %% %%
	%% %add number to subsubsection 2=subsection, 3=subsubsection
	%% % below subsubsection is not good idea.
	\setcounter{secnumdepth}{3}
	%
	%% %% Table of content upto 2=subsection, 3=subsubsection
	\setcounter{tocdepth}{2}
	\usepackage{amsmath,amsfonts,amssymb,amsthm}
	\usepackage{graphicx}
	%% % r educe spaces for Table of contents, figures and tables
	%% % i t is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
	\usepackage[notlot,nottoc,notlof]{}
	\usepackage{color}
	\usepackage{transparent}
	\usepackage{eso-pic}
	\usepackage{lipsum}
	\usepackage{footnotebackref} %% link at the footnote to go to the place of footnote in the text
	%% spacing between line
	\usepackage{setspace}
	%% %% \onehalfspacing
	%% %% \doublespacing
	\singlespacing
	%% %% %% %% %% % d atetime
	\usepackage{datetime}
	\newdateformat{MonthYearFormat}{%
	\monthname[\THEMONTH], \THEYEAR}
	%% RO, LE will not work for 'oneside' layout.
	%% Change oneside to twoside in document class
	\usepackage{fancyhdr}
	\pagestyle{fancy}
	\fancyhf{}
	%% % Alternating Header for oneside
	\fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
	\fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}
	%% % Alternating Header for two side
	%\fancyhead[RO]{\small \nouppercase{\rightmark}}
	%\fancyhead[LE]{\small \nouppercase{\leftmark}}
	% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
	\fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny David THERINCOURT} }{}{\tiny sqdsq}}
	%% % Alternating Footer for two side
	%\fancyfoot[RO, RE]{\scriptsize Meher Krishna Patel (mekrip@gmail.com)}
	%% % page number
	\fancyfoot[CO, CE]{\thepage}
	\renewcommand{\headrulewidth}{0.5pt}
	\renewcommand{\footrulewidth}{0.5pt}
	\RequirePackage{tocbibind} %% % c omment this to remove page number for following
	\addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
	\addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
	\addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
	% \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}
	%% reduce spacing for itemize
	\usepackage{enumitem}
	\setlist{nosep}
	%% %% %% %% %% % Quote Styles at the top of chapter
	\usepackage{epigraph}
	\setlength{\epigraphwidth}{0.8\columnwidth}
	\newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
	%% %% %% %% %% % Quote for all places except Chapter
	\newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
	''',

	'maketitle': r'''
	\pagenumbering{Roman} %% % to avoid page 1 conflict with actual page 1
	\begin{titlepage}
	\centering
	\vspace*{40mm} %% % * is used to give space from top
	\textbf{\Huge {Python pour les sciences physiques}}
	\vspace{0mm}
	\begin{figure}[!h]
	\centering
	\includegraphics[scale=0.4]{Python_logo.png}
	\end{figure}
	\vspace{0mm}
	\\
	\Large \textbf{{David THERINCOURT}}
	\vspace*{0mm}
	\\
	\small 3 juin 2019
	%% \vfill adds at the bottom
	\vfill
	\small \textit{Plus d'informations sur }{\href{http://???}{}}
	\end{titlepage}
	\clearpage
	\pagenumbering{roman}
	\tableofcontents
	%\listoffigures
	%\listoftables
	\clearpage
	\pagenumbering{arabic}
	''',
	# Latex figure (float) alignment
	#
	# 'figure_align': 'htbp',
	'sphinxsetup': \
	'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
	verbatimwithframe=true, \
	TitleColor={rgb}{0,0,0}, \
	HeaderFamily=\\rmfamily\\bfseries, \
	InnerLinkColor={rgb}{0,0,1}, \
	OuterLinkColor={rgb}{0,0,1}',
	'tableofcontents':' ',

}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Python.tex', 'Python pour les sciences physiques',
     'David THERINCOURT', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Python', 'Python pour les sciences physiques',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Python', 'Sciences physiques et Python',
     author, 'dir', 'One line description of project.',
     'Miscellaneous'),
]

[extensions]
todo_include_todos=True

