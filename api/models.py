from django.db import models

class User(models.Model):
  ACTIVE = 'A'
  INACTIVE = 'I'
  STATUS_CHOICES = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
  ]

  balance = models.DecimalField(decimal_places=2, default=10.00, max_digits=8)
  password = models.CharField(max_length=256)
  status = models.CharField(choices=STATUS_CHOICES, max_length=1)
  username = models.EmailField()


class Operation(models.Model):
  ADDITION = 'addition'
  DIVISION = 'division'
  MULTIPLICATION = 'multiplication'
  RANDOM_STRING = 'random_string'
  SQUARE_ROOT = 'square_root'
  SUBTRACTION = 'subtraction'

  TYPE_CHOICES = [
    (ADDITION, 'Addition'),
    (DIVISION, 'Division'),
    (MULTIPLICATION, 'Multiplication'),
    (RANDOM_STRING, 'Random String'),
    (SQUARE_ROOT, 'Square Root'),
    (SUBTRACTION, 'Subtraction'),
  ]

  cost = models.DecimalField(decimal_places=2, default=1.00, max_digits=3)
  type = models.CharField(choices=TYPE_CHOICES, max_length=14)


class Record(models.Model):
  amount = models.DecimalField(decimal_places=2, default=1.00, max_digits=3)
  date = models.DateTimeField(auto_now_add=True)
  deleted = models.BooleanField(default=False)
  operation_id = models.ForeignKey(Operation, db_column='operation_id', on_delete=models.PROTECT)
  operation_response = models.CharField(max_length=256)
  user_balance = models.DecimalField(decimal_places=2, max_digits=8)
  user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.PROTECT)
  
