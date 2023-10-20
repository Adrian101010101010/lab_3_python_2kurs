class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    sums = []

    def calculate_branch_sums(node, current_sum, is_left):
        if node is None:
            return

        if node.left is None and node.right is None and is_left:
            sums.append(current_sum + node.value)

        calculate_branch_sums(node.left, current_sum, True)
        calculate_branch_sums(node.right, current_sum, False)

    calculate_branch_sums(root, 0, False)
    return sum(sums)

