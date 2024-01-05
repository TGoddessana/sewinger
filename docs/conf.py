project = "sewinger"
copyright = "2024, tgoddessana"
author = "tgoddessana"
release = "0.1.0"

extensions = [
    "autodoc2",
    "sphinx.ext.napoleon",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_permalinks_icon = "<span>#</span>"
html_theme = "sphinxawesome_theme"
html_static_path = ["_static"]

source_suffix = [
    ".rst",
    ".md",
]

master_doc = "pages/index"

# autodoc2 settings.
autodoc2_packages = [
    "../sewinger/",
]
autodoc2_render_plugin = "myst"
myst_enable_extensions = ["fieldlist"]
