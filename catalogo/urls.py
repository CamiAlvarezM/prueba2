from django.urls import path 
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('index/<int:pk>', views.IndexDetailView.as_view(), name='index-detail'),
	path('',views.index,name='index'),
    path('info/<int:pk>', views.InfoDetailView.as_view(), name='info-detail'),
	path('',views.info,name='info'),
    path('formulario/<int:pk>', views.FormularioDetailView.as_view(), name='formulario-detail'),
	path('',views.formulario,name='formulario'),
    path('galeria/<int:pk>', views.GaleriaDetailView.as_view(), name='galeria-detail'),
	path('',views.galeria,name='galeria'),
    path('we/<int:pk>', views.WeDetailView.as_view(), name='we-detail'),
	path('',views.we,name='we'),
]