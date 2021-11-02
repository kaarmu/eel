
from ast import AST

class ParseObject:
    pass

class LiteralParseObject(ParseObject):
    pass

class Document(ParseObject):
    header: Header
    module: Module

    # flags
    # public members
    ...

class Module(ParseObject):
    members: list[ParseObject]

class Expression(ParseObject):
    pass

class Identifier(Expression, LiteralParseObject):
    name: str

class Operator(LiteralParseObject):
    symbol: str

class BinaryOperation(ParseObject):
    left: Expression
    operator: Operator
    right: Expression

class UnaryOperation(ParseObject):
    operator: Operator
    right: Expression

class Declaration(BinaryOperation):
    left: Identifier
    operator = Operator(':')
    right: Expression

class ProperDefinition(BinaryOperation):
    left: Declaration
    operator = Operator('=')
    right: Expression

class ImproperDefinition(BinaryOperation):
    left: Identifier
    operator = Operator('=')
    right: Expression

