from django.test import TestCase
from .models import Item

#Test todo items are created by default with a Done status of false

class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name = 'Test Todo Item')
        self.assertFalse(item.done)
        