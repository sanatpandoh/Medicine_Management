from django.contrib import admin

# Register your models here.
from patient.models import Medicine, MedicineAllot, Patient,Disease,DiseaseAllot

admin.site.register(Medicine)
admin.site.register(MedicineAllot)
admin.site.register(Patient)
admin.site.register(Disease)
admin.site.register(DiseaseAllot)


