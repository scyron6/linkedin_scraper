from Scrape import Scraper
from Excel import Excel

workbook = Excel('contacts.xlsx')

contacts = Scraper().get_contacts()

if contacts:
    workbook.clear_sheet()
    workbook.write_contacts(contacts)
else:
    raise NoConnectionsError