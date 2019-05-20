from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

	# Setup anything we need before the test.
	def setUp(self):
		# Get a webdriver of Firefox.
		self.browser = webdriver.Firefox()
		# Ask selenium wait 3 three seconds to do anything.
		self.browser.implicitly_wait(3)
	
	# After the test, clean anything we don't need anymore.
	def tearDown(self):
		# Close the webdriver.
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
	
	# First testcase we need. It should start with 'test-' and the testcase.
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Open the page.
		self.browser.get('http://localhost:8000')

		# Check the browser's title.
		self.assertIn('To-Do', self.browser.title)

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')

		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)

		time.sleep(1)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		time.sleep(1)

		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		self.fail('Finish the test!')

