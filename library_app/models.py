from datetime import timezone
import datetime
from datetime import date
from django.db import models
from faker import Faker # Used to fake data for easier testing
fake = Faker()
start_date = datetime.date(year=2015, month=1, day=1)



class Customer(models.Model):
    name    =  models.CharField(max_length=50,  default=fake.name())
    address =  models.CharField(max_length=200, default=fake.address())
    age     = models.PositiveIntegerField()
    # email     =  models.EmailField(default=None, blank=True)               # Allowing this field to be blank (None by default)
    # phone     =  models.CharField(max_length=20, default=None, blank=True) # Allowing this field to be blank (None by default)



class Book(models.Model):
    name         = models.CharField(max_length=200, default=fake.name())
    author       = models.CharField(max_length=200, default=fake.name())
    genre        = models.CharField(max_length=45)
    copies       = models.PositiveIntegerField(default=0)
    created_at   = models.DateTimeField('date published', auto_now_add=True)
    published_at = models.DateTimeField(default=fake.date_between(start_date=start_date, end_date='-5y'))

    class meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

    def was_published_recently(self):
        """
        Check if book was published recently
        """
        
        now = timezone.now()
        
        return now - datetime.timedelta(days=1) <= self.created_at <= now
    

    def does_contain_bad_word(self):
        """
        Check if a book contains any bad words init

        Returns True if the book contains any bad words (in it's entirety)

        Known bugs:
            - Doesn't return True if a word is surrounded by special characters | "(damn)"
            - Doesn't return True if a word has a special character at the end  | "damn!"
        """
        
        bad_words = ['damn', 'bad', 'very_bad', 'extremely_bad'] # 'bad', (for debugging)

        for book_word in self.name.split(' '):
            if book_word in bad_words:
                # Need to return true because it contains a bad word in the name
                # Should return True if functions properly
                return True
        
        # No bad words were detected in the book text
        # so return False after going through all of them

        return False
    
class Loan(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book_id     = models.ForeignKey(Book, on_delete=models.CASCADE)
    type_id     = models.CharField(max_length=1)
    loaned_at   = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)
