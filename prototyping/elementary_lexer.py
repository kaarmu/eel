
from dataclasses import dataclass
import string


INDENT = '  '
IDENTIFIER = string.ascii_letters + '_'
SYMBOL = '-=[];\,./~!@#$%^&*()+{}:|<>?'
NUMBER = string.digits
STRING = '"' + "'"
WHITESPACE = string.whitespace


@dataclass
class LexerObject:
    linenr: int
    cursnr: int

@dataclass
class LexerObject_Literal(LexerObject):
    content: str

class LO_NEWLINE(LexerObject): pass

class LO_INDENT(LexerObject): pass

class LO_IDENTIFIER(LexerObject_Literal): pass

class LO_SYMBOL(LexerObject_Literal): pass

class LO_NUMBER(LexerObject_Literal): pass

class LO_STRING(LexerObject_Literal): pass


def lookahead(line: str, cursnr: int, group: str) -> int:

    while cursnr < len(line) and line[cursnr] in group:
        cursnr += 1

    return cursnr


def lexer(text: str):

    for linenr, line in enumerate(text.splitlines()):

        cursnr = 0

        # indentation...
        while line[cursnr:].startswith(INDENT):
            yield LO_INDENT(linenr, cursnr)
            cursnr += len(INDENT)

        while cursnr < len(line):

            # symbols...
            cursend = lookahead(line, cursnr, SYMBOL)
            if cursnr != cursend:
                yield LO_SYMBOL(linenr, cursnr, line[cursnr:cursend])
                cursnr = cursend
                continue

            # identifier...
            cursend = lookahead(line, cursnr, IDENTIFIER)
            if cursnr != cursend:
                LO_IDENTIFIER(linenr, cursnr, line[cursnr:cursend])
                cursnr = cursend
                continue

            # number...
            cursend = lookahead(line, cursnr, NUMBER)
            if cursnr != cursend:
                LO_NUMBER(linenr, cursnr, line[cursnr:cursend])
                cursnr = cursend
                continue

            # string...
            cursend = lookahead(line, cursnr, STRING)
            if cursnr != cursend:
                LO_STRING(linenr, cursnr, line[cursnr:cursend])
                cursnr = cursend
                continue

            # remove whitespace
            if line[cursnr] in WHITESPACE:
                cursnr += 1
                continue

            raise Exception('waddd')


if __name__ == '__main__':

    string = """
div: (a: int, b: int) -> float = {
  return a/b;
}
"""

    for o in lexer

