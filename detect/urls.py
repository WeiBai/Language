from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from singleline import views as line_views
from uploader import views as uploader_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'detect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', line_views.index, name='home_page'),
    url(r'^edit/$', line_views.edit_page, name='edit_page'),
    url(r'^edit/action$', line_views.edit_action, name='edit_action'),
    url(r'^upload/$', uploader_views.home, name='file_upload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
