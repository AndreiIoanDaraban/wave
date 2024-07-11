import unittest
import json
from ui_ext import _clean, boxes, box

class TestUIExt(unittest.TestCase):


    def test_boxes(self):
        self.assertEqual(boxes('zone1', 'zone2'), json.dumps(('zone1', 'zone2')))
        self.assertEqual(boxes(), json.dumps(()))

    def test_box(self):
        # Test with minimal args
        self.assertEqual(box('zone1'), json.dumps({'zone': 'zone1'}))
        # Test with all args
        self.assertEqual(box('zone1', 1, '2', '100px', '200px'), json.dumps({'zone': 'zone1', 'order': 1, 'size': '2', 'width': '100px', 'height': '200px'}))
        # Test with int size
        self.assertEqual(box('zone1', size=3), json.dumps({'zone': 'zone1', 'size': '3'}))
        # Test with invalid size
        with self.assertRaises(ValueError):
            box('zone1', size=3.5)

if __name__ == '__main__':
    unittest.main()
