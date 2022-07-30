from django.contrib import admin
from .models import Equipments


# Register your models here.


@admin.register(Equipments)
class EquipAdmin(admin.ModelAdmin):
    list_display = ["id", "cp_number", "sne_id", "trs_area"]
