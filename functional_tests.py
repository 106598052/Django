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
		# It will fail anyway. We use it to finish the test.
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
