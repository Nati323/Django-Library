# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse#
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views import View
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
# from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin

from library_app.forms import CreateBookForm
from .models import Book, Loan
# from .forms import CreateBookForm


class IndexView(generic.View):
    """
    Perhaps have all of the available actions displayed in this page by category
    """

    def get(self, request):
        return render(request, 'library/index.html', status=200)


#
# Books
#

class BooksList(generic.ListView):
    template_name        =  'library/books_list.html'
    context_object_name  =  'books_list'

    def get_queryset(self):
        """
        Get all available books, order by their creation date
        """
        return Book.objects.order_by('-created_at')


class CreateBook(View):
    """
    Create a new book
    """
    # Using .split(" ") instead of just "in" so it won't just take words
    # that include the bad words (shityoo) but only the bad word itself (shit) as a whole
    def get(self, request):
        # Create a blank form and pass to template's context
        form = CreateBookForm()

        return render(request, 'library/create_book.html', {'form': form}, status = 200)

    def post(self, request):
        # Create a form instance and populate it with data from the request:
        form = CreateBookForm(request.POST)

        # process the data in form.cleaned_data as required
        if form.is_valid():

            book = Book(name=form.cleaned_data['name'], in_stock=form.cleaned_data['in_stock'], created_at=datetime.now())

            # Check if the book contains any bad words in it
            if book.does_contain_bad_word():
                return HttpResponse(f'Invalid Form Data! Includes a bad word in the book\'s name!', status = 400)

            # Insert new book to db
            book.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Your form data is invalid! Please return to the original form and re-enter valid data.')


class BookDetails(generic.DetailView):
    """
    Show the details of a specific book
    """
    model = Book
    template_name = 'library/book_details.html'
    


class DeleteBook(LoginRequiredMixin, View):
    """
    (!) No deletes for now, it's here for later... (!)

    Delete a book
    """
    pass


#
# Customers
#

class CustomersList(generic.ListView):
    """
    Show all customers
    """
    pass


class CreateCustomer(LoginRequiredMixin, View):
    """
    Create a new customer
    """
    pass
    # def get(self, request):
    #     # if a GET (or any other method) we'll create a blank form
    #     form = NewBookForm()

    #     return render(request, 'library/create_book.html', {'form': form}, status = 200)

    # def post(self, request):
    #     # create a form instance and populate it with data from the request:
    #     form = NewBookForm(request.POST)

    #     # process the data in form.cleaned_data as required
    #     if form.is_valid():

    #         book = Book(name=form.cleaned_data['book_name'], created_at=datetime.now())

    #         # Check if the book contains any bad words in it
    #         if book.does_contain_bad_word():
    #             return HttpResponse(f'Invalid Form Data! Includes a bad word in the book\'s name!', status = 400)

    #         # Insert new book to db
    #         book.save()

    #         return HttpResponseRedirect('/')
    #     else:
    #         return HttpResponse('Your form data is invalid! Please return to the original form and re-enter valid data.')


class CustomerDetails(LoginRequiredMixin, generic.DetailView):
    """
    Show the details of a specific customer
    """
    pass


class DeleteCustomer(LoginRequiredMixin, View):
    """
    (!) No deletes for now, it's here for later... (!)

    Delete a customer
    """
    pass


#
# Loans
#

class LoansList(generic.ListView):
    """
    Show all loans
    """
    pass


class CreateLoan(LoginRequiredMixin, View):
    """
    Create a new loan
    """
    pass


class LoanDetails(LoginRequiredMixin, generic.DetailView):
    """
    View all available loans and their details
    """
    pass


class Deleteloan(LoginRequiredMixin, View):
    """
    Delete a loan from the models
    """
    pass


class Logout(View):
    """
    Log the user out
    """
    pass