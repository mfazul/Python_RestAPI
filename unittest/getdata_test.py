import unittest
import sys
sys.path.append("/testpython/RestAPI/src")  
import getdata
class getdataTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(getdata.hello(), "Hello World!", "Should be Hello World!")
   
if __name__ == '__main__':
    unittest.main()