class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (
                self.tag == other.tag,
                self.value == other.value,
                self.children == other.children,
                self.props == other.props,
            )

    def to_html(self):
        raise notImplementedError()

    def props_to_html(self):
        return f'href: {self.props["href"]} target: "{self.props["target"]}"'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

        if value is None:
            raise ValueError("Leafes need to have a value")

    def to_html(self):
        if (self.tag == None):
            return f"{self.value}"

        formattedProps = ""
        if self.props:
            for key, value in self.props.items():
                formattedProps += f' {key}="{value}"'

        return f"<{self.tag}{formattedProps}>{self.value}</{self.tag}>"


leafCat = LeafNode("p", "kitty cat uwu", props={"href": "www.google.com"})

katze = HTMLNode(
    "uwu",
    "daddy",
    "nya",
    {
        "href": "https://www.google.com",
        "target": "_blank",
    },
)

print("===")
print(katze)
print("===")
print(katze.props)
print("===")
print(katze.props_to_html())
print("===")
print(leafCat.to_html())
print("===")
print(leafCat.children)
