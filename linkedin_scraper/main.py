from openpyxl import load_workbook
from scrape import get_contacts

data_file = 'linkedin_scraper/contacts.xlsx'

wb = load_workbook(data_file, data_only=True)
ws = wb['Sheet1']

# Delete all Rows other than Headers
while (ws.max_row > 1):
    ws.delete_rows(2)

# Scrape and Append Rows
for contact in get_contacts():
    ws.append([contact[0],contact[1]])

wb.save(filename=data_file)
