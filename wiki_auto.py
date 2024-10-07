import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InfoRetriever():
    def __init__(self):
        service = Service(
            executable_path=r"C:/Users/yashk/Projects/webDriver/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        self.driver.get("https://www.wikipedia.org")
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )

        # enter query
        search = self.driver.find_element(By.ID, 'searchInput')
        search.clear()
        search.send_keys(query)
        search.submit()  # hit enter

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]'))
        )

        # First two paragraphs
        try:
            paragraphs = self.driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p')
            text_to_read = ""
            for i in range(min(2, len(paragraphs))):  # Get up to two paragraphs
                text_to_read += paragraphs[i].text + " "
            
            if not text_to_read.strip():
                text_to_read = "Sorry, no information found."

        except Exception as e:
            text_to_read = "Sorry, I couldn't retrieve the information. Error: " + str(e)
        
        self.driver.quit()
        
        print(text_to_read)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1] 
        assist = InfoRetriever()
        assist.get_info(query)
    else:
        print("No search topic provided.")
