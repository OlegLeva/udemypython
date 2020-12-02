import unittest
import func_upper


class Test_class(unittest.TestCase):

    def test_name_up(self):
        name = 'Jack'
        result = func_upper.name_up(name)
        self.assertEqual(result, "JACK")


if __name__ == '__main__':
    unittest.main()
