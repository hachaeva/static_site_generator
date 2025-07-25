import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from main import text_node_to_html_node
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p", value="This is a text node")
        node2 = HTMLNode(tag="p", value="This is a text node")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = HTMLNode(value="This is a text node", props = {"href": "https://www.google.com"})
        node2 = HTMLNode(value="This is a text node", props = {"href": "https://www.firefox.com"})
        self.assertNotEqual(node, node2)

    def test_noteq2(self):
        node = HTMLNode(tag="h1", value="This is a text node")
        node2 = HTMLNode(tag="h2", value="This is a text node")
        self.assertNotEqual(node, node2)

    def test_noteq3(self):
        node = HTMLNode(value="This is a text node")
        node2 = HTMLNode(value="This is NOT a text node")
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),"<a href=\"https://www.google.com\">Click me!</a>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
