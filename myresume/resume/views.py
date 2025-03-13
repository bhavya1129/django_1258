from django.shortcuts import render

def resume_view(request):
    context = {
        'name': 'Bhavya',
        'title': 'Web Developer',
        'profile': 'A passionate web developer skilled in modern technologies.',
        'education': [
            {'degree': 'Tenth', 'stream': 'MPC', 'institution': 'Sri Chaitanya Techno School', 'year': '2021'},
            {'degree': 'Intermediate', 'stream': 'MPC', 'institution': 'Sri Chaitanya Junior College', 'year': '2023'},
            {'degree': 'B-Tech', 'stream': 'Information Technology', 'institution': 'Shri Vishnu Engineering College For Women', 'year': '2027'},
        ],
        'skills': ['HTML', 'CSS', 'JavaScript', 'Django', 'Bootstrap', 'React', 'Node.js'],
        'projects': [
            {'name': 'Job Board Website', 'description': 'A platform for job postings and applications using React, Node.js, and MongoDB.'},
            {'name': 'Portfolio Website', 'description': 'A personal portfolio showcasing my projects and skills with dynamic cursor effects.'},
            {'name': 'E-Commerce Site', 'description': 'An online shopping platform with secure payment gateway integration.'},
        ],
        'hobbies': ['Coding', 'Reading Tech Blogs', 'Photography', 'Gaming', 'Blogging'],
        'languages_known': ['English', 'Telugu',],
        'certifications': [
            {'name': 'Frontend Web Development', 'issuer': 'Coursera'},
            {'name': 'Django Framework', 'issuer': 'Udemy'},
            {'name': 'React Developer', 'issuer': 'FreeCodeCamp'},
        ],
    }
    return render(request, 'resume.html', context)


