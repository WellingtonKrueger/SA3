from django.urls import path
from gladiadoremp.views import index, elenco, enredo

urlpatterns = [
    path('', index),  # Adicione esta linha para corresponder à raiz e redirecionar para a visualização 'index'
    path('elenco/', elenco),
    path('enredo/', enredo)

]