# Code for binTreeNode class and treeInsert function acquired from http://pastebin.com/LXdWF0KW.
class binTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def treeInsert(tree, item):
    if tree==None:
        tree=binTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=binTreeNode(item)
            else:
                treeInsert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=binTreeNode(item)
            else:
                treeInsert(tree.right,item)
    return tree

def inOrder(tree):
    stack = []
    currentNode = tree
    finished = False

    while not finished:
        if currentNode is not None:
            stack.append(currentNode)
            currentNode = currentNode.left
        else:
            if len(stack) > 0:
                currentNode = stack.pop()
                print(currentNode.value)
                currentNode = currentNode.right
            else:
                finished = True

def treeSort(items):
    tree = treeInsert(None,items[0])
    for i in items[1:]:
        treeInsert(tree,i)
    inOrder(tree)

if __name__ == '__main__':
    lst = [254,6,10,1,5,2,3,4,11]
    treeSort(lst)