from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('price-me', views.price, name='price'),
    path('feedback-you', views.feedback, name='feedback'),
    path('create', views.create, name='create'),
    path("createComment/<int:pk>/", views.createComment, name='createComment'),
]
