project = '老子-道德经'
copyright = '2025, pyzpyjxh@163.com'
author = '陈江桥'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# 扩展
extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgconverter',
    'sphinx.ext.autosummary',
]

# 设置主题
html_theme = 'sphinx_rtd_theme'
language = 'zh_CN'

# 支持Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# 图片路径设置
html_static_path = ['_static']
html_js_files = ['svg-interaction.js',]
html_css_files = [
    'custom.css']

# 使用系统字体回退方案
html_theme_options = {
    'font_family': "'STSong', 'SimSun', serif",
}
