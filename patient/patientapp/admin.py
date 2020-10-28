from django.contrib import admin

from patientapp.models import patient

class patientAdmin(admin.ModelAdmin):
    list_display=('id','cNAME','cID','cGENDER','cAGE','cWHERE','cPAINSITE','cWHEN','cHOW','cPAINLEVEL','cPI')
    list_filter=('cNAME','cGENDER')
    search_fields=('cNAME',)
    ordering=('id',)

admin.site.register(patient,patientAdmin)

# Register your models here.
