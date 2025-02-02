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

seks = HTMLNode('uwu', 'nya', 'arf', {"sex": "yes"})


print(seks.__repr__())

class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value, children=None)
    
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