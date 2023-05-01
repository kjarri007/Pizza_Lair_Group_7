from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here
def register(request):
    # Could be either a POST or GET request!

    # If it's a POST request, gather the data from the HTTP body in a form variable,
    # check if its valid, if it is then store it and redirect the user to the login screen.
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")

    # If it's a GET request, then send a render request to the 'register.html' file and send
    # Django built-in form as context.
    return render(request, "user/register.html", context={"form": UserCreationForm()})
