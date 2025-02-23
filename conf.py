# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SillyTavern 内容 by 青空莉想做舞台少女的狗'
copyright = '2024, 青空莉想做舞台少女的狗'
author = '青空莉想做舞台少女的狗'
html_title = f'{project}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_examples',
    'sphinx_last_updated_by_git',
    'sphinx_sitemap',
    'sphinx_tabs.tabs',
    'sphinx_togglebutton',
    'sphinxext.opengraph',
]

extlinks = {
    'resource': ('https://gitgud.io/SmilingFace/tavern_resource/-/raw/main/%s?inline=false', '[资源 %s]'),
    'resource_commit': ('https://gitgud.io/SmilingFace/tavern_resource/-/raw/%s?inline=false', '[资源 %s]'),
}

togglebutton_hint = "点击展开"
togglebutton_hint_hide = "点击隐藏"

templates_path = ['_templates']
exclude_patterns = ['README.md']

rst_prolog = '\n'.join(
    list(
        map(
            lambda filename: open(f'_static/{filename}', 'r', encoding="utf8").read(),
            ['links.rst']))) + '\n'

language = 'zh_CN'

html_copy_source = False
html_show_sourcelink = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_theme_options = {
    'icon_links': [
        {
            'name': 'Gitlab',
            'url': 'https://gitlab.com/sillyme/doc',
            'icon': 'fa-brands fa-gitlab',
        }
    ],
    'repository_url': 'https://gitlab.com/sillyme/doc',
    'search_as_you_type': True,
    'show_nav_level': 0,
    'show_prev_next': True,
    'show_toc_level': 2,
    'use_edit_page_button': True,
    'use_issues_button': True,
    'use_sidenotes': True,
    'use_source_button': True,
}
html_static_path = ['_static', '_theme']
html_search_language = 'zh'
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S'
git_last_updated_timezone = 'Asia/Shanghai'
html_baseurl = 'https://sillytavern-stage-girls-dog.readthedocs.io/'
sitemap_filename = 'sitemapindex.xml'
sitemap_url_scheme = '{link}'
html_extra_path = [
    '_static/robots.txt',
]


def setup(app):
    app.add_css_file("theme.css")
