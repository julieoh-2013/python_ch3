from django.db import models

# Create your models here.


class Emaillist(models.Model): #테이블명
    #테이블 칼럼
    first_name = models.CharField(max_length=50) #varchar
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):#java tostring
        return'Emaillist(%s,%s,%s)' %(self.first_name, self.last_name,self.email)




