from django.shortcuts import render, redirect

from contact.models import Contact
from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form,
        }

        if form.is_valid:
            # form.save()
            contato = form.save(commit=False)
            contato.show = False
            contato.save()
            return redirect('contact:create')

        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm()
    }
    return render(request, 'contact/create.html', context)
