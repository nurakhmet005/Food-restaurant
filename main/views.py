from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReserveForm


# Create your views here.
def index(request):
    form = ReserveForm()
    error = ""

    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма заполнена неверно"
    
    data = {
        "form":form,
        "error": error
    }

    return render(request, "main/index.html", data)