class Sequence():
    def __init__(self, starting_val=0):
        self.num = starting_val

    def val(self):
        return self.num

    def increment(self):
        self.num += 1


def write_header(excel):
    styles = {
        "foreground": "FFFFFF",
        "bold": True,
        "background": "154360",
        "size": 9
    }
    excel.set_cell(1, 0, "Title",    **styles)
    excel.set_cell(1, 1, "Username", **styles)
    excel.set_cell(1, 2, "Password", **styles)
    excel.set_cell(1, 3, "Notes",    **styles)


def write_to_excel(kpg, excel, row=Sequence(2)):
    styles = {
        "size": 9
    }
    for entry in kpg.entries:
        r = row.val()

        formatted_parts = []
        if entry.url:
            formatted_parts.append(entry.url)
        if entry.notes:
            unwrapped_notes = "; ".join(entry.notes.split("\n"))
            formatted_parts.append(unwrapped_notes)
        if formatted_parts:
            notes = "\n".join(formatted_parts)
        else:
            notes = ""

        # excel.set_cell(r, 0, kpg.name)
        excel.set_cell(r, 0, entry.title, **styles)
        excel.set_cell(r, 1, entry.username, **styles)
        excel.set_cell(r, 2, entry.password, font="Monaco", size=8)
        excel.set_cell(r, 3, notes, **styles)
        row.increment()

    for group in kpg.groups:
        write_to_excel(group, excel, row)
