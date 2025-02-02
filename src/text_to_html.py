from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(textNode):
    if textNode.text_type == TextType.TEXT:
        return LeafNode(None, textNode.text)
    elif textNode.text_type == TextType.BOLD:
        return LeafNode("b", textNode.text)
    elif textNode.text_type == TextType.ITALIC:
        return LeafNode("i", textNode.text)
    elif textNode.text_type == TextType.CODE:
        return LeafNode("code", textNode.text)
    elif textNode.text_type == TextType.LINK:
        return LeafNode("a", textNode.text, {"href": textNode.url})
    elif textNode.text_type == TextType.IMAGE:
        return LeafNode('img', "",{"src": textNode.url, "alt": textNode.text})
    else:
        raise Exception(f'Invalid text type: {textNode.text_type}')