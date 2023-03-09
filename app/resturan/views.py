from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
# from azbankgateways import bankfactories, models as bank_models, default_settings as settings
# from azbankgateways.exceptions import AZBankGatewaysException
# import logging
# from django.http import HttpResponse, Http404
# from django.urls import reverse


def error(request):
    return render(request,'resturan/e.html')

    
    
def Fastfood(request):
    fastFood = product.objects.filter(descpription = 'فست فود')
    context = {'fastfood':fastFood}
    return render(request,'resturan/fastfood.html',context)
    
    
def sald(request):
    sald = product.objects.filter(descpription = 'سالاد')
    context = {'sald':sald }
    return render(request,'resturan/sald.html',context)



def drink(request):
    drink = product.objects.filter(descpription = 'نوشیدنی')
    context = { 'drink':drink }
    return render(request,'resturan/drink.html',context)

    
    

   


def Home(request):
    
        
    
    menu = product.objects.all()

    
    # reserve desk code start
    List = []
    form = reserve_Form()
    if request.method == 'POST':        
        form = reserve_Form(request.POST)
        if form.is_valid():
            for i in form :
                List.append(i.data)
            print(List) 
                 
                 
            if List[4] == '30' or List[4] == '40':
                return render (request,'resturan/call.html',{})
            
            
            if reserveDesk.objects.filter(date = List[2],time = List[3]):
                return render (request,'resturan/full.html',{})
            
            
            else :
                counter = 0
        
                if List[4] is not None:
                    get = reserveDesk.objects.filter(desk = List[4]) 
                    if get is not None:
                        for i in get:
                            counter = counter + 1
                        print(counter)    
                        if counter == 5:
                            print('*reject*')
                            return render(request,'resturan/e.html')
                    
              
                        elif 5 >= counter:
                            print('---------------------------------')
                            push = reserveDesk(name = List[0],phone = List[1],date =List[2] ,time =List[3],desk = List[4] )
                            push.save()
                            reserve_amaunt = (int(List[4]) * 50000)
                            print('+seved+')
                            context = {
                                'name':List[0],'nummber':List[1],'date':List[2]
                                , 'time':List[3],'desk':List[4],'reserve_amaunt':reserve_amaunt,
                            }
                            
                            return render(request,'resturan/chckoutres.html',context)
                        
                    # reserve desk code END


    context =  {'form':form,
                'menu':menu,
            }       
    return render(request,'resturan/index1.html',context)



def Abouts(request):
    return render(request,'resturan/about.html')




def menu(request):
    return render(request,'resturan/menu.html')


from django.contrib.auth.decorators import login_required

@login_required
def AddToCart (request, id):
    menu = product.objects.get(id=id)

    # if registerModel.objects.get(user_id = request.user.id).exists():
    #     print('user is exist to registerModel .')
    # else : 
    #     return redirect(Login_Veiw)
        
    
    register = registerModel.objects.get(id=request.user.id)    
    try :
        if item.objects.get(ProductID=id,user=register):
            update = item.objects.get(ProductID=id,user=register)
            update.quantity += 1
            update.save()
       
        else:
            print('ngfdfghj')
    except:
        # register = registerModel.objects.get(id=request.user.id)    
        add =item(ProductID=menu, quantity=1, user=register)
        add.save()
        
    
    # return render(request, 'resturan/index.html')        
    return redirect(Cart_View)


def deletCompleteCart(request,id):
    items = item.objects.get(ProductID=id,user=request.user.id)
    items.delete()
    return redirect(Cart_View)
    
    


def deletCart (request,id):
    try :
        if item.objects.get(ProductID=id,user=request.user.id):
            update = item.objects.get(ProductID=id,user=request.user.id)
            update.quantity -= 1
            if update.quantity == -1 :
                update.quantity = 0
                update.save()
            else : 
                update.save()
                
            return redirect(Cart_View)
        
    except:
        if item.objects.filter(ProductID=id,user=request.user.id) == None:
            if item is  None :
                print('exept')
    return redirect(Home)    
    




# def Cart_View(request):
#     id_list = []
#     user_id = request.user.id
#     items = item.objects.filter(user_id=user_id)
#     for iitem in items:
#         id_list.append(iitem.ProductID.pk)
#     print(id_list)
#     products = product.objects.filter(id__in=id_list)
#     return render(request, 'resturan/cart.html', {'items': products})




