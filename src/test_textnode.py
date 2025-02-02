import unittest

from textnode import TextNode, TextType
from htmlnode import *
from text_to_html import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a different Text node", TextType.BOLD, "www.google.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node2, node3)

class TestTextToHTMLConversion(unittest.TestCase):
    def test_eq(self):
        text_node = TextNode("Hello uwu", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello uwu"
        assert html_node.props == None

if __name__ == "__main__":
    unittest.main()