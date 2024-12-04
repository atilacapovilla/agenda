from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    # qualquer_campo = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Novo campo criando',
    #         }
    #     ),
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Digite o seu primeiro nome, veio do init',
        # })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture'
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Digite o seu primeiro nome',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro e segundo nome não podem ser iguais',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        # if first_name == last_name:
        #     self.add_error(
        #         ValidationError(
        #             'Primeiro e segundo nomes não podem ser iguais',
        #             code='invalid'
        #         )
        #     )

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro 2',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     None,
        #     ValidationError(
        #         'Mensagem de erro de formulário non-field_error 1',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     None,
        #     ValidationError(
        #         'Mensagem de erro de formulário non-field_error 2',
        #         code='invalid'
        #     )
        # )

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        # if first_name == 'ABC':
        #     raise ValidationError(
        #         'Não digite ABC neste campo',
        #         code='invalid'
        #     )

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC neste campo',
                    code='invalid'
                )
            )

        return first_name
