#!/usr/bin/python3
from elem import Elem, Text
class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content, 'simple')
class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content, 'simple')
class Talbe(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr = attr, content = content)
class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content)
class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content, 'simple')
class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(self.__class__.__name__.lower(), attr, content, 'simple')



if __name__ == '__main__':
    # print(Html([Head(), Body()]))

    html = Html([Head(Title(Text('"Hello ground!"'))), Body([H1(Text('"Oh no, not again!"')), Img(attr={"src":'http://i.imgur.com/pfp3T.jpg'})])])

    print(html)