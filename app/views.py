from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your views here.

def home_page(request):
    return render(request, "home.html")


def student_list(request):
    data = Student.objects.all()
    return render(request, 'student_list.html', {'data': data})


def add_student(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('/students/')

    return render(request, 'add_student.html', {'form': form})


def edit_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('/students/')

    return render(request, 'edit_student.html', {'form': form})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.error(request, "Student deleted!")
    return redirect('/students/')

from django.db.models import Avg, Min, Max
from .models import Student

def dashboard(request):
    total = Student.objects.count()
    avg_age = Student.objects.aggregate(Avg('age'))['age__avg']
    youngest = Student.objects.order_by('age').first()
    oldest = Student.objects.order_by('-age').first()
    recent = Student.objects.order_by('-id')[:5]

    context = {
        'total': total,
        'avg_age': avg_age,
        'youngest': youngest,
        'oldest': oldest,
        'recent': recent,
    }
    return render(request, "dashboard.html", context)
