import json

class HtmlNode:
    def __init__(self, tag:str) -> None:
        self.tag = tag
        self.attributes = {}
        self.children = []
        self.text = {}
        self.itemsIndex = 0

    def add_child(self, child):
        self.children.insert(0, child)
        self.itemsIndex += 1

    def add_text(self, text):
        self.text[self.itemsIndex] = text
        self.itemsIndex += 1

    def get_dom(self):
        return {
            "tag": self.tag,
            "attributes": {i:self.attributes[i] for i in self.attributes},
            "text": {i:self.text[i] for i in self.text},
            "children":[i.get_dom() for i in self.children]
        }
    
    def get_dom_as_json(self):
        return json.dumps(self.get_dom(), indent='\t')
    
    def as_html(self, tab_level:int = 0):
        data = ('\t'*tab_level) + f'<{self.tag}'
        attrs = [(i if not self.attributes[i] else f'{i}="{self.attributes[i]}"') for i in self.attributes]
        attrs_string = ''.join([f" {i}" for i in attrs])
        data += attrs_string
        if self.itemsIndex > 0:
            data += '>\n'
            for i in range(self.itemsIndex):
                if i in self.text:
                    data += self.text[i] + '\n'
                else:
                    data += self.children.pop().as_html(tab_level + 1)
            data += f'</{self.tag}>'
        else:
            data += '/>\n'
        return data
    
    def walk(self):
        yield self
        for child in self.children:
            for sub_child in child.walk():
                yield sub_child