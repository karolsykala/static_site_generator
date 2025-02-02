import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("test tag", "test value")
        node2 = HTMLNode("test tag", "test value", ["obj1", "obj2"], {"key": "value2"})
        self.assertEqual(node.props_to_html(), 'test tag test value')
        self.assertNotEqual(node, node2)

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "dupa", {"href": "www.pornhub.com"})
        self.assertEqual(node.to_html(), '<p href="www.pornhub.com">dupa</p>')

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            "div",
            [
        LeafNode("p", "Hello"),
        LeafNode("span", "World"),
            ])
        self.assertEqual(node.to_html(), '<div><p>Hello</p><span>World</span></div>')

        with self.assertRaises(ValueError) as context:
            node = ParentNode(
                "",
                [
                    LeafNode("p", "Hello"),
                    LeafNode("span", "World"),
                ]
            )
            node.to_html()
        self.assertEqual(str(context.exception), "Lacks Tag")

if __name__ == "__main__":
    unittest.main()