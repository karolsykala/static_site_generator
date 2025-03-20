import unittest

from htmlnode import HTMLNode


class testhtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("uwu", "daddy", "nya", {
            "href": "https://www.google.com",
            "target": "_blank"
        })
        node2 = HTMLNode("uwu", "daddy", "nya", {
            "href": "https://www.google.com",
            "target": "_blank"
        })
        node3 = HTMLNode("uwu", "daddy", "nya", {
            "href": "https://www.kittycat.com",
            "target": "_blank"
        })

        self.assertEqual(node, node2)
        self.assertEqual(node, HTMLNode(tag="uwu", value="daddy", children="nya", props={'href': 'https://www.google.com', 'target': '_blank'}))
        self.assertEqual(node.props, {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), 'href: https://www.google.com target: "_blank"')
    def test_not_eq(self):
        node = HTMLNode("uwu", "daddy", "nya", {
            "href": "https://www.google.com",
            "target": "_blank"
        })
        node2 = HTMLNode("uwu", "daddy", "nya", {
            "href": "https://www.kittycat.com",
            "target": "_blank"
        })
        
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
