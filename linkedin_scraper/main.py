from .scrape import Scraper
from .excel import Excel

def main():
    workbook = Excel('contacts.xlsx')

    contacts = Scraper().get_contacts()

    if contacts:
        workbook.clear_sheet()
        workbook.write_contacts(contacts)
    else:
        raise NoConnectionsError