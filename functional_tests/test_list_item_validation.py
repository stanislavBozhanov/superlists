from .base import FunctionaTest


class ItemValidationTest(FunctionaTest):

    def test_cannot_add_empty_items(self):
        # Anna goes to her homepage and accidently tries to submit
        # empty item. She hits enter on the empty input box
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # the page refreshes and there is a error saying
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # she tries some text and it works
        self.browser.find_element_by_id('id_new_item').send_keys('1: Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # she tries again blank and get similar Warning
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # and she corrects it by filling some text
        self.browser.find_element_by_id('id_new_item').send_keys('2: Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
