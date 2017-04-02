"""
This is the file that contains your dicision tree
"""


class DTreeNode:
    """
    Your Node Class for your dicision tree
    """
    
    def __init__(self, key, data=None):
        """
        I am allowing these to be public to manipulate them easy
        """
        self.key = key      
        self.data = data
        self.class = None
        self.edges = None #A dictionary storing the reference to children
            

class MyDecisionTree:
    """
    Will contain your deicision tree algorithm
    """
    
    def __init__(self):
        self.__myRoot = None
        self.__maxHeight = -1
        self.__minHeight = -1


    def train(self, xData, yData, maxDepth):
        """
        External interface for building the tree
        """
        pass


    def eval(self, xData):
        """
        External interface for evaluating the tree (Predicting)
        """
        pass


    def _entropy(self, xData, xMap, col):
        """
        Will be used to calculate the entropy of column (col-relative to xData)
        xData is a 2D Python list
        xMap is a dictionary that maps the current column number to the original
        returns a list of unique elements in the col of xData and entropy of column
        """
        pass

    def _stripRowCol(self, xData, yData, col):
        """
        Will strip the column and rows related to the unique elements in col.
        returns a list of 2DLists.  One for each unique element.
        """
        pass
    
    def __recursiveBuild(self, root, xData, xMap,  yData, currentDepth, maxDepth):
        """
        Where you really will build the tree
        root - of the current subtree (may not be used)
        xData - 2D Python List of attributes
        xMap - Dictionary mapping current rows to those in the original 
        yData - Output
        currentDepth - How many times we have already recursed
        maxDepth - how many level the tree will have at most
        """
        pass

    def _walk(self, root, xData, xMap):
        """
        Walks the tree 
        returns the most likely ydata classifier
        """
        pass

def testMyDecisionTree():
    """
    Used for your testing
    """
    pass


if __name__ == "__main__":
    testMyDecisionTree()
