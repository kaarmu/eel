
from elementary_lexer import *

class TreeNode:
    pass

@dataclass
class TreeNode_Sequence(TreeNode):
    children: list[TreeNode]

@dataclass
class TreeNode_Container(TreeNode):
    seq: TreeNode_Sequence

class TN_Pair:
    left: LexicalObject_Literal
    right: LexicalObject_Literal

class TN_Row(TreeNode_Sequence): pass

class TN_Col(TreeNode_Sequence): pass

class TN_Curly(TreeNode_Container): pass

def parse(text):
    pass

