import algorythm as algo
import unittest


class AlgorythmTest(unittest.TestCase):
    def test_good1(self):
        table = algo.prepare_table('textfile.txt')
        self.assertEqual(algo.table_search(table, 1023, algo.hash_func, 'I'), True)

    def test_good2(self):
        table = algo.prepare_table('textfile.txt')
        self.assertEqual(algo.table_search(table, 1023, algo.hash_func, 'Gregor'), True)

    def test_bad1(self):
        table = algo.prepare_table('textfile.txt')
        self.assertEqual(algo.table_search(table, 1023, algo.hash_func, 'qwdasxqwd'), False)

    def test_bad2(self):
        table = algo.prepare_table('textfile.txt')
        self.assertEqual(algo.table_search(table, 1023, algo.hash_func, '__xasxk_ldkm'), False)


if __name__ == '__main__':
    unittest.main()