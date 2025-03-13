
from django.shortcuts import render, HttpResponse
from .models import Student

def insert_student(request):
    student = Student(name="Bhavya", age=19, email="bhavya@example.com")
    student.save()
    return HttpResponse("Student record added successfully!")
def student_list(request):
    students = Student.objects.all()
    return render(request, 'std/student_list.html', {'students': students})
