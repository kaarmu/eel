import string
from parse_objs import *

class Lexer:

    IDENTIFIER = string.ascii_letters + '_'
    DIGITS = string.digits
    SYMBOLS = '~!@#$%^&*:|?-=\,./'
    WHITESPACE = ' \t'
    NEWLINE = '\n'

    text: str
    linenr: int
    cursor: int

    def __init__(self, text):
        self.text = text
        self.linenr = 0
        self.cursor = 0

    def consume(self, group):
        if self.text[0] in group:
            i = 1
            while self.text[i] in group:
                i += 1
            text, self.text = self.text[:i], self.text[i:]
            self.cursor += len(text)
            return text

    def __iter__(self):

        while self.text:

            if self.text[0] == self.NEWLINE:
                self.cursor = 0
                self.linenr += 1
                self.text = self.text[1:]

            self.consume(self.WHITESPACE)

            if text := self.consume(self.IDENTIFIER):
                yield text
            if text := self.consume(self.DIGITS):
                yield text
            if text := self.consume(self.SYMBOLS):
                yield text

class Parse:

    source: str
    _lexer: Lexer

    def __init__(self, filepath):

        with open(filepath) as f:
            self.source = f.read()

        self._lexer = Lexer(self.source)


def print(self) -> None:
    raise NotImplementedError()


if __name__ == '__main__':

    parser = ArgumentParser()

    parser.add_argument('--interpreter', '-i', action='store_true')
    parser.add_argument('--ast', '-a', metavar='FILE')

    args = parser.parse_args()

    if path := args.ast:

        with open(path) as f:
            tree = AST()

            tree(f.read()).print()

    elif args.interpreter:

        interpreter()
