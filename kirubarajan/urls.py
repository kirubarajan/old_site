from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from blog.views import blog, post, category
from about.views import splash, projects, research

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name='projects'),
    path('research/', research, name='research'),
    path('post/<str:id>', post, name='post'),
    path('blog/category/<int:category>', category, name='category'),
    path('blog/', blog, name='blog'),
    path('', splash, name='splash')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)