from django.shortcuts import render

def student_details(request):
    students = [
        {'name': 'Bhavya', 'marks':61},
        {'name': 'Hema','marks':70},
        {'name': 'Meena','marks':55},
        {'name': 'Jaya', 'marks':40},
    ]
    passing_marks = 50  # Define passing marks threshold
    return render(request, 'student/student_details.html', {'students': students, 'passing_marks': passing_marks})

