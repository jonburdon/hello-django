from django.test import TestCase
from .models import Item

#Test todo items are created by default with a Done status of false

class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name = 'Test Todo Item')
        self.assertFalse(item.done)
        
    def test_models_string_method_returns_name(self):
        # Create an item with a name and then confirm this name is returned when this item is rendered as a string.
        item = Item.objects.create(name = 'Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')