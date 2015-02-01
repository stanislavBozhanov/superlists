from .base import FunctionaTest


class ItemValidationTest(FunctionaTest):

    def test_cannot_add_empty_items(self):
        # Anna goes to her homepage and accidently tries to submit
        # empty item. She hits enter on the empty input box
        # the page refreshes and there is a error saying
        # that list items cannot be blank

        # she tries some text and it works
        # she tries again blank and get similar Warning
        # and she corrects it by filling some text
        self.fail('write me!')
