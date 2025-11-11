from django.contrib import admin

from app1.models import staff_model,student_model,fee_model

class staff_admin(admin.ModelAdmin):
    list_display=["name","email","mobile","department","salary","hire_date"]
admin.site.register(staff_model,staff_admin)

class student_admin(admin.ModelAdmin):
    list_display=["name","age","email","mobile","department","join_date"]
admin.site.register(student_model,student_admin)

class fee_admin(admin.ModelAdmin):
    list_display=["student_name","amount","status","payment_date"]
admin.site.register(fee_model,fee_admin)
