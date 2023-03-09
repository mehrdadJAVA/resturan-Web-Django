from django.db import models
from django.contrib.auth.models import User



class registerModel(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self) :
        return str(self.user.id)



class loader(models.Model):
    name1 = models.CharField(max_length=100,blank=True,null=True)
    name2 = models.CharField(max_length=100,blank=True,null=True)
    img1 = models.ImageField('/media',blank=True,null=True)
    img2 = models.ImageField('/media',blank=True,null=True)
    
    
    
class product (models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    img = models.ImageField('/media')   
    offPrice = models.CharField(max_length=100,blank=True,null=True)
    descpription = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    

class item(models.Model):
    ProductID = models.ForeignKey(product,on_delete=models.CASCADE)
    user = models.ForeignKey(registerModel,on_delete=models.CASCADE)
    quantity = models.IntegerField()    



class About (models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=255)
    img1 = models.ImageField('/media')
    img2 = models.ImageField('/media',blank=True,null=True)
    img3 = models.ImageField('/media',blank=True,null=True)
    img4 = models.ImageField('/media',blank=True,null=True)
    
    
    

class team(models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=100)
    img1 = models.ImageField('/media')
    
    
    
class order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(item,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    addres = models.CharField(max_length=200)
    paymentToAddres = models.BooleanField()
    total_price = models.CharField(max_length=100,blank=True,null=True)
    
    
    

    
    

class buy_Finish_order (models.Model):
    user = models.ForeignKey(order,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    Reference_num = models.CharField(max_length=150,null=True,blank=True)
    TotalPrice = models.CharField(max_length=100,null=True,blank=True)
    
    




class desk (models.Model):
    Number_seats = models.CharField(max_length=20)
    
    def __str__(self) :
        return self.Number_seats




class reserveDesk(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.DateField()

    five = 17;four = 16;there = 15;tow = 14;one = 13;six = 18
    seven = 19;eight = 20 ;nin= 21 ; ten=22 ;eleven = 22;toweleve = 23
    timetuple = (
        (one,'13:00'),(tow,'14:00'),(there,'15:00'),(four,'16:00'),
        (five,'17:00'),(six,'18:00'),(seven,'19:00'),(eight,'20:00'),
        (nin,'21:00'),(ten,'22:00'),(eleven,'23:00')
    ) 
    time = models.IntegerField(choices= timetuple)
    
    
    tow = 2
    six = 6;five = 5;four = 4;there = 3
    ten = 10;nin = 9;eight = 8;seven = 7
    thrtin = 13;towelev = 12;eleven = 11
    sixteen = 16;fifteen =15;fourteen = 14
    eighteen =  18;ninteen = 19;seventeen = 17
    therteen = 30;fourtrrr = 40;towentiy = 20
    
    
    desktuple = (
        (tow,'دو'),(there,'سه'),(four,'چهار '),(five,'پنج '),(six,'شش'),(seven,'هفت')
        ,(eight,'هشت'),(nin,'نه'),(ten,'ده'),(eleven,'یازده'),(towelev,'دوازده'),(thrtin,'سیزده'),
        (fourteen,'چهارده'),(fifteen,'پانزده'),(sixteen,'شانزده'),(seventeen,'هوده'),(eighteen,'هجده'),(ninteen,'نوزده'),
        (towentiy,'بیست'),(therteen,'سی'),(fourtrrr,'چهل'),
    )
   
    desk = models.IntegerField(choices=desktuple)
    
    
    

    
    
    
class Emoloye(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addres = models.CharField(max_length=120)
    
















    
    

    