from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm   #<--- Import your new user

def signup(request):
    # If user submitted the form (POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create the user in database
            return redirect('login')  # Send them to login page
        
    # If user is just visiting the page (GET)
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

