from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo_list(request):
# create a query variable called items which will pull all the items from the database
    items = Item.objects.all()
# create a varable called context will be a dictionary containing all the data we just requested
    context = {
        'items': items
    }
# ensure this is passed to the render function to html can access it
    return render(request, 'todo/todo_list.html', context)

def add_item(request):
    return render(request, 'todo/add_item.html')
