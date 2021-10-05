from django.contrib import admin
# from accounts import views
from main import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    #path('', include('result.urls')),
    path('test1/', views.test, name="test1"),
    #path('test1/', views.test1, name="test1"),
    path('test2/', views.test1, name="test2"),
    path('test3/', views.test2, name="test3"),
    path('test4/', views.test3, name="test4"),
    path('test5/', views.test4, name="test5"),
    path('test6/', views.test5, name="test6"),
    path('test7/', views.test6, name="test7"),
    path('test8/', views.test7, name="test8"),
    path('result/', views.result, name="result"),
    #path('submit/', views.submit, name="submit"),
    
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
