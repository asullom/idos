from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.layout import Button, Submit
from crispy_forms.bootstrap import FormActions, TabHolder, Tab, \
    PrependedAppendedText, PrependedText
from .models import Cliente


class ClienteForm(forms.ModelForm):

    """ """
    class Meta:
        model = Cliente
        #fields = ['nombre', 'apellidos', 'foto', 'dni',  ]

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-vertical'

        self.helper.layout = Layout(
            Row(
                Div(Field('nombre', css_class='input-required'),
                    css_class='col-md-6'),
                Div(Field('apellidos', css_class=''),
                    css_class='col-md-6'),
            ),
            Row(
                Div(Field('dni', css_class='input-numeric mask-num'),
                    css_class='col-md-6'),
                Div(Field('categoria', css_class='input-numeric mask-num'),
                    css_class='col-md-6'),
            ),
            Row(
                Div(Field('productos', css_class=''),
                    css_class='col-md-6'),
            ),
            Row(
                Div(Field('foto', css_class=''),
                    css_class='col-md-6'),
            ),


            FormActions(
                Submit('save', 'Save changes'),
                Button('cancel', 'Cancel')
            )
        )
