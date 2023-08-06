from .html import HtmlNode
from html.parser import HTMLParser


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack:list[HtmlNode] = []
        self.children:list[HtmlNode] = []
        self.text:list[str] = []
        self.last:HtmlNode = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = HtmlNode(tag)
        for l in attrs:
            node.attributes[l[0]] = l[1]
        self.stack.append(node)

    def handle_endtag(self, tag: str) -> None:
        node = self.stack.pop()
        children = []
        while node.tag != tag:
            children.append(node)
            node = self.stack.pop()
        for i in children:
            node.add_child(i)
        while len(self.text) > 0:
            node.add_text(self.text.pop())
        for child in self.children:
            node.add_child(child)
        self.children.clear()
        if len(self.stack) > 0:
            self.stack[-1].add_child(node)
        self.last = node

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = HtmlNode(tag)
        for a in attrs:
            node.attributes[a[0]] = a[1]
        self.children.append(node)

    def handle_data(self, data: str) -> None:
        if data.strip() != '':
            self.text.append(data)

    def parse(self, data:str) -> HtmlNode:
        self.feed(data)
        while len(self.stack) > 1:
            child = self.stack.pop()
            self.stack[-1].add_child(child)
        result = self.last if len(self.stack) == 0 else self.stack[0]
        return result
