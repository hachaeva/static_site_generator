class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")
    
    def props_to_html(self):
        props_str = ""
        if self.props:
            for key,value in self.props.items():
                props_str += f' {key}="{value}"'
        return props_str
    
    def __eq__(object1,object2):
        if object1.tag == object2.tag and object1.value == object2.value and object1.children == object2.children and object1.props == object2.props:
            return True

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value)
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag)
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")
        if not self.children:
            raise ValueError("All parent nodes must have at least one child.")
        children_html_string = ""
        for child in self.children:
            children_html_string += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{children_html_string}</{self.tag}>"

        
