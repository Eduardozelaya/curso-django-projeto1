from django.urls import path
from recipes.views import home, contato, sobre


urlpatterns = [
    path('', home), # /home/
    path('sobre/', sobre), # /contato/
    path('contato/', contato), # /contato/
]