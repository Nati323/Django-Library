from django import forms
from .models import Book, Customer, Loan
# from django.db.models import QuerySet





class CreateCustomerForm(forms.Form):
    name  = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=21)


    # Tell 'em to which model he relates to
    class Meta:
        model = Customer


class CreateBookForm(forms.Form):
    name     = forms.CharField(label='Book name', max_length=100)
    in_stock = forms.IntegerField(label='Books In Stock')


    # Assign the form to the related model
    class Meta:
        model = Book
    #     fields = ('book_name', 'created_at_date')


class CreateLoanForm(forms.Form):
    pass
    # book_name   = forms.CharField(label='book name', max_length=100)


    # Assign the form to the related model
    class Meta:
        model = Loan
    #     fields = ('book_name', 'created_at_date')
