from django.contrib import admin
from django.urls import path,include
from chart import views # !!!

urlpatterns = [
    path('',include('chart.urls')),
    path('world-population/', views.world_population, name='world_population'), #views.world_population 함수형 뷰
    path('admin/', admin.site.urls),
]