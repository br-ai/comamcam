from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path("", views.home, name="home"),

    path("allCandidate", views.allCandidate, name="allCandidate"),
    path("candidate/<int:numero>", views.candidateDetail, name="candidateDetail"),

    path("allCandidat", views.allCandidat, name="allCandidat"),
    path("candidat/<int:numero>", views.candidatDetail, name="candidatDetail"),

    path("votezMiss/<int:id>", views.votez, name="votez"),
    path("votezMaster/<int:id>", views.votezH, name="votezH"),

    path("galerie", views.galerie, name="galerie"),

    path("actualite/<int:id>", views.actualite, name="actualite"),

    path("evenement", views.evenement, name="evenement"),

    path('transaction/', views.TransactionApiView.as_view({'get': 'list', 'post':'create', 'patch':'partial_update', 'put':'update' }), name='transaction'),
    path('transaction/<int:pk>', views.TransactionApiView.as_view({'get': 'retrieve', 'patch':'partial_update', 'put':'update', 'delete':'destroy'}), name='transaction'),

   
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)