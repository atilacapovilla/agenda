from django.shortcuts import render
from contact.models import Contact


def index(request):
    # Seleciona todos os contatos com order decrescente de id
    # contacts = Contact.objects.all().order_by('-id')

    # Seleciona filtra os contatos com o campo show True
    # contacts = Contact.objects.filter(show=True).order_by('-id')

    # Seleciona filtra os contatos com o campo show True mostra os 5 primeiros
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:5]
    # print(contacts.query)

    # cria a variável de contexto
    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )
