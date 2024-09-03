import unittest

class Math(unittest.TestCase):
    
    def test_int(self, x:int) -> int:
        self.assertEqual(type(x), int)
        return x