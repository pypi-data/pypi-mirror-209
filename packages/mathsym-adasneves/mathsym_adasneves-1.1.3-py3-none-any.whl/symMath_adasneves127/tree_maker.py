from .tree_node import tree_node
from typing import List
from .token import token

def create_tree(node_list: List[tree_node]):
    dummy_node = tree_node("DUMMY", "", 0)
    node_list.insert(0, dummy_node)
    node_list.append(dummy_node)
    for index, node in enumerate(node_list):
        
        if node.type == "NUMBER" and node_list[index + 1].type == "VARIABLE":
            node_list.insert(index + 1, tree_node("MULTIPLICATION", "*", node.prec + 2))
        if node.type == "MINUS" and node_list[index + 1].type == "MINUS":
            double_neg(node, node_list[index + 1])
        
        if node.type == "NUMBER" or node.type == "VARIABLE":
            prev_op = node_list[index - 1]
            next_op = node_list[index + 1]
            if next_op.prec > prev_op.prec:
                prec_r_g_l(node, prev_op, next_op)
            else:
                prec_l_g_r(node, prev_op, next_op)
         
def double_neg(node: tree_node, next: tree_node):
    del next
    node.type = "PLUS"
    node.value = "+"
    
def prec_r_g_l(node: tree_node, prev_op: tree_node, next_op: tree_node):
    next_op.left_child = node
    node.parent = next_op
    if prev_op.type != "DUMMY":
        prev_op.right_child = next_op
        next_op.parent = prev_op
        
        
def prec_l_g_r(node: tree_node, prev_op: tree_node, next_op: tree_node):
    prev_op.right_child = node
    node.parent = prev_op
    
    if next_op.type != "DUMMY":
        while prev_op.parent is not None:
            if prev_op.parent.prec < next_op.prec:
                break
            prev_op = prev_op.parent
        if prev_op.parent is not None:
            prev_op.parent.right_child = next_op
            next_op.parent = prev_op.parent
        next_op.left_child = prev_op
        prev_op.parent = next_op
        
        
        


def get_prec(type: str) -> int:
    prec = 0
    if type == "PLUS" or type == "MINUS":
        prec = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        prec = 2
    elif type == "EXPONENT":
        prec = 3
    return prec

def create_tree_list(token_list: List[token]):
    node_list: List[tree_node] = []
    global_prec = 0
    for token in token_list:
        if token.type == "LPAREN":
            global_prec += 4
        elif token.type == "RPAREN":
            global_prec -= 4
        else:
            new_node = tree_node(token.type, token.value, get_prec(token.type) + \
                global_prec)
            node_list.append(new_node)
    return node_list

def link_nodes(parent: tree_node, left: tree_node | None = None, \
    right: tree_node | None = None):
    
    parent.left_child = left or parent.left_child
    parent.right_child = right or parent.right_child
    
    if right is not None:
        right.parent = parent
    if left is not None:
        left.parent = parent
        
        
        
def create_neg_one():
    minus = tree_node("MINUS", "-", 10)
    mult = tree_node("MULTIPLICATION", "*", 10)
    
    link_nodes(minus, tree_node("NUMBER", "0", 0), tree_node("NUMBER", "1", 0))
    
    link_nodes(mult, minus)
    
    return mult

def create_neg():
    # Create a tree that represents -1 * n.
    minus = tree_node("MINUS", "-", 10)
    mult = tree_node("MULTIPLICATION", "*", 10)
    
    link_nodes(minus, tree_node("NUMBER", "0", 0), tree_node("NUMBER", "1", 0))
    
    link_nodes(mult, minus, tree_node("DUMMY", "n", 0))
    
    return mult