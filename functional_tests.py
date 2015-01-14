from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # My bro Sten here heard of this awsome to-do app
        # He is entering its webpage to check it out
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention
        # to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        self.fail('Finish the test!')

        # He is invited to enter To-Do item stright away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # He types "Buy milk!" into text box
        # When he hits enter the page updates, and now the
        # page lists: "1. Buy milk! " as an item in a to-do list
        inputbox.send_keys('Buy milk!!! ')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy milk!!!' for row in rows))

        # There is still a test mox inviting him to add another item
        # He enters "Learn to code" and presses enter again
        self.fail('Finish the test')

        # The page updates and now lists both items

        # He wonders if the site remembers his items and sees
        # that it generates a unique url for him

        # He visits that URL and sees that everything is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
