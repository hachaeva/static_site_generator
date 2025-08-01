from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print (node)
    return

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href" : text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode('img', "", {"src" : text_node.url, "alt" : text_node.text})
    else:
        raise Exception("Invalid text type.")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    delimiter_dict = {"`" : TextType.CODE, "**" : TextType.BOLD, "_" : TextType.ITALIC}
    for node in old_nodes:
        if isinstance(node,TextNode) and delimiter in delimiter_dict:
            text_strings = node.text.split(delimiter)
            new_nodes.append(TextNode(text_strings[0]), TextType.Text)
            new_nodes.append(TextNode(text_strings[1]), delimiter_dict[delimiter])
            new_nodes.append(TextNode(text_strings[2]), TextType.Text)
        else: new_nodes.append(node)

def extract_markdown_images(text):
    return re.findall(r".*?!\[(\w+)\]\((.*?)\)", text) 

def extract_markdown_links(text):
    return re.findall(r".*?\[(\w+)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node,TextNode):
            images = extract_markdown_images(node.text)
            text_strings = re.split(r"!\[(\w+)\]\((.*?)\)")
            for i in range(len(text_strings)):
                if len(text_strings[i]) > 0:
                    new_nodes.append(TextNode(text_strings[i]))
                if i < len(images):
                    new_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
                
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node,TextNode):
            links = extract_markdown_links(node.text)
            text_strings = re.split(r"\[(\w+)\]\((.*?)\)")
            for i in range(len(text_strings)):
                if len(text_strings[i]) > 0:
                    new_nodes.append(TextNode(text_strings[i]))
                if i < len(links):
                    new_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]))

if __name__ == "__main__":
    main()

