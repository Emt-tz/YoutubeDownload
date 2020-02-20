from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


class youtubedl:

	def getlink():
		url = str(input("Enter valid youtube url: "))

		if "https://www." in url:
			return url.replace("youtube", "youtubepp")

		else:

			url = "https://www." + url

			return url.replace("youtube", "youtubepp")

	def audio():
		#Downloading audio file
		x = youtubedl.getlink()
		print(x)
		browser = webdriver.Chrome('/home/emt/chromedriver')
		browser.maximize_window()
		browser.get(x)

		time.sleep(5)

		paste = browser.find_element_by_name('query')

		paste.send_keys(str(x))

		time.sleep(2)
		click = browser.find_element_by_xpath('//*[@id="btn-submit"]').click()
		time.sleep(2)

		audio_select = browser.find_element_by_xpath('//*[@id="result"]/div[1]/div[2]/ul/li[2]/a').click()

		select = browser.find_element_by_xpath('//*[@id="process_mp3_a"]').click()

		time.sleep(8)

		download = browser.find_element_by_xpath('//*[@id="dl-btns"]/a').click()



	def video():
		#Downloading a 360p video
		x = youtubedl.getlink()
		print(x)
		browser = webdriver.Chrome('/home/emt/chromedriver')
		browser.maximize_window()
		browser.get(x)

		time.sleep(5)
		
		paste = browser.find_element_by_name('query')

		paste.send_keys(str(x))

		time.sleep(2)
		click = browser.find_element_by_xpath('//*[@id="btn-submit"]').click()
		time.sleep(2)
		video = browser.find_element_by_xpath('//*[@id="mp4"]/table/tbody/tr[3]/td[3]/a').click()

		time.sleep(8)

		download = browser.find_element_by_xpath('//*[@id="dl-btns"]/a').click()

	def Begin():

		choice = int(input("1 for Audio and 2 for Video: "))

		if choice == 2:
			youtubedl.video()
		else:
			youtubedl.audio()

if __name__ == '__main__':
	youtubedl.Begin()
