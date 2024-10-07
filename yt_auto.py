import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YouTubeSearch():
    def __init__(self):
        service = Service(executable_path=r"C:/Users/yashk/Projects/webDriver/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def search_and_play(self, query):
        self.driver.get("https://www.youtube.com")
        
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'search_query'))
        )
        
        # Enter query in search box
        search_box.send_keys(query)

        search_button = self.driver.find_element(By.ID, 'search-icon-legacy')
        search_button.click() # hit enter

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]'))
        )

        first_video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        first_video.click() # play the first video that show up

        input("The video is now playing. You can close the browser when you are done.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1] 
        yt_search = YouTubeSearch()
        yt_search.search_and_play(query)
    else:
        print("Please provide a YouTube video topic to search.")
