# crud_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
# CREATE
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ItemForm()
    return render(request, 'crud_app/item_form.html', {'form': form})
# READ
def list_items(request):
    items = Item.objects.all()
    return render(request, 'crud_app/item_list.html', {'items': items})

def view_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'crud_app/item_detail.html', {'item': item})
# UPDATE
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'crud_app/item_form.html', {'form': form})
# DELETE
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list_items')
    return render(request, 'crud_app/item_confirm_delete.html', {'item': item})
