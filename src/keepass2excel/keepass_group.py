from keepass2excel.keepass_entry import KeepassEntry

class KeepassGroup():
    def __init__(self, group_node, tags):
        self.name = group_node['Name']
        entries = group_node.get("Entry", [])
        if isinstance(entries, dict):
            entries = [ entries ]
        self.entries = []
        for e in entries:
            kpe = KeepassEntry(e)
            if not tags or kpe.has_any_tags(tags):
                self.entries.append(kpe)

        groups = group_node.get("Group", [])
        if isinstance(groups, dict):
            groups = [ groups ]
        self.groups = [ KeepassGroup(g, tags) for g in groups if g["Name"] != "Trash" ]
