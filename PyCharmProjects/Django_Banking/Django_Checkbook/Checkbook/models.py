from django.db import models

# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    Accounts = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# creating the transaction class

# this list will be used as a choices box for the form
# deposit and withdrawal are placed twice because the first is for the database
# and the second one is for the form
#NOTE: these do not have to be the same name but know which position names which
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()

# NOTE: Whenver you add, delete, or modify changes in the models module
# be sure to migrate all changes by:
    # In the terminal, ensure your path leads to the manage.py file
    # --> python manage.py makemigrations
    # --> python manage.py migrate
































