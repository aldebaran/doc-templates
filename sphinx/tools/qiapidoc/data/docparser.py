import re
import sys

from qiapidoc.mycpp import DefinitionParser, DefinitionError
from qiapidoc.data.rootparser import RootParser

class DocParser(RootParser):
    def __init__(self, *args, **kwargs):
        RootParser.__init__(self, *args, **kwargs)
        self.sorting_type, self._definition = None, ''

    def _get_fulltext(self, element):
        return ''.join(element.itertext())

    def _replace_text(self, element, text=None, frmt='{full_text}'):
        full_text = self._get_fulltext(element) if text is None else text
        for child in element:
            child.clear()
        element.text = frmt.format(full_text = full_text)

    def _parse_briefdescription(self, element):
        self.parse(element)

    def _parse_detaileddescription(self, element):
        self.parse(element)

    def _parse_para(self, element):
        lst, self._contains_includename = None, False
        self.parse(element)
        if self._backtrace[-1] == 'briefdescription':
            lst = self.brief()
        elif self._backtrace[-1] == 'detaileddescription':
            lst = self.details()
        else:
            self._replace_text(element)
        if lst is not None:
            if lst and lst[-1] != '':
                lst.append('')
            res = self._get_fulltext(element).splitlines()
            if self._contains_includename:
                res[0] = res[0].lstrip()
            lst.extend(res)

    def _parse_verbatim(self, element):
        res = []
        for line in element.text.splitlines():
            if line.startswith('* ') or line == '*':
                line = line[2:]
            res.append(line)
        element.text = '\n'.join(res)

    def _in_detaileddescription(self):
        return ('detaileddescription' in self._backtrace)

    def _in_briefdescription(self):
        return ('briefdescription' in self._backtrace)

    def _parse_type(self, element):
        self._definition += self._get_fulltext(element)

    def _parse_definition(self, element):
        def sublist_pos(a, b):
            len_a = len(a)
            for it in xrange(len(b) - len_a + 1):
                if b[it:it + len_a] == a:
                    return it
            return -1
        def split_tokens(definition):
            tmp = [it.strip() for it in re.split('(\w+)', definition)]
            return [''.join(it.split()) for it in tmp
                    if it and 'API' not in it]
        definition = split_tokens(element.text)
        cur_def = split_tokens(self._definition)
        it = sublist_pos(cur_def, definition)
        if it != -1:
            definition = definition[it + len(cur_def):]
        self._definition += u' ' + u' '.join(definition)
        tmp = self._definition.split('::')
        self._definition = u'::'.join([it.strip() for it in tmp])
        self._definition = self._definition.replace('~ ', '~')

    def _parse_argsstring(self, element):
        if element.text is not None:
            self._definition += element.text

    def get_obj(self):
        try:
            _def = DefinitionParser(self._definition)
            self.copy_obj(self._get_def_function()(_def))
        except DefinitionError:
            print >> sys.stderr, 'Could not parse following doxygen',
            print >> sys.stderr, 'definition:', self._definition
            return False
        return True

    def _get_def_function(self):
        raise NotImplementedError('must be implemented by child.')
