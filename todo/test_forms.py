from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        # create a form that has not been completed properly - test if Name Field is Required
        form = ItemForm({'name': ''})
        # Use Assert Fale to check this form is invalid
        self.assertFalse(form.is_valid())
        # Form should send a dictionary of errors. Use Assert In to check if there is a name key in the dictionary of errors
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # Test if Done Field is NOT Required

    def test_item_done_is_not_required(self):
        form = ItemForm({'name':'Test Todo Item with no DONE status'})
        self.assertTrue(form.is_valid())

    # Test only name and done are displayed

    def test_fields_are_explicit_in_metaclass(self):
        form = ItemForm()
        #create empty form - check form.meta.fields attribute is equal to a list with name and done in it - NOTHING ELSE should have been added to this form
        self.assertEqual(form.Meta.fields, ['name', 'done'])

        