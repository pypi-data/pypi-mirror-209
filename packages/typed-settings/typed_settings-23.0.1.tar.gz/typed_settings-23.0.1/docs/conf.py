try:
    from importlib.metadata import version as get_version
except ImportError:
    # py37 - Just create a mock for testing:
    def get_version(_):  # type: ignore[misc]
        return "0.0.0"


project = "Typed Settings"
author = "Stefan Scherfke"
copyright = "2020, Stefan Scherfke"
release = get_version("typed-settings")
version = ".".join(release.split(".")[0:2])


extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "smartquotes",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


html_theme = "furo"
html_theme_options = {
    # "logo_only": True,
    # "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "#266DB4",
        "color-brand-content": "#266DB4",
    },
    "dark_css_variables": {
        "color-brand-primary": "#3186DC",
        "color-brand-content": "#3186DC",
    },
}
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]
html_logo = "_static/typed-settings-spacing.svg"
html_title = "Typed Settings"


# Autodoc
autodoc_member_order = "bysource"

# Copybutton
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

# Intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "attrs": ("https://www.attrs.org/en/stable/", None),
    "cattrs": ("https://cattrs.readthedocs.io/en/latest/", None),
    "click": ("https://click.palletsprojects.com/en/latest/", None),
    "click-option-group": (
        "https://click-option-group.readthedocs.io/en/latest/",
        None,
    ),
}
