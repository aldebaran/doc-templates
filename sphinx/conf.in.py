import os
import sys
from qisys import ui
import qisys.worktree

source_suffix = '.rst'
copyright = u'2011-2012, Aldebaran Robotics'
version = "{version}"
release = "{version}"
master_doc = 'index'
pygments_style="sphinx"

html_theme="djangodocs"
html_use_index = True



def setup_tools():
    this_dir = os.path.basename(__file__)
    worktree_root = qisys.worktree.guess_worktree(raises=False)
    if not worktree_root:
        return
    worktree = qisys.worktree.WorkTree(worktree_root)
    tools_proj = worktree.get_project("doc/tools", raises=False)
    if not tools_proj:
        return
    if not tools_proj.path in sys.path:
        sys.path.insert(0, tools_proj.path)

setup_tools()
extensions = ["sphinx.ext.pngmath",
              "sphinx.ext.todo",
              "sphinx.ext.intersphinx",
              "sphinx.ext.ifconfig",
              "qiapidoc",
              "naoqi",
              #"cppwithparams", # causes sphinx to fail
              "extendcpp",
             ]

exclude_patterns=["family/bulk/*"]
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
