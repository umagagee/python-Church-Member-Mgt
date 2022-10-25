from django.db import models

# Create your models here.

class Member(models.Model):
    gender=(('male','male'),('female','female'),('other','other'))

    level = (('Professor','Professor'),
    ('Masters','Masters'),('Degree','Degree'),
    ('High School','High School'),('Others','Others'))

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=100, null=True,choices=gender)
    birth_date = models.DateField(null=True)
    age = models.IntegerField(null=True)
    Occupation = models.CharField(max_length=100, null=True)
    education = models.CharField(max_length=100, null=True,choices=level)
    Address = models.CharField(max_length=100, null=True)
    date_join = models.DateField(null=True)
    date_created = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.first_name

class Payment(models.Model):
    catergory = (('Tithe','Tithe'),('Contribution','Contribution'),
    ('Collection','Collection'),('Dues','Dues'),
    ('Others','Others'))

    method = (('Cash','Cash'),('Cheque','Cheque'),
    ('Card','Card'),('Mobile Money','Mobile Money'),
    ('Others','Others'))

    member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(null=True)
    payment_cart = models.CharField(max_length=100, null=True, choices=catergory)
    payment_method = models.CharField(max_length=100, null=True, choices=method)
    date_paid = models.DateField(null=True)
    date_added = models.DateField(auto_now_add=True)



    



