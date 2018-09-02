# -*- coding: utf-8 -*-
"""
    RSpec lexer
    ~~~~~~~~~~~
    Pygments lexer for Ruby + RSpec.
    :copyright: Copyright 2012 Hugo Maia Vieira
    :license: BSD, see LICENSE for details.
"""

from pygments.lexers.c_cpp import CppLexer
from pygments.token import Name, Keyword



#from pygments.lexers.c_cpp import CppLexer

#from pygments.lexers.agile import RubyLexer


class MyCppLexer(CppLexer):
    name = 'MyCppLexer'
    aliases = ['mycpp']
    filenames = ['*.mycpp'] # just to have one if you whant to use

    EXTRA_TYPES = ['State', 'Command', 'CoverageFlightTrigger', 'shared_ptr', 'Trajectory', 'NodeHandle', 'Subscriber', 'Publisher', 'Rate']

    def get_tokens_unprocessed(self, text):
        for index, token, value in CppLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_TYPES:
                yield index, Keyword.Type, value
            else:
                yield index, token, value

