import unittest
from dynamicProgramming.matrixChainMultiplication.matrixChainMultiplication import MatrixChainMultiplication

class TestMatrixChainMultiplication(unittest.TestCase):

    def setUp(self):
        self.empty_p = []
        self.one_matrix = [2, 3]
        self.two_matrices = [2, 3, 4]
        self.p = [10, 100, 5, 50]
        self.other_p = [5, 12, 3, 10, 5, 40]

    def test_empty(self):
        matrixChain = MatrixChainMultiplication(self.empty_p)
        self.assertRaises(ValueError, matrixChain.getOptimalStructure)

    def test_one_matrix(self):
        matrixChain = MatrixChainMultiplication(self.one_matrix)
        result = "Minimum Scalar Multiplications: 0\n"
        result += "Optimal Parathenses: A1"
        self.assertEqual(matrixChain.getOptimalStructure(), result)

    def test_two_matrix(self):
        matrixChain = MatrixChainMultiplication(self.two_matrices)
        result = "Minimum Scalar Multiplications: 24\n"
        result += "Optimal Parathenses: (A1A2)"
        self.assertEqual(matrixChain.getOptimalStructure(), result)

    def test_p(self):
        matrixChain = MatrixChainMultiplication(self.p)
        result = "Minimum Scalar Multiplications: 7500\n"
        result += "Optimal Parathenses: ((A1A2)A3)"
        self.assertEqual(matrixChain.getOptimalStructure(), result)

    def test_other_p(self):
        matrixChain = MatrixChainMultiplication(self.other_p)
        result = "Minimum Scalar Multiplications: 1405\n"
        result += "Optimal Parathenses: (((A1A2)(A3A4))A5)"
        self.assertEqual(matrixChain.getOptimalStructure(), result)
        