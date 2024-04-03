from django.shortcuts import render

finches = [
    {'name': 'Tweety', 'color': 'yellow', 'age': 5},
    {'name': 'Raspberry', 'color': 'red', 'age': 7},
    {'name': 'Dinah', 'color': 'blue', 'age': 4}
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })