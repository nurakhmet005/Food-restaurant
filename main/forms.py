from .models import Reserve
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, TimeInput, NumberInput

class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        fields = ['name', 'phone', 'guests', 'time']
        widgets = {
            "name": TextInput(attrs={
                "class": "modal__input modal__name",
                "placeholder": "Имя"
            }),
            "phone": TextInput(attrs={
                "class": "modal__input modal__phone",
                "placeholder": "Телефон"
            }),
            "guests": NumberInput(attrs={
                "class": "modal__input modal__guests",
                "placeholder": "Гостей"
            }),
            "time": TimeInput(attrs={
                "class": "modal__input modal__time",
                "placeholder": "Время"
            })
        }