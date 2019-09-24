import collections
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def main():
	channel_name = input("Enter a channel on Twitch that you want to see the logs of: ")
	user_name = input("Enter a user's logs that you want to check: ")
	website = "https://overrustlelogs.xyz/stalk?channel=" + channel_name + "&nick=" + user_name

	word = input("Enter a word that you want to search for (case-sensitive): ")
	word_list = []
	driver = webdriver.Chrome()  # Use .Chrome() for Chrome
	html = driver.get(website)
	months = driver.find_elements_by_css_selector('[id^=\"month\"]')
	if not months:
		return ("Invalid channel or user.")

	for month in months:
	    headers = month.find_element_by_class_name('card-header')
	    btn = headers.find_element_by_xpath("button")
	    btn.click()
	    time.sleep(1)

	time.sleep(2)
	for comment_string in months:
		body = comment_string.find_element_by_css_selector('[class^=\"card-body\"]')
		divider = body.find_element_by_tag_name('div')
		comment = divider.find_element_by_xpath('span')
		individual_posts = comment.text.split("\n")
		for post in individual_posts:
			split_post = post.split()
			word_list.extend(split_post[4:len(split_post)])

	word_count = collections.Counter(word_list)
	print("Total number of " + word + " = " + str(word_count[word]))

main()