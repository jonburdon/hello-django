from django.test import TestCase
# Import Item so that CRUD operations can be used to create an item in the database, and then test this item id url exists
from .models import Item

#TESTING VIEWS
#We need to test there is a successful HTTP Response, use the proper templates, and that items can be added and toggled

# Test 1: We can get the to do list (the home page)
# Test 2: We can get the add item page
# Test 3: We can get the edit item page
# Test 4: We can add an item
# Test 5: We can delete an item using delete view
# Test 6: We can toggle an item using the toggle view

#inherit functionality from TestCase

class TestViews(TestCase):
    def test_get_todo_list(self):
        #Use http client fron django testing framework
        #Check response for loading home page is successful response ie 200
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        #Check the correct template is loaded
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item(self):
        # Need to add an example item id to the url
        item = Item.objects.create(name = 'Test Todo Item')
        # Use f string to insert the item id. These work like template literals.
        # When using f, anything in curly braces will be interpreted and turned in to part of the string
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post ('/add', {'name': 'Test Added Item'})
        # If item is created successfully, this view should redirect to home page, so test this:
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # Create and then delete and item
        item = Item.objects.create(name = 'Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        # check the redirect is correct
        self.assertRedirects(response, '/')
        # Check item is deleted by getting it using filter
        existing_items = Item.objects.filter(id=item.id)
        # Check existing items is in fact zero - it should be empty
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # Create an item with done status of True
        item = Item.objects.create(name = 'Test Todo Item', done=True)
        # Call the toggle url on the id of the above item
        response = self.client.get(f'/toggle/{item.id}')
        # Check the redirect is correct
        self.assertRedirects(response, '/')
        # Check done status has changed to false
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
