"""A simple Python template renderer, for a nano-subset of Django syntax."""

# # https://github.com/aosabook/500lines/tree/master/template-engine/code

# Coincidentally named the same as http://code.activestate.com/recipes/496702/ but different

# rewrite by zhengxu at github.com/notfresh, 2021-01-02 09:04:37

import re

class SyntaxError(ValueError):
    def __init__(self, msg=""):
        self.msg = msg
        pass

    def __str__(self):
        return self.msg

class CodeBuilder:

    def __init__(self, indent_level=0):
        self.code = []
        self.indent_level = indent_level
        self.intent_char = ' ' * 4

    def __str__(self):
        return ''.join([str(item) for item in self.code]) # some item is not str but Codebuilder object

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        self.indent_level -= 1

    def add_line(self, line):
        self.code.append( self.indent_level*self.intent_char + line + '\n')

    def add_section(self):
        sect = CodeBuilder(self.indent_level)
        self.code.append(sect)
        return sect

    def get_globals(self):
        assert self.indent_level == 0
        python_source = str(self)
        global_namespace = {}
        exec(python_source, global_namespace)
        return global_namespace

class Templite: # this is a template engine, but it's mini, so we call it Templite
    """
    the templite can translate the template with context which means variables into static html or something else  like django but with a mini implementation
    support {{ variables | filter | filter2 }} , {% if %}, {% for item in list %}, {{ endif }},{{ endfor }}
    support nested control flow such as `if` or `for`
    support varibles.member_attribute, if the varibles are dictionaries, access the key also with dot `.`, not []
    not support `include`
    not support variables not privided in context but in {{}} or in for clause, these cause syntax error, you can fix it if you like it
    """

    def __init__(self, template, *contexts):
        """
        :param template: it could be a str, or a filepath which is relative or absolute
        :param contexts: filter functions or injected variables, they are both ok
        """
        import sys, os
        cwd = os.getcwd()

        template_path = ''
        if os.path.exists(template):
            template_path = template
        elif os.path.exists(os.path.join(cwd, template)):
            template_path = os.path.join(cwd, template)
        else:
            pass

        if template_path:
            with open(template_path, encoding='utf-8') as file:
                template = file.read()
        self.all_variables = []
        self.loop_variables = []

        code = CodeBuilder()
        code.add_line('def render(context, do_dots):')
        code.indent()
        vars_code = code.add_section()
        code.add_line("result = []")
        code.add_line("append_result = result.append")
        code.add_line("append_extend = result.extend")
        code.add_line('to_str = str') # local function is faster that global or built-in function

        code.add_line(" return ''.join(result) ")
        code.dedent()
        self._render_function = code.get_globals()['render']












