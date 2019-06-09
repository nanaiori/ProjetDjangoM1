from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.home),
    path('article/<id_article>', views.view_article),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('contact/', views.contact, name='contact'),
    path('livre/', views.livre, name='livre'),
    path('livreDetails/<int:id>', views.livreDetails, name='livreDetails'),
]