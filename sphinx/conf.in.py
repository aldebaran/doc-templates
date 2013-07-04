import os
import sys
source_suffix = '.rst'
copyright = u'2011-2012, Aldebaran Robotics'
version = "{version}"
release = "{version}"
master_doc = 'index'
pygments_style="sphinx"

html_theme="djangodocs"
html_use_index = True


extensions = ["sphinx.ext.pngmath",
              "sphinx.ext.todo",
              "sphinx.ext.intersphinx",
              "sphinx.ext.ifconfig",

exclude_patterns=["family/bulk/*"]
sys.path.insert(0, os.path.abspath("tools/doxylink"))
exclude_patterns = ["**bulk"]

nitpicky=True
nitpick_ignore = [('naoqi:type', 'std::string')]

build_type = os.environ.get("build_type")

html_theme_options = dict()

if build_type == "release":
    html_show_source_link=False
    html_copy_source=False
    keep_warnings=False
    todo_include_todos=False
else:
    html_show_source_link=True
    html_copy_source=True
    keep_warnings=True
    todo_include_todos=True

html_theme_options['build_type'] = build_type

def setup(app):
    app.add_config_value("build_type", "internal", True)
