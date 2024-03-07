from django import forms

from .models import Client, Task, Note

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['name', 'type', 'size', 'address', 'city', 'post_number', 'country', 'tel', 'mob', 'email', 'fax',
				  'director_name', 'director_address', 'director_oib',
				  'oib', 'vat_id', 'reg_number', 'stat_number', 'hzmo_number', 'hzzo_number', 'pdv', 'number_worker',
				  'price']
		labels = {'name': 'Naziv',
				  'type': 'Tip',
				  'size': 'Veličina',
				  'address': 'Adresa',
				  'city': 'Grad',
				  'post_number': 'Poštanski broj',
				  'country': 'Država',
				  'tel': 'Telefon',
				  'mob': 'Mobitel',
				  'email': 'e-mail',
				  'fax': 'Fax',
				  'director_name': 'Odgovorna osoba',
				  'director_address': 'Adresa prebivališta',
				  'director_oib': 'OIB odgovorne osobe',
				  'oib': 'OIB',
				  'vat_id': 'PDV-ID',
				  'reg_number': 'MBS',
				  'stat_number': 'MB',
				  'hzmo_number': 'HZMO broj',
				  'hzzo_number': 'HZZO broj',
				  'pdv': 'Obeznik PDV-a',
				  'number_worker': 'Broj zaposlenih',
				  'price': 'Cijena',
				  }

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'due_date', 'recurring', 'recurring_period', 'end_date', 'description']
		labels = {'name': 'Naziv',
				  'due_date': 'Datum',
				  'recurring': 'Ponavljajući',
				  'recurring_period': 'Period ponavljanja',
				  'end_date': 'Završni datum',
				  'description': 'Opis',
				  }

	due_date = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d.%m.%Y', )
        )
	end_date = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d.%m.%Y', )
        )

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['text']
		labels = {'text': 'Bilješka',
				  }