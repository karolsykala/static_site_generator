from textnode import TextNode, TextType

def main():
    newNode = TextNode("Twoja stara je banana", TextType.LINK, "https://www.wykop.pl")
    print(newNode)


if __name__ == '__main__':
    main()
