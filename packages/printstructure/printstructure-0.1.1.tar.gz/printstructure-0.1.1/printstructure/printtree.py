# class Node:
#     def __init__(self, val = None, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right


class Tree:
    def __init__(self, node):
        self._check_node(node)
        self.node = node

    def print_tree(self):
        lines, *_ = self._generate_tree()
        for line in lines:
            print(line)

    def _generate_tree(self, node=None):
        if not node:
            node = self.node

        if node.left is None and node.right is None:
            line = str(node.val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        elif node.right is None:
            self._check_node(node.left)
            lines, n, p, x = self._generate_tree(node.left)
            s = str(node.val)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        elif node.left is None:
            self._check_node(node.right)
            lines, n, p, x = self._generate_tree(node.right)
            s = str(node.val)
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        else:
            self._check_node(node.left)
            left, n, p, x = self._generate_tree(node.left)
            self._check_node(node.right)
            right, m, q, y = self._generate_tree(node.right)
            s = str(node.val)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
            second_line = (
                x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
            )
            if p < q:
                left += [n * " "] * (q - p)
            elif q < p:
                right += [m * " "] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [
                a + u * " " + b for a, b in zipped_lines
            ]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

    def _check_node(self, node):
        if (not hasattr(node, "left")) or (not hasattr(node, "right")):
            raise AttributeError(
                "invalid node of binary tree, a node must has attributes 'left' and 'right'"
            )
