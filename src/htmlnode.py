class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return self.tag == other.tag, self.value == other.value, self.children == other.children, self.props==other.props
    def to_html(self):
        raise notImplementedError()
    def props_to_html(self):
        return f'href: {self.props["href"]} target: "{self.props["target"]}"'



katze = HTMLNode("uwu", "daddy", "nya", {
    "href": "https://www.google.com",
    "target": "_blank",
}
)

#print("===")
#print(katze)
#print("===")
#print(katze.props)
#print("===")
#print(katze.props_to_html())
#print("===")



























