import sys

import qiapidoc.datas.cppclass
import qiapidoc.datas.cppenum
import qiapidoc.datas.cppfunction
import qiapidoc.datas.cppmacro
import qiapidoc.datas.cppnamespace
import qiapidoc.datas.cppstruct
import qiapidoc.datas.cpptypedef
import qiapidoc.datas.cppvariable
import qiapidoc.datas.hppfile

TYPES = {
    'class': qiapidoc.datas.cppclass.CPPClass,
    'define': qiapidoc.datas.cppmacro.CPPMacro,
    'enum': qiapidoc.datas.cppenum.CPPEnum,
    'file': qiapidoc.datas.hppfile.HPPFile,
    'function': qiapidoc.datas.cppfunction.CPPFunction,
    'namespace': qiapidoc.datas.cppnamespace.CPPNamespace,
    'struct': qiapidoc.datas.cppstruct.CPPStruct,
    'typedef': qiapidoc.datas.cpptypedef.CPPTypedef,
    'variable': qiapidoc.datas.cppvariable.CPPVariable,
}

def get_class(kind):
    try:
        return qiapidoc.datas.types.TYPES[kind]
    except KeyError:
# Uncomment this to debug:
#        print >> sys.stderr, 'Element kind `{}` is not yet implemented.'.format(
#            kind
#        )
        return None

def parse_type(root, objs, element):
    kind = element.attrib['kind']
    if kind in ['dir']:
#        print >> sys.stderr, 'Directory ignored.'
        return None
#    print >> sys.stderr, 'Found a compound element named', kind, '!'
    cls = qiapidoc.datas.types.get_class(kind)
    if cls is None:
        return None
    obj = cls(root, objs)
    obj.parse_attributes(element)
    obj.parse(element)
    return obj
