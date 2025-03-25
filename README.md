****
**FiveM Server CFX ID Scraper**
****
This is a Python script that uses Selenium to scrape the top 10 FiveM servers from the FiveM Server List and saves their CFX IDs into a text file.
****
**Features**
****
- Automatically scrolls through the list of servers.
- Collects the top 10 servers' CFX IDs.
- Saves the CFX IDs into a .txt file for easy use.
****
**Requirements**
****
Before running the script, you'll need to install some dependencies.

Python 3.7+: Make sure you have Python installed on your system. You can download it from python.org.

Google Chrome: The script uses Chrome for web automation. You can download it from here.

Python Libraries:
``selenium``
``webdriver-manager``
****
**How To use**
****
Open setup.bat and after the dependencies are installed open the start.bat.
****
**Output**
****
The script will create a server_ids.txt file in the same directory as the script, containing the CFX IDs of the top 10 servers.
Example output:

``CFX IDs of the servers with the most players:
cf7a2c
cf48f2
...``
