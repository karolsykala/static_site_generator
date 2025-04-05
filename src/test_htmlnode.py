import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class testhtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "uwu",
            "daddy",
            "nya",
            {"href": "https://www.google.com", "target": "_blank"},
        )
        node2 = HTMLNode(
            "uwu",
            "daddy",
            "nya",
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(node, node2)
        self.assertEqual(
            node,
            HTMLNode(
                tag="uwu",
                value="daddy",
                children="nya",
                props={"href": "https://www.google.com", "target": "_blank"},
            ),
        )
        self.assertEqual(
            node.props, {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), 'href: https://www.google.com target: "_blank"'
        )

    def test_not_eq(self):
        node = HTMLNode(
            "uwu",
            "daddy",
            "nya",
            {"href": "https://www.google.com", "target": "_blank"},
        )
        node2 = HTMLNode(
            "uwu",
            "daddy",
            "nya",
            {"href": "https://www.kittycat.com", "target": "_blank"},
        )

        self.assertNotEqual(node.__repr__(), node2.__repr__())

    def test_leaf_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
