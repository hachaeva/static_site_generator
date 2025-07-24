import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

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

if __name__ == "__main__":
    unittest.main()
