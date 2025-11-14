from django import forms

class AttendanceConfirmationCodeForm(forms.Form):
  access_code = forms.CharField(
    label="Código de Acesso do Evento",
    max_length=20,
    widget=forms.TextInput(attrs={
      "class": "shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500",
      "placeholder": "Digite o seu código de acesso"
    })
  )

class AttendanceForm(forms.Form):
  guest_name = forms.CharField(
    label="Nome Completo",
    max_length=200,
    widget=forms.TextInput(attrs={
      "class": "shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500"
    })
  )
  total_guests = forms.IntegerField(
    label="Número Total de Convidados (inclua você)",
    min_value=1,
    widget=forms.NumberInput(attrs={
      "class": "shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500"
    })
  )
  status = forms.ChoiceField(
    label="Confirmação de Presença",
    choices=[('confirmed', 'Confirm'), ('declined', 'Decline')],
    widget=forms.RadioSelect(attrs={"class": "inline-flex space-x-4"})
  )
  notes = forms.CharField(
    label="Notas (opcional)",
    required=False,
    widget=forms.Textarea(attrs={
      "class": "shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500",
      "rows": 3
    })
  )
