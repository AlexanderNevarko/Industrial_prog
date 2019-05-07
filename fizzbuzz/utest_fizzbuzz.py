import fizzbuzz as fb
import unittest


class FizzbuzzTest(unittest.TestCase):
    def test_big_num(self):
        seq = ['10000000000005000000000000000',
               '2000000000005000000000000001',
               '333333333333333333333333333333',
               '555555555555555505555555555555']
        ans = ['fizzbuzz',
               '2000000000005000000000000001',
               'fizz',
               'buzz']
        self.assertListEqual(fb.fizzbuzz(seq), ans)

    def test_neg_num(self):
        seq = ['-11110101010201102',
               '89123123125',
               '-15',
               '-07645',
               '-33333']
        ans = ['-11110101010201102',
               'buzz',
               'fizzbuzz',
               'buzz',
               'fizz']
        self.assertListEqual(fb.fizzbuzz(seq), ans)

    def test_bad_num(self):
        seq = ['0000098',
               '-9876545',
               '000000000005',
               '00000000000010000002',
               '-000011115',
               '00000033']
        ans = ['0000098',
               'buzz',
               'buzz',
               'fizz',
               'fizzbuzz',
               'fizz']
        self.assertListEqual(fb.fizzbuzz(seq), ans)

if __name__ == '__main__':
    unittest.main()