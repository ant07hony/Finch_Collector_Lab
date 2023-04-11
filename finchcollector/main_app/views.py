from django.shortcuts import render

finches = [
    { 'name': 'Tweety', 'breed': 'House', 'Latin': 'Haemorhous Mexicanus', 'age': 3 },
    { 'name': 'Sachmo', 'breed': 'Purple', 'Latin': 'Haemorhous Purpureus', 'age': 2 }, 
    { 'name': 'River', 'breed': 'American Gold',
     'Latin': 'Spinus Tristis', 'age': 0 },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html',{
        'finches': finches
    })
