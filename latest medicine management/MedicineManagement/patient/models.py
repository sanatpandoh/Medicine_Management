from django.db import models

# Create your models here.
from django.utils import timezone


class Patient(models.Model):
    name = models.CharField(max_length=20, blank=False)
    # father_name = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=10, blank=False, default='----NA----')
    aadhar_id = models.CharField(max_length=12, default='------NA------')
    sex = models.CharField(max_length=10, blank=False)
    age = models.IntegerField(blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class Disease(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.name)


class Medicine(models.Model):
    name = models.CharField(max_length=20, blank=False)
    total_tablets = models.IntegerField(blank=False, default=0)
    total_packets = models.IntegerField(blank=False, default=0)
    total_quantity = models.IntegerField(blank=False)
    available = models.BooleanField(default=True)
    tablet_price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
    med_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class MedicineAllot(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.name)


class DiseaseAllot(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return str(self.name)