# def Cart_View(request):
#     items = []
    
#     total_checkout_price = 0
#     user_id = request.user.id
#     cart_items = item.objects.filter(user_id=user_id)
#     for cart_item in cart_items:
#         product_id = cart_item.ProductID.pk
#         product_quantity = cart_item.quantity
#         # Get the product object and its image URL
#         prod_obj = product.objects.get(id=product_id)
#         prod_img_url = prod_obj.img.url if prod_obj.img else None
#         # Add the product information to the items list
#         items.append({
#             'product': prod_obj,
#             'quantity': product_quantity,
#             'image_url': prod_img_url
#         })


#     print('   ',total_checkout_price)      

#     return render(request, 'resturan/cart.html', {'items': items})



def Cart_View(request):
    items = []
    total_Price = 0
    sum_quantity = 0
    user_id = request.user.id
    cart_items = item.objects.filter(user_id=user_id)
    total_checkout_price = 0
    for cart_item in cart_items:
        product_id = cart_item.ProductID.pk
        product_quantity = cart_item.quantity
        # Get the product object and its image URL
        prod_obj = product.objects.get(id=product_id)
        prod_img_url = prod_obj.img.url if prod_obj.img else None
        # Calculate the total price for the item
        total_price = int(product_quantity) * int(prod_obj.price)
        # Add the total price of the item to the checkout price
        total_checkout_price += total_price
        # Add the product information to the items list
        sum_quantity +=product_quantity
        total_Price = total_price
        items.append({
            'product': prod_obj,
            'quantity': product_quantity,
            'image_url': prod_img_url,
            'price': prod_obj.price,
            'total_price': total_price,
        })
        
    # addes and send prodeuct
    List_order = []
    item_order = item.objects.filter(user_id=user_id)
    form = order_Form()

    if request.method == 'POST':
        form = order_Form(request.POST)
        if form.is_valid():
            for b in form:
                List_order.append(b.data)
            print('0000000  ',List_order)
            # Create a new order for each item in item_order
            for i in item_order:
                Save = order(user=i, phone=List_order[0], addres=List_order[1],
                         paymentToAddres=List_order[2], total_price=total_Price)
                Save.save()
                print('save .......')
                return render(request,'resturan/sendfood.html')
                
    Userdetails = User.objects.get(id=request.user.id)
    username = Userdetails.first_name
    print(username)
    
    
    return render(request, 'resturan/cart.html', {'username':username,'form':form,'sum_quantity':sum_quantity,'items': items,
                                                  'total_checkout_price': total_checkout_price})









def EmpView(request):
    form = Employe_Form()
    if request.method == 'POST':
        form = Employe_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'resturan/succses.html')
    
    return render(request,'resturan/employe.html',{'form':form})
        
        
        
        
        
        
def Register_View(request):
    List =[]
    Reg =RegisterForm()
    if request.method == 'POST':
        Reg =RegisterForm(request.POST)
        if Reg.is_valid():
            for i in Reg:
                List.append(i.data)
            print(List)
            user =User.objects.create_user(first_name =List[0] ,username = List[1],password=List[2])
            user.save()
            return redirect(Login_Veiw)
            
    return render(request,'resturan/register.html',{"Reg":Reg})




    
    
    
def Login_Veiw(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password=password)
        
        if user is not  None:
            login(request , user)
                
            if registerModel.objects.filter(user_id = request.user.id):
                print('.... user is exist ....')
            else:
                saveTOregister = registerModel(user_id = request.user.id)
                saveTOregister.save()
                print('user is ( not ) exist to registerModel || but saved :)')
            # messages.success(request,('with success'))
            return redirect(Home)
        
        else :
            context = {
                'username':username,
                'errormessage':'کاربر یافت نشد'
            }
            return render (request ,'resturan/login.html',context)
    else :
        return render (request , 'resturan/login.html',{})           

    
    
    

'''
def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 1000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url(reverse('callback-gateway'))
        bank.set_mobile_number(user_mobile_number)  # اختیاری
    
        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید. 
        bank_record = bank.ready()
        
        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e 




def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")
'''