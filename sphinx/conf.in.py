import os
import sys
source_suffix = '.rst'
copyright = u'2011-2012, Aldebaran Robotics'
version = "{version}"
release = "{version}"
master_doc = 'index'
pygments_style="sphinx"

html_theme_path = ["{themes_path}"]
html_theme="djangodocs"
html_use_index = True

sys.path.insert(0, "{ext_path}")

extensions = ["sphinx.ext.pngmath",
              "sphinx.ext.todo",
              "sphinx.ext.intersphinx",
              "doxylink"]

exclude_patterns=["family/bulk/*"]
sys.path.insert(0, os.path.abspath("tools/doxylink"))
doxylink = {doxylink}
intersphinx_mapping = {intersphinx_mapping}
exclude_patterns = ["**bulk"]

# Useful when building internal doc,
# we should remove that when building
# official doc
nitpicky=True
nitpick_ignore = [('naoqi:type', 'std::string')]
keep_warnings=True
html_show_source_link=True
todo_include_todos=True
