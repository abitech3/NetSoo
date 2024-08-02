from django.urls import path
from netsooapp.views import Register
urlpatterns= [
    path("register" , Register.as_view())
]