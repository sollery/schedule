from django.urls import path        #Импорт модуля Django
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main_show,name='main'),
    path('schedule/',views.schedule_show,name='schedule'),
    path('lesson/<int:lesson_id>/', views.put_marks,name='put_marks'),
    path('performance/',views.performance_show,name='performance'),
    path('performance/<int:stud_id>/', views.performance_stud_show, name='performance_stud'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns