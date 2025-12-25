from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaction    #<--- Import the Models
from .forms import TransactionForm   #<--- Import your new form 


@login_required
def home(request):
    #LOGIC: If the user clicked "Add" (POST request)
    if request.method =='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            tansaction = form.save(commit=False)  #<--- Pause saving
            tansaction.user = request.user
            tansaction.save()  #<--- Resume saving
            return redirect('home')  # Refresh the page to clear the form
    
    # LOGIC: If the user is just looking at the page (GET request)
    else:
        form = TransactionForm()
    
    # Fetch ALL transactions from the database
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    #CALCULATION LOGIC STARTS HERE
    total_income = transactions.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    current_balance = total_income - total_expense

    # Pack them into a box (Context) to send th the template
    context = {
        'transactions': transactions,
        'form': form,
        'total_income': total_income,     #<--- Sending these to HTML
        'total_expense': total_expense,
        'current_balance': current_balance
    }

    #4. Send the box with the HTML
    return render(request, 'home.html', context)

@login_required
def delete_transaction(request, transaction_id):
    # Find the specific transaction or show 404 error
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)

    # Delete it
    transaction.delete()

    # Go back to home
    return redirect('home')


