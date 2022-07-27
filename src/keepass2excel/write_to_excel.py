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
        "background": "154360"
    }
    excel.set_cell(1, 0, "Group",    **styles)
    excel.set_cell(1, 1, "Title",    **styles)
    excel.set_cell(1, 2, "Username", **styles)
    excel.set_cell(1, 3, "Password", **styles)
    excel.set_cell(1, 4, "URL",      **styles)
    excel.set_cell(1, 5, "Notes",    **styles)


def write_to_excel(kpg, excel, row=Sequence(2)):
    for entry in kpg.entries:
        r = row.val()
        notes = "; ".join(entry.notes.split("\n"))
        excel.set_cell(r, 0, kpg.name)
        excel.set_cell(r, 1, entry.title)
        excel.set_cell(r, 2, entry.username)
        excel.set_cell(r, 3, entry.password, font="Monaco", size=10)
        excel.set_cell(r, 4, entry.url)
        excel.set_cell(r, 5, notes)
        row.increment()

    for group in kpg.groups:
        write_to_excel(group, excel, row)
