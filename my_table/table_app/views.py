from django.shortcuts import render  
def grid_view(request): 
    people = [ 
        {"name": "Meenakshi", "age": 20, "city": "Ongole"}, 
        {"name": "Nandini", "age": 19, "city": "Bhimavaram"}, 
        {"name": "Hema", "age": 19, "city": "Rajmundary"}, 
        {"name": "Devi", "age": 20, "city": "Guntur"}, 
        {"name": "Bhavya", "age": 21, "city": "Vijayawada"}, 
    ] 
    return render(request, "t/user_list.html", {"people": people}) 
def table_view(request): 
    people = [
          {"name": "Meenakshi", "age": 20, "city": "Ongole"}, 
        {"name": "Devi", "age": 20, "city": "Guntur"}, 
        {"name": "Bhavya", "age": 21, "city": "Vijayawada"}, 
    ] 
    return render(request, "t/table.html", {"people":people})  
