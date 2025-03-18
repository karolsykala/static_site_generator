class HTMLnode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise notImplementedError()
    def props_to_html(self):
        return f'href: {self.props["href"]} target: "{self.props["target"]}"'



katze = HTMLnode("uwu", "daddy", "nya", {
    "href": "https://www.google.com",
    "target": "_blank",
}
)

print(katze.props)

print(katze.props_to_html())



























