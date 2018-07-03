from django.contrib import admin
from django.urls import path
from blog.views import blog, post
from about.views import splash, projects, research

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name='projects'),
    path('research/', research, name='research'),
    path('post/<str:id>', post, name='post'),
    path('blog/', blog, name='blog'),
    path('', splash, name='splash')
]