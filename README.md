# keepass2excel

Convert XML export from KeePass into Excel spreadsheet


# How To Run

1. Install Python (at least 3.something)
1. Install needed libraries: `pip install xmldict openpyxl`
1. Run KeePass, load and open the `.kdbx` file you want to export.  I'm using MacPass here.
1. Select File --> Export To --> XML.  Save the file somewhere
1. Run this script: `~/keepass2excel ~/Downloads/keepass-export.xml ~/Downloads/keepass.xlsx --tags print`

This will create a new file with the same name and path as the input file, with extension `.xlsx`.


Use "`--tags print`" to filter out any items that don't have the "print" tag.
