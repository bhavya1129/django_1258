from django.shortcuts import render
from .forms import ContactForm
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Process email and message as needed
            return render(request, "f/success.html", {"name": name})
    else:
        form = ContactForm()
        return render(request, 'f/contact.html', {'form': form})
def success_view(request):
    return render(request,"f/success.html")
