This is a scraper to get the name and email address from all of your LinkedIn connections.

This project uses poetry so navigate to the project directory and run "poetry init". To run the scraper you will need to create a .env file and put two variables in it as shown below.

| LINKEDIN_USERNAME=your_username_here
| LINKEDIN_PASSWORD=your_password_here
| 
You will also need to create a contacts.xlsx file with the headers Name and Email in A1 and B1 respectively. This file will need to be located in the linkedin_scraper directory with the python files.

In future iterations, I will add functionality where the program creates the excel file if it does not already exist.

Finally, to run just use './scrape' from the parent directory, 'linkedin-scraper'.