class KeepassEntry():
    def __init__(self, entry):
        self.title = "?"
        self.url = ""
        self.notes = ""
        self.username = ""
        self.password = ""
        self.tags = []
        if entry.get("Tags"):
            self.tags = entry["Tags"].split(";")

        for keyValue in entry["String"]:
            key = keyValue["Key"]
            val = keyValue["Value"]
            if key == "Title" and val:
                self.title = val
            elif key == "URL" and val:
                self.url = val
            elif key == "Notes" and val:
                self.notes = val
            elif key == "UserName" and val:
                self.username = val
            elif key == "Password" and val:
                self.password = val.get("#text", "")

    def has_any_tags(self, tags):
        for tag in tags:
            if tag in self.tags:
                return True
        return False

    def __str__(self):
        return f"KeepassEntry(title={self.title}, u={self.username}, p={self.password}, url={self.url})"
