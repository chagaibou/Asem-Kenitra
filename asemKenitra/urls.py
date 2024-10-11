from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import backend_frontend.views as views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home_view,name='home'),
    path("evenement",views.evenement_list_view,name='evenement'),
    path("evenement/<int:event_id>",views.evenement_detail_view,name='evenement-detail'),
    path("about/",views.a_propos_view,name='about'),
    path("infosAdministratives",views.infos_administrative_view,name='infos')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)