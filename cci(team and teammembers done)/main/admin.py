from django.contrib import admin

from . models import TeamMembers, Teams, CciGroups

admin.site.register(TeamMembers)
admin.site.register(Teams)
admin.site.register(CciGroups)
