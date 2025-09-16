from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home_view),
    path("age/",views.age_view),
    path("course/",views.course_view),
    path("result/", views.final_course_view),

]
