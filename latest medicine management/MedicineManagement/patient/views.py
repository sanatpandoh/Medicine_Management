from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import datetime

# Create your views here.
from patient.models import Patient, DiseaseAllot, Disease, MedicineAllot, Medicine


@login_required
def homepage(request):
    medicines = Medicine.objects.all()
    return render(request, 'patient/Homepage.html', {'all_medicines': medicines})


def add_patinet_view(request):
    diseases = Disease.objects.all()
    medicines = Medicine.objects.all()
    context = {'all_diseases': diseases,
               'all_medicines': medicines}
    return render(request, 'patient/add_patient.html', context)


def register_user(request):
    if request.method == 'POST':
        name = request.POST['name']

        phone = request.POST['phone']
        address = request.POST['address']
        age = request.POST['age']
        gender = request.POST['gender']
        total_disease = request.POST['total_disease']
        total_medicine = request.POST['total_medicine']
        # total_price = request.POST['price']
        adhar = request.POST['adhar']

        print(total_disease)
        print(total_medicine)

        patient = Patient()
        patient.name = name

        patient.phone = phone
        patient.age = age
        patient.sex = gender
        patient.address = address
        # patient.total_bill = total_price
        patient.aadhar_id = adhar
        patient.save()

        i = 1
        j = 1

        while i <= int(total_disease):
            disease_name = request.POST['disease' + str(i)]
            disease_obj = get_object_or_404(Disease, name=disease_name)
            disease_allot = DiseaseAllot()
            disease_allot.patient = patient
            disease_allot.disease = disease_obj
            disease_allot.name = disease_name
            disease_allot.save()
            i += 1

        while j <= int(total_medicine):
            medicine_name = request.POST['medicine' + str(j)]
            medicine_qty = request.POST['quantity' + str(j)]

            medicine_obj = get_object_or_404(Medicine, name=medicine_name)

            medicine_allot = MedicineAllot()
            medicine_allot.name = medicine_name
            medicine_allot.patient = patient

            medicine_allot.medicine = medicine_obj

            total_qty = int(medicine_obj.total_quantity) - int(medicine_qty)

            if total_qty > 0:
                medicine_obj.total_quantity = total_qty
                medicine_allot.quantity = medicine_qty
                # medicine_allot.price = int(medicine_obj.tablet_price) * int(medicine_qty)
                messages.success(request, str(total_qty) + " tablets of " + str(medicine_obj.name) + " left in stock")

            elif total_qty == 0:
                medicine_obj.total_quantity = total_qty
                medicine_allot.quantity = medicine_qty
                # medicine_allot.price = int(medicine_obj.tablet_price) * int(medicine_qty)
                medicine_obj.available = False
                messages.success(request, medicine_obj.name + " is out of stock")

            else:
                medicine_obj.total_quantity = 0
                medicine_obj.available = False
                medicine_allot.quantity = int(medicine_obj.total_quantity)
                # medicine_allot.price = int(medicine_obj.tablet_price) * int(medicine_obj.total_quantity)
                messages.success(request, medicine_obj.name + " is out of stock")

            medicine_obj.save()
            medicine_allot.save()
            j += 1

        messages.success(request, "User Registered Successfully.")
        return HttpResponseRedirect('/patient/add_patient')

    else:
        return render(request, 'patient/add_patient.html', {})


def all_patients(request):
    if request.method == "POST":
        medicines = Medicine.objects.all()
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']

        print(day)

        if day == '0':
            day = ''
            all_patients = Patient.objects.filter(date__year=year, date__month=month)

        else:
            all_patients = Patient.objects.filter(date__year=year, date__month=month, date__day=day)

        context = {
            'day': day,
            'month': month,
            'year': year,
            'all_patients': all_patients,
            'all_medicines': medicines
        }

        return render(request, 'patient/all_patients.html', context)

    else:
        medicines = Medicine.objects.all()
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        all_patients = Patient.objects.filter(date__year=currentYear, date__month=currentMonth, date__day=currentDay)
        context = {
            'day': currentDay,
            'month': currentMonth,
            'year': currentYear,
            'all_patients': all_patients,
            'all_medicines': medicines
        }

        return render(request, 'patient/all_patients.html', context)


def patient_detail(request, pk):
    if request.method == 'POST':
        name = request.POST['name']

        phone = request.POST['phone']
        address = request.POST['address']
        age = request.POST['age']
        gender = request.POST['gender']
        total_disease = request.POST['total_disease']
        total_medicine = request.POST['total_medicine']
        # total_price = request.POST['price']
        adhar = request.POST['adhar']

        print(total_disease)
        print(total_medicine)

        patient = get_object_or_404(Patient, pk=pk)
        patient.name = name

        patient.phone = phone
        patient.age = age
        patient.sex = gender
        patient.address = address
        # patient.total_bill = total_price
        patient.aadhar_id = adhar
        patient.save()

        if total_disease != int(total_disease):

            i = 1
            print("hello")

            while i <= int(total_disease):
                disease_name = request.POST['disease' + str(i)]
                disease_obj = get_object_or_404(Disease, name=disease_name)
                disease_allot = DiseaseAllot()
                disease_allot.patient = patient
                disease_allot.disease = disease_obj
                disease_allot.name = disease_name
                disease_allot.save()
                i += 1

        if total_medicine != int(total_medicine):
            print("world")
            j = 1

            while j <= int(total_medicine):
                medicine_name = request.POST['medicine' + str(j)]
                medicine_qty = request.POST['quantity' + str(j)]

                medicine_obj = get_object_or_404(Medicine, name=medicine_name)

                medicine_allot = MedicineAllot()
                medicine_allot.name = medicine_name
                medicine_allot.patient = patient

                medicine_allot.medicine = medicine_obj

                total_qty = int(medicine_obj.total_quantity) - int(medicine_qty)

                if total_qty > 0:
                    medicine_obj.total_quantity = total_qty
                    medicine_allot.quantity = medicine_qty
                    # medicine_allot.price = int(medicine_obj.tablet_price) * int(medicine_qty)
                    messages.success(request,
                                     str(total_qty) + " tablets of " + str(medicine_obj.name) + " left in stock")

                elif total_qty == 0:
                    medicine_obj.total_quantity = total_qty
                    medicine_allot.quantity = medicine_qty
                    # medicine_allot.price = int(medicine_obj.tablet_price) * int(medicine_qty)
                    medicine_obj.available = False
                    messages.success(request, medicine_obj.name + " is out of stock")

                else:
                    medicine_obj.total_quantity = 0
                    medicine_obj.available = False
                    medicine_allot.quantity = int(medicine_obj.total_quantity)
                    # medicine_allot.price = int(medicine_obj.tablet_price) * int(medicine_obj.total_quantity)
                    messages.success(request, medicine_obj.name + " is out of stock")

                medicine_obj.save()
                medicine_allot.save()
                j += 1

        messages.success(request, "User Updated Successfully.")
        return HttpResponseRedirect('/patient/'+pk)

    else:
        medicines = Medicine.objects.all()
        diseses = Disease.objects.all()
        patient = get_object_or_404(Patient, pk=pk)
        return render(request, 'patient/patient_detail.html',
                      {'patient': patient, 'all_medicines': medicines, 'all_diseases': diseses})


def all_meds(request):
    if request.method == 'POST':
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']

        print(day)

        if day == '0':
            day = ''
            all_med = Medicine.objects.filter(med_date__year=year, med_date__month=month)

        else:
            all_med = Medicine.objects.filter(med_date__year=year, med_date__month=month, med_date__day=day)

        context = {
            'day': day,
            'month': month,
            'year': year,
            'all_medicines': all_med
        }

        return render(request, 'patient/all_medicines.html', context)

    else:

        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        medicines = Medicine.objects.filter(med_date__year=currentYear, med_date__month=currentMonth,
                                            med_date__day=currentDay)

        return render(request, 'patient/all_medicines.html', {'day': currentDay,
                                                              'month': currentMonth,
                                                              'year': currentYear, 'all_medicines': medicines})
