from typing import List
from .tree_node import tree_node
from .token import token
from .token_maker import tokenize
from .tree_maker import create_tree, create_tree_list
  
            

    

def create_eq(eq: str) -> tree_node:
    """Create an equation that can be evaluated.
    :param eq: The equation (In terms of a single variable) to be created
    :type eq: str
    :returns: A node within the equation. Use this node to evaluate."""
    token_seq = tokenize(eq)
    root = parse(token_seq)
    if root is None:
        raise TypeError("Root node not found.")
    return(root)


def parse(token_list: List[token]):
    rootNode = None
    treeNodeList = create_tree_list(token_list)
    create_tree(treeNodeList)
    rootNode = findRoot(treeNodeList)
    return rootNode


def findRoot(treeNodeList):
    rootNode = None
    for node in treeNodeList:
        if (node.parent is not None and node.parent.type == "DUMMY") or \
            (node.parent is None and node.type != "DUMMY"):
            rootNode = node
            break
    return rootNode
            
