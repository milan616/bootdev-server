from textnode import TextNode, TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        
        output = []

        for k, v in self.props.items():
            output.append(f'{k}="{v}"')

        return " ".join(output)

    def __repr__(self):
        return f"{self.tag}\n{self.value}\n{self.children}\n{self.props_to_html()}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return value

        output = ""
        props = self.props_to_html()

        if props == "":
            output = f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            output = f"<{self.tag} {props}>{self.value}</{self.tag}>"

        return output

    def __repr__(self):
        return f"{self.tag}\n{self.value}\n{self.props_to_html()}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.children is None:
            raise ValueError("Missing children")

        start = f"<{self.tag}>"
        end = f"</{self.tag}>"

        contents = ""

        for child in self.children:
            contents = contents + child.to_html()

        return start + contents + end

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url,})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url,"alt":text_node.text,})
