"""
URL configuration for school_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import (
    opening_table,staff_table,add_staff,update_staff,delete_staff,student_table,add_student,update_student,delete_student,fee_table,add_fee,update_fee,delete_fee)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",opening_table,name="openingtable"),
    
    path("staff_table/",staff_table,name="stafftable"),
    path("add_staff/", add_staff, name='addstaff'),
    path("update_staff/<int:id>/", update_staff, name='updatestaff'),
    path("delete_staff/<int:id>/", delete_staff, name='deletestaff'),


    path("student_table/",student_table,name="studenttable"),
    path("add_student/", add_student, name='addstudent'),
    path("update_student/<int:id>/", update_student, name='updatestudent'),
    path("delete_student/<int:id>/", delete_student, name='deletestudent'),

    path("fee_table/",fee_table,name="feetable"),
    path("add_fee/", add_fee, name='addfee'),
    path("update_fee/<int:id>/", update_fee, name='updatefee'),
    path("delete_fee/<int:id>/", delete_fee, name='deletefee'),
]