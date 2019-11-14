
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import logout
from .forms import LoginForm



def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect("index")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    return render(request, 'Cardgame/index.html', {'form': form})
    
def views_logout(request):
    logout(request)
    return redirect("index")



def playing(request):
    return render(request,'Cardgame/playing.html')