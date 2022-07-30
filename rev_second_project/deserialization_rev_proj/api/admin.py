from django.contrib import admin
from .models import Equipment


# Register your models here.


@admin.register(Equipment)
class EquipAdmin(admin.ModelAdmin):
    list_display = ["id", "cp_number", "sne_id", "sch_number", "trs_area"]
