from django.db import models

# Create your models here.
# class donar(models.Model):
#     donar_id=models.AutoField(primary_key=True)
#     donar_name=models.CharField(max_length=50)
#     donar_email=models.EmailField(unique=True)
#     donar_password=models.CharField(max_length=20)
#     donar_phone = models.IntegerField(null=True, blank=True)


class borrower(models.Model):
    borrower_id=models.AutoField(primary_key=True)
    borrower_name=models.CharField(max_length=50)
    borrower_email=models.EmailField(unique=True)
    borrower_password=models.CharField(max_length=20)
    borrower_phone= models.IntegerField()

# never delete this volunteer because user datas are stored in this model
class volunteer(models.Model):
    volunteer_id=models.AutoField(primary_key=True)
    volunteer_name=models.CharField(max_length=50)
    volunteer_email=models.EmailField(unique=True)
    volunteer_password=models.CharField(max_length=20)
    volunteer_phone= models.IntegerField()

class agriculture(models.Model):
    agri_id=models.AutoField(primary_key=True)
    # donar_id=models.ForeignKey(donar,on_delete=models.CASCADE)
    brief_desc=models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/')
    amount=models.IntegerField()

class education(models.Model):
    edu_id=models.AutoField(primary_key=True)
    # donar_id=models.ForeignKey(donar,on_delete=models.CASCADE)
    brief_desc=models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/')
    amount=models.IntegerField()

class foodandhealth(models.Model):
    food_id=models.AutoField(primary_key=True)
    # donar_id=models.ForeignKey(donar,on_delete=models.CASCADE)
    brief_desc=models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/')
    amount=models.IntegerField()
    
class smallenterprise(models.Model):
    enter_id=models.AutoField(primary_key=True)
    # donar_id=models.ForeignKey(donar,on_delete=models.CASCADE)
    brief_desc=models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/')
    amount=models.IntegerField()

class vehicles(models.Model):
    vehi_id=models.AutoField(primary_key=True)
    # donar_id=models.ForeignKey(donar,on_delete=models.CASCADE)
    brief_desc=models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/')
    amount=models.IntegerField()

class categories(models.Model):
    agri_id=models.ForeignKey(agriculture,on_delete=models.CASCADE)
    edu_id=models.ForeignKey(education,on_delete=models.CASCADE)
    food_id=models.ForeignKey(foodandhealth,on_delete=models.CASCADE)
    enter_id=models.ForeignKey(smallenterprise,on_delete=models.CASCADE)
    vehi_id=models.ForeignKey(vehicles,on_delete=models.CASCADE)


    

class BorrowModel(models.Model):
    id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    age=models.IntegerField()
    adhaar_number=models.IntegerField()
    category=models.CharField(max_length=50)
    borrower_img = models.ImageField(upload_to='images/')
    # borrow_amount=models.IntegerField()
    description=models.CharField(max_length=150)
    

