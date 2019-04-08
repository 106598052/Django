from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

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

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			ant(row.text == '		: Buy peacock feathers' for row in rows)
		)

		self.fail('Finish the test')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
