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
        for key,value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def __eq__(object1,object2):
        if object1.tag == object2.tag and object1.value == object2.value and object1.children == object2.children and object1.props == object2.props:
            return True

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  