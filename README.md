# keepass2excel

Convert XML export from KeePass into Excel spreadsheet.



# Setup

Install Python (at least 3.something) and pip

Create a virtual env for dependencies to avoid polluting the global space:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install needed libraries: `pip install -r requirements.txt`



# How To Run

Run KeePass, load and open the `.kdbx` file you want to export.  Select File --> Export.  Click "KeePass XML", pick an output file, and click OK.

Run this script to read the XML export from KeePass above and create an Excel output file:

```bash
./keepass2excel keepass.xml keepass.xlsx --tags print
```

Use "`--tags print`" to filter out any items that don't have the "`print`" tag.
