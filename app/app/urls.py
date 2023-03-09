from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from resturan.views import *
# from azbankgateways.urls import az_bank_gateways_urls




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',Home),
    path('addto<int:id>',AddToCart),
    path('delcart<int:id>',deletCart),
    path('delcomplet<int:id>',deletCompleteCart),
    path('register',Register_View),
    path('Login',Login_Veiw),
    path('cart',Cart_View),
    path('drink',drink),
    path('fastfood',Fastfood),
    path('sald',sald),
    path('about',Abouts),
    path('menu',menu),
    path('employe',EmpView),
    # path('bankgateways/', az_bank_gateways_urls()),

    
    
    
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #not both
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

