from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending/'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  #chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_video_divs(driver):
  driver.get(YOUTUBE_TRENDING_URL)
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  time.sleep(1)
  video_divs = driver.find_elements(by=By.TAG_NAME,value=VIDEO_DIV_TAG)
  return video_divs



if __name__ == '__main__':
  driver = get_driver()
  videos = get_video_divs(driver)
  #title,url,thumbnailurl,views,uploaded,desc.
  
  title = [video.find_element(by=By.ID,value='video-title').text for video in videos]
  print(title)
