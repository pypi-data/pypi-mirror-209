from .printdp import DPTable
from .printtree import Tree


class PrintStructure:
    @staticmethod
    def print(data):
        if isinstance(data, list):
            dp = DPTable(data)

            dp.print_dp()
        else:
            tree = Tree(data)
            tree.print_tree()
