project = '老子-道德经'
copyright = '2025, Chen-jiangqiao'
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

#响应式SVG的CSS
def setup(app):
    app.add_css_file('custom.css')
