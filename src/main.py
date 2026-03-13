from textnode import TextNode, TextType

def main():
    test = TextNode("test", TextType.LINK, "https://google.com")

    print(test)


main()
