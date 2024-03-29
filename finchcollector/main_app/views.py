from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import SightingForm

# finches = [
#     { 'name': 'Tweety', 'breed': 'House', 'Latin': 'Haemorhous Mexicanus', 'age': 3 },
#     { 'name': 'Sachmo', 'breed': 'Purple', 'Latin': 'Haemorhous Purpureus', 'age': 2 }, 
#     { 'name': 'River', 'breed': 'American Gold',
#      'Latin': 'Spinus Tristis', 'age': 0 },
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html',{
        'finches': finches
    })
    
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'sighting_form': sighting_form,
    })
    
def add_sighting(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = SightingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)
    
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    # Special string pattern Django will use
    # success_url = '/finches/{finch_id}' <- what it may look like under the hood
    # Or if you wanted to redirect to the index page
    # success_url = '/finches' 
    
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'Latin', 'age']
    

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/all_finches'
    

    