class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return f'{self.tag} {self.value}'
    
    def __repr__(self):
        return f'{self.tag}\n{self.value}\n{self.children}\n{self.props}'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        elif self.tag == None or not self.tag:
            return f'{self.value}'
        else:
            if self.props:
                props_str = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
                return f'<{self.tag} {props_str}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.tag or self.tag.strip() == "":
            raise ValueError("Lacks Tag")
        elif not self.children:
            raise ValueError("lacks Children")
        else:
            childHTML = "".join(child.to_html() for child in self.children)
            return f'<{self.tag}>{childHTML}</{self.tag}>'
        
