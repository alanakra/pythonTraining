import newList
import unittest

class TestNewList(unittest.TestCase):
    def test_new_list(self):
        self.assertCountEqual(newList.new_list(list1,list2), [25, 35, 40, 60, 90])

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

if __name__ == '__main__':
    unittest.main()