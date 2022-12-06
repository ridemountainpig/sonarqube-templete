import pytest
from selenium import webdriver
import unittest
import os
import sys
import pytest
import time


class BmiFunctionalTests(unittest.TestCase):

	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--no-sandbox')
		self.driver = webdriver.Chrome(os.path.join(os.environ["ChromeWebDriver"], 'chromedriver.exe'), options=options)
		self.driver.implicitly_wait(300)

	def test_selenium(self):
		webAppUrl = pytest.config.getoption('webAppUrl')
		start_timestamp = time.time()
		end_timestamp = start_timestamp + 60*10
		while True:
			try:
				response = self.driver.get(webAppUrl)
				
				height = self.driver.find_element_by_id("id_height")
				weight = self.driver.find_element_by_id("id_weight")

				height.send_keys('1.7')
				weight.send_keys('60')
				weight.submit()

				time.sleep(1)
				bmi = self.driver.find_element_by_id("bmi")

				self.assertEqual("20.76", bmi.text)
				break
			except Exception as e:
				print('"##vso[task.logissue type=error;]Test test_selenium failed with error: ' + str(e))
				current_timestamp = time.time()
				if(current_timestamp > end_timestamp):
					raise
				time.sleep(5)

	def tearDown(self):
		try:
			self.driver.quit()
		except Exception as e:
			print('tearDown.Error occurred while trying to close the selenium chrome driver: ' + str(e))
