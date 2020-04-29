import unittest
import sys
sys.path.append("/testpython/RestAPI/src")  
import getdata

class GetdataTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(getdata.hello(), "Hello World!", "Should be get Hello World!")
   
if __name__ == '__main__':
    unittest.main()