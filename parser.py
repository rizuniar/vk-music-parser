import time
import json
import html
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup 

def scroll_to_bottom(driver, pause_time=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("That's end!")
            break

        last_height = new_height
        print("Keep scrolling...")

profile_path = "YOUR_PATH"

options = Options()

options.add_argument("-profile")
options.add_argument(profile_path)

driver = webdriver.Firefox(options=options)

driver.get("YOUR_AUDIO_PATH")
scroll_to_bottom(driver)

source_html = driver.page_source

soup = BeautifulSoup(source_html, 'lxml')
audio_rows = soup.find_all('div', class_='audio_row')

playlist = []

for row in audio_rows:
    data_audio_str = row.get('data-audio')
    
    if not data_audio_str:
        continue

    try:
        track_data = json.loads(data_audio_str)
        title = track_data[3]
        artist = track_data[4]

        clean_title = html.unescape(title)
        clean_artist = html.unescape(artist)

        playlist.append(f"{clean_artist} - {clean_title}")
    except (json.JSONDecodeError, IndexError) as e:
        continue

with open("vk_playlist.txt", "w", encoding="utf-8") as file:
    for track in playlist:
        print(track)
        file.write(track + "\n")

print(f"\nParsed tracks: {len(playlist)}")
driver.quit()
