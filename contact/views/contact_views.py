
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact


def index(request):
    # contacts = Contact.objects.all().order_by('-id')
    # contacts = Contact.objects.filter(show=True).order_by('-id')

    contacts = Contact.objects.filter(show=True).order_by('-id')
    # print(contacts.query)

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        # 'contacts': contacts,
        'page_obj': page_obj,
        'site_title': 'Contatos '
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def search(request):
    # search_value = request.GET['q']

    # para evitar erros - .strip, remove espaços do começo e do fim
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    # com a virgula ( , )- AND
    # Q(first_name__icontains=search_value), Q(last_name__icontains=search_value)
    # com o pipe ( | )- OR
    # Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value)
    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search '
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    # single_contact = Contact.objects.get(pk=contact_id)
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    site_title = f'{ single_contact.first_name } { single_contact.last_name } '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
