import sys
sys.path.append("src")  # hack since this is a /script/ and the process needs src/ as a module root on the path

import argparse
import xmltodict
from keepass2excel.keepass_group import KeepassGroup
from keepass2excel.excel_file import ExcelFile
from write_to_excel import write_header, write_to_excel

def print_group(group, indent_level=0):
    print(f"{' ' * indent_level}Group {group.name}:")
    for entry in group.entries:
        print(f"{' ' * (indent_level + 4)}{entry.title}")
    for grp in group.groups:
        print_group(grp, indent_level + 4)


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("--toc", action="store_true")
    parser.add_argument("--tags", nargs="+")
    parser.add_argument("keepass_export_xml", type=argparse.FileType('r'))
    parser.add_argument("excel_output", type=argparse.FileType('wb'))
    return parser.parse_args()



args = parse_commandline()
excel = ExcelFile()
write_header(excel)

doc = xmltodict.parse(args.keepass_export_xml.read())
top_level_group = doc["KeePassFile"]["Root"]["Group"]
kpg = KeepassGroup(top_level_group, args.tags)

if args.toc:
    print_group(kpg)

write_to_excel(kpg, excel)
excel.set_column_widths([ 20, 40, 23, 30, 35, 80 ])
excel.save(args.excel_output)
