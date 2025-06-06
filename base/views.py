from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Student  # Import your model
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


@login_required
def home(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, "home.html", {"students": students})
@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')
        if not Student.objects.filter(name=name, subject=subject).exists():
            Student.objects.create(name=name, subject=subject, marks=marks)
        else:
            messages.warning(request, "Student with this name and subject already exists.")
        students = Student.objects.all()  # Fetch all students
    return render(request, "home.html", {"students": students})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def update_student(request):
    if request.method == "POST":
        student_id = request.POST.get('id')
        student = get_object_or_404(Student, id=student_id)

        student.name = request.POST.get('name')
        student.subject = request.POST.get('subject')
        student.marks = request.POST.get('marks')
        student.save()

        students = Student.objects.all()  # Fetch all students
    return render(request, "home.html", {"students": students})
@login_required
def delete_student(request, id):
    if request.method == "POST":
        student = get_object_or_404(Student, id=id)
        print(student)
        student.delete()
        students = Student.objects.all()  # Fetch all students
    return render(request, "home.html", {"students": students})
