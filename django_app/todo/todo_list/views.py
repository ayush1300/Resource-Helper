from django.core import paginator
from django.shortcuts import render, redirect
from .models import List, ComponentList
from .forms import ListForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            # messages.success(request, ('Item has been added to the List!'))
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    # messages.success(request, ("Item has been deleted"))
    return redirect("home")


def delete2(request, componentlist_id, list_id):
    item = ComponentList.objects.get(pk=componentlist_id)
    item.delete()
    # messages.success(request, ("Item has been deleted"))
    return redirect("http://localhost:8000/component/"+list_id)


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect("home")


def uncross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect("home")


def edit(request, componentlist_id, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        componentitem = ComponentList.objects.get(pk=componentlist_id)
        data = request.POST

        componentitem.topic = data['topic']
        componentitem.description = data['description']
        componentitem.link = data['link']
        componentitem.save()

        all_items = ComponentList.objects.filter(list=item)
        paginator = Paginator(all_items, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        list_name = item.item
        return render(request, 'component.html', {
            'all_items': all_items,
            'page_obj': page_obj,
            'list_id': list_id,
            'list_name': list_name
        })

    else:
        item = List.objects.get(pk=list_id)
        componentitem = ComponentList.objects.get(pk=componentlist_id)
        return render(request, "edit.html", {'componentitem': componentitem})


def component(request, list_id):

    item1 = List.objects.get(pk=list_id)

    if request.method == 'POST':

        data = request.POST
        a = ComponentList()
        a.list = item1
        a.topic = data['topic']
        a.description = data['description']
        a.link = data['link']

        a.save()

        all_items = ComponentList.objects.filter(list=item1)
        paginator = Paginator(all_items, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        list_name = item1.item
        return render(request, 'component.html', {
            'all_items': all_items,
            'page_obj': page_obj,
            'list_id': list_id,
            'list_name': list_name
        })

    else:
        all_items = ComponentList.objects.filter(list=item1)
        paginator = Paginator(all_items, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        list_name = item1.item
        return render(request, 'component.html', {
            'all_items': all_items,
            'page_obj': page_obj,
            'list_id': list_id,
            'list_name': list_name
        })
