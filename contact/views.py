from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('name', '')
            content = request.POST.get('name', '')
            #Si sale bien se redirecciona
            return redirect(reverse('contact')+"?OK")
    return render(request, "contact/contact.html",{'form':contact_form})
