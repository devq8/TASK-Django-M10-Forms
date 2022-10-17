from ast import Try
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from stores import models
from .forms import StoreItemForm
from .models import StoreItem


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)


def index(request):

    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)

def create_store_item(request):
    form = StoreItemForm()

    if request.method == "POST":
        form = StoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")


    context = {
        "form": form,
    }


    return render (request, "create_store_item.html", context)

def update_store_item(request, item_id):
    store_item = StoreItem.objects.get(id=item_id)
    form = StoreItemForm(instance=store_item)
    context = {
        "store_item": store_item,
        "form": form,
    }
    if request.method == "POST":
        form = StoreItemForm(request.POST, instance=store_item)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")
    return render(request, "update_store_item.html", context)

def delete_store_item(request, item_id):
    try:
        store_item = StoreItem.objects.get(id=item_id)
    except:
        raise Http404
    
    store_item.delete()
    return redirect("store-item-list")