from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # My bro Sten here heard of this awsome to-do app
        # He is entering its webpage to check it out
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention
        # to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter To-Do item stright away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # He types "Buy milk!" into text box
        # When he hits enter the page updates,
        # he is taken to a new URL and now the
        # page lists: "1. Buy milk! " as an item in a to-do list
        inputbox.send_keys('Buy milk!!!')
        inputbox.send_keys(Keys.ENTER)
        sten_list_url = self.browser.current_url
        self.assertRegex(sten_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy milk!!!')

        # There is still a test mox inviting him to add another item
        # He enters "Learn to code" and presses enter again
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Learn to code')
        inputbox.send_keys(Keys.ENTER)

        # The page updates and now lists both items
        self.check_for_row_in_list_table('1: Buy milk!!!')
        self.check_for_row_in_list_table('2: Learn to code')

        # Now a new user, Anna, comes along the site.
        ## We will make a new browser session to make sure
        ## that no info of Sten's is coming through some Cookies etc #

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Anna visits the home page. There is no sign of Sten's list

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy milk!!!', page_text)
        self.assertNotIn('to code', page_text)

        # Anna starts a new list entering a new item. She is less intersing

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Write homework')
        inputbox.send_keys(Keys.ENTER)

        # Anna gets her own unique URL
        anna_list_url = self.browser.current_url
        self.assertRegex(anna_list_url, '/lists/.+')
        self.assertNotEqual(sten_list_url, anna_list_url)

        # Again there is no trace of Sten's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('to code', page_text)
        self.assertIn('Write homework', page_text)

        # Satisfied, they both go back to sleep
