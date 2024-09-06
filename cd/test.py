import cal
import unittest
class Testcal(unittest.TestCase):
   def test_add(self):
       self.assertEqual(cal.add(1,2),3)
       self.assertEqual(cal.add(2,-1),1)
       self.assertEqual(cal.add(-2, -1), -3)
   def test_sub(self):
       self.assertEqual(cal.sub(1, 2), -1)
       self.assertEqual(cal.sub(2, -1), 3)
       self.assertEqual(cal.sub(-2, -1), -1)
       self.assertEqual(cal.sub(5,2),3)
   def test_mul(self):
       self.assertEqual(cal.mul(1, 2), 2)
       self.assertEqual(cal.mul(2, 4), 8)
       self.assertEqual(cal.mul(-2, -1), 2)
   def test_div(self):
       self.assertEqual(cal.div(100, 2), 50)
       # with self.assertRaises(ZeroDivisionError):
       #     cal.div(12,0)
if __name__=='__main__':
    unittest.main()