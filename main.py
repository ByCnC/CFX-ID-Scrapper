from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://servers.fivem.net/"

try:
    driver.get(url)
    time.sleep(5)

    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'AHTD5K9Y')]"))
    )

    server_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'AHTD5K9Y')]")

    top_server_ids = []
    for server in server_elements[:10]:
        try:
            server_name = server.text
            server_id = server.find_element(By.XPATH, ".//preceding-sibling::div//img").get_attribute("alt")
            top_server_ids.append((server_id, server_name))
        except:
            continue

    driver.quit()

    with open("server_ids.txt", "w") as file:
        file.write("CFX IDs of the servers with the most players:\n")
        for server_id, server_name in top_server_ids:
            file.write(f"{server_id}\n")

    print("CFX IDs have been saved to 'server_ids.txt'.")

except Exception as e:
    print(f"Error getting data: {e}")
    driver.quit()
