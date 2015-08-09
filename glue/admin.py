from django.contrib import admin
from glue.models import *


class LocationAdmin(admin.ModelAdmin):
    search_fields = ['x', 'y']


admin.site.register(GameRoom)
admin.site.register(Player)
admin.site.register(PlayerConfig)
admin.site.register(Stage)
admin.site.register(CurrentStage)
admin.site.register(MobType)
admin.site.register(Mob)
admin.site.register(Location, LocationAdmin)