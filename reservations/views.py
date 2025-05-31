from .models import Appointment, Complaint
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import redirect, get_object_or_404
from .models import Complaint


def reserve_page(request):
    return render(request, 'Reservation.html')

def reserve_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')

        Appointment.objects.create(name=name, email=email, phone=phone, date=date, time=time)
        return redirect('success')

    return render(request, 'Reservation.html')

def success_page(request):
    return render(request, 'success.html')

def receptionist_dashboard(request):
    query = request.GET.get('q')
    if query:
        appointments = Appointment.objects.filter(
            Q(name__icontains=query) 
        ).order_by('date', 'time')
    else:
        appointments = Appointment.objects.all().order_by('date', 'time')

    return render(request, 'receptionist_dashboard.html', {'appointments': appointments})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    return redirect('receptionist')

def add_appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']

        Appointment.objects.create(name=name, email=email, phone=phone, date=date, time=time)
        return redirect('receptionist_dashboard')

def main_page(request):
    return render(request, 'Main_Page.html')

def complaint_page(request):
    return render(request, 'Complaint_Page.html')


def submit_complaint(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Complaint.objects.create(name=name, email=email, message=message)
        return redirect('complaint_success')

def complaint_success(request):
    return render(request, 'complaint_success.html')


def receptionist_dashboard(request):
    q = request.GET.get('q', '')
    appointments = (
    Appointment.objects.filter(name__icontains=q).order_by('-date', '-time')
    if q else Appointment.objects.all().order_by('-date', '-time')
)

    complaints = Complaint.objects.all().order_by('-created_at') 
    return render(request, 'receptionist_dashboard.html', {
        'appointments': appointments,
        'complaints': complaints,
    })

    

def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    complaint.delete()
    return redirect('receptionist_dashboard')

def main_page(request):
    latest_complaints = Complaint.objects.order_by('-created_at')[:3]
    return render(request, 'main_page.html', {'latest_complaints': latest_complaints})

