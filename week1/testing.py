import unittest
import unittest.mock
from stack import Stack

class TestStack(unittest.TestCase):
    """ """

    def setUp(self) -> None:
        self.stack = Stack()


    def test_push_add_to_stack(self):
        """ """
       
        self.stack.push(0)
        self.stack.push(0)
        self.assertEqual(self.stack.__top , 2)
