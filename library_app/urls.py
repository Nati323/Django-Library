from django.urls import path
from .           import views

urlpatterns = [
    path('',                          views.IndexView.as_view(),       name='index'),

    path('customers/',                views.CustomersList.as_view(),   name='customers_list'),
    path('customers/create/',         views.CreateCustomer.as_view(),  name='create_customer'),
    path('customers/<int:pk>/',       views.CustomerDetails.as_view(), name='customer_details'),
    path('customers/<int:pk>/delete/', views.DeleteCustomer.as_view(),  name='delete_customer'),
    
    path('books/',                    views.BooksList.as_view(),       name='books_list'),
    path('books/create/',             views.CreateBook.as_view(),      name='create_book'),
    path('books/<int:pk>/',           views.BookDetails.as_view(),     name='book_details'),
    path('books/<int:pk>/delete/',     views.DeleteBook.as_view(),      name='delete_book'),
    
    path('loans/',                    views.LoansList.as_view(),       name='loans_list'),
    path('loans/create/',             views.CreateLoan.as_view(),      name='create_loan'),
    path('loans/<int:pk>/details/',   views.LoanDetails.as_view(),     name='loan_details'),
    path('loans/<int:pk>/delete/',     views.Deleteloan.as_view(),      name='delete_loan'),

    path('logout/',     views.Logout.as_view(),      name='logout'),
]