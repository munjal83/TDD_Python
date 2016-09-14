from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): #1

	def setUp(self): #2
		self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
		self.browser.implicitly_wait(3)
		
	def tearDown(self): #3
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self): #4
		#Tony heard about the new to-do list app.
		# He goes to check out the home page.
		self.browser.get('http://localhost:8000')

		# HE noices the page title an header mention to-do list
		self.assertIn('To-Do', self.browser.title) #5
		self.fail('Finish the test!') #6

		# He is invited to enter a to-do item staraight away

		# He type "learn TDD with python" (he's and avid learning)

		# When he hits enter, the page updates, and now the page lists
		# 1. "learn TDD with python" as an item in a to-do list

		# There is still a text box inviting him to add another item.
		# He enters "Search for relevant tutorials"

		# The page updates again, and now shows both items on his list

		# Tony wonders whether the site will remember his list. Then he sees that the site
		# has generated a unique URL for him --- there is some explanatory text that that 
		# effect

		# he visits that URL - his to-do list is still there.
		# Satisfied, he goes back to sleep

if __name__ == '__main__': #7
	unittest.main(warnings='ignore') #8