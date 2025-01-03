import unittest

from divideAndConquer.nthPower.nthPower import nthPowerNaive, nthPowerOptimized


class TestNthPower(unittest.TestCase):

    def setUp(self):
        self.small_x = 10
        self.small_n = 3
        self.zero = 0
        self.one = 1
        self.n = 10
        self.large_x = 9
        self.large_n = 25

    def test_small_x(self):
        self.assertEqual(nthPowerNaive(self.small_x, self.small_n), 1000)
        self.assertEqual(nthPowerOptimized(self.small_x, self.small_n), 1000)

    def test_zero_x(self):
        self.assertEqual(nthPowerNaive(self.zero, self.n), 0)
        self.assertEqual(nthPowerOptimized(self.zero, self.n), 0)

    def test_one_x(self):
        self.assertEqual(nthPowerNaive(self.one, self.n), 1)
        self.assertEqual(nthPowerOptimized(self.one, self.n), 1)

    def test_large_x(self):
        self.assertEqual(nthPowerNaive(self.large_x, self.large_n), 717897987691852588770249)
        self.assertEqual(nthPowerOptimized(self.large_x, self.large_n), 717897987691852588770249)
