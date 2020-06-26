from django.test import TestCase

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

#    def test_get_todo_list(self):

#    def test_get_todo_list(self):

#    def test_get_todo_list(self):

#    def test_get_todo_list(self):

#    def test_get_todo_list(self):