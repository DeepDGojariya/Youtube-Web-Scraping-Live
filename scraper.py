import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import smtplib

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending/'


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(
        'C:/Users/LENOVO/.wdm/drivers/chromedriver/win32/102.0.5005.61/chromedriver.exe',
        options=chrome_options)
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_video_divs(driver):
    driver.get(YOUTUBE_TRENDING_URL)
    VIDEO_DIV_TAG = 'ytd-video-renderer'
    time.sleep(1)
    video_divs = driver.find_elements(by=By.TAG_NAME, value=VIDEO_DIV_TAG)
    return video_divs


def store_video_information(videos):
    #title,url,thumbnailurl,views,uploaded,desc,channel.
    title = [
        video.find_element(by=By.ID, value='video-title').text.strip()
        for video in videos
    ]
    url = [
        video.find_element(by=By.ID, value='video-title').get_attribute('href')
        for video in videos
    ]
    thumbnail_url = [
        video.find_element(by=By.TAG_NAME, value='img').get_attribute('src')
        for video in videos
    ]
    channel_name = [
        video.find_element(by=By.CLASS_NAME,
                           value='ytd-channel-name').text.strip()
        for video in videos
    ]
    views = [
        video.find_element(by=By.ID, value='metadata-line').text.strip()
        for video in videos
    ]
    description = [
        video.find_element(by=By.ID, value='description-text').text.strip()
        for video in videos
    ]

    df = pd.DataFrame({
        'Video_title': title,
        'Video_url': url,
        'Thumbnail_url': thumbnail_url,
        'Channel_name': channel_name,
        'Views': views,
        'Description': description
    })
    df.to_csv('youtube-trending.csv', index=False)



if __name__ == '__main__':
    driver = get_driver()
    videos = get_video_divs(driver)
    store_video_information(videos)
    
