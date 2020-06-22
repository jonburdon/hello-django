from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
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

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form' : form
    }
    return render(request, 'todo/add_item.html', context)

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

#post handler
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')


# pre fill the form with data from the database using instance=item
# add form to the view
    form = ItemForm(instance=item)
    context = {
        'form' : form
    }
    return render(request, 'todo/edit_item.html', context)

def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # use not to flip the status of the boolean to the opposite of current
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')