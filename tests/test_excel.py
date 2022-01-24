import os

from openpyxl import load_workbook
from linkedin_scraper.excel import Excel

# When given filename that doesn't exist, Excel creates a new one
def test_create_new_file():
    filename = 'newfile.xlsx'
    workbook = Excel(filename)
    assert os.path.exists(filename)
    os.remove(filename)

# When creating new file, Excel creates header row
def test_create_header_row():
    filename = 'newfile.xlsx'
    workbook = Excel(filename)
    sheet = workbook.wb.active
    assert sheet.cell(row=1, column=1).value == 'Name'
    assert sheet.cell(row=1, column=2).value == 'Email'
    assert sheet.max_row == 1
    assert sheet.max_column == 2
    os.remove(filename)