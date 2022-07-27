from keepass2excel.keepass_entry import KeepassEntry

class KeepassGroup():
    def __init__(self, group_node):
        # print(f"Looking at raw node {group_node}")
        self.name = group_node['Name']
        entries = group_node.get("Entry", [])
        # print(f"Entries {entries}")
        if isinstance(entries, dict):
            self.entries = [ KeepassEntry(entries) ]
        else:
            self.entries = [ KeepassEntry(e) for e in entries ]

        groups = group_node.get("Group", [])
        if isinstance(groups, dict):
            groups = [ groups ]
        self.groups = [ KeepassGroup(g) for g in groups if g["Name"] != "Trash" ]
