from html.parser import HTMLParser


class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag =="a":
            for (attribute, value) in attrs:
                if attribute == "href":
                    if 'grp_mmbr_list' in value:
                        self.links.add(value)

                        
        return super().handle_starttag(tag, attrs)
                        
    def get_links(self):
        return self.links