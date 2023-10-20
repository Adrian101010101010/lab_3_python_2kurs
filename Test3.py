import unittest
from lab3 import BinaryTree
from lab3 import branch_sums


class TestFindLeftChild(unittest.TestCase):

    def test_LeftChild(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        result = branch_sums(root)
        self.assertEqual(result, 24)

    def test_LeftChild1(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.left.left = BinaryTree(15)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        result = branch_sums(root)
        self.assertEqual(result, 30)


if __name__ == '__main__':
    unittest.main()
