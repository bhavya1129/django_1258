from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from faker import Faker
import random

def insert_rows(request):
    fake = Faker()
    for _ in range(30):
        Person.objects.create(
            name=fake.name(),
            age=random.randint(18, 80),
            email=fake.unique.email()
        )
    return HttpResponse("30 records inserted successfully.")

def person_list(request):
    sort_by = request.GET.get('sort')
    order = request.GET.get('order')
    
    persons = Person.objects.all()

    if sort_by in ['name', 'age', 'email'] and order in ['asc', 'desc']:
        if order == "desc":
            sort_by = f"-{sort_by}"
        persons = persons.order_by(sort_by)

    return render(request, 'person_list.html', {'persons': persons}) 
