import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("test tag", "test value", ["obj1", "obj2"], {"key": "value"})
        node2 = HTMLNode("test tag", "test value", ["obj1", "obj2"], {"key": "value2"})
        self.assertEqual(node.props_to_html(), 'test tag test value')
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()