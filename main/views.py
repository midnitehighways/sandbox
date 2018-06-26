# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from main.models import Part
from main.forms import PartForm, DeletePartForm

# Create your views here.

def index(request):
    my_list = [1, 2, 33, 5]
    my_string = 'hi there'
    context = {'my_list': my_list, 'hello': my_string, 'parts': Part.objects.all()}
    return render(request, 'index.html', context)

def parts(request):
    context = {'parts': Part.objects.all()}
    return render(request, 'parts.html', context)

def delete_part(request, pk):
    # if request.method == 'POST':
    #   part = get_object_or_404(Part, pk=pk)
    #   part.delete()
    #   return 
    
    # return render(request, 'parts.html', context)

    part = get_object_or_404(Part, pk=pk)
    part.delete()
    return redirect('parts')#render(request, 'parts.html', {})

def edit_part(request):
    return render(request, 'parts.html')

def add_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = form.cleaned_data['name']
            post.content = form.cleaned_data['content']
            post.pub_date = timezone.now()
            post.save()
            return redirect('parts')
    form = PartForm()
    return render(request, 'part_edit.html', {'form': form})
