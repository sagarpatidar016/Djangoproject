from django import forms
from rooftop.models import sage
from rooftop.models import reserve
from rooftop.models import comment



class RoofForm(forms.ModelForm):
    class Meta:
        model=sage
        fields={"name","email","phone","message"}

class ReservForm(forms.ModelForm):
    class Meta:
        model=reserve
        fields={"name","email","phone","date","time","message"}


class ReviewForm(forms.ModelForm):
    class Meta:
        model=comment
        fields={"name","email","subject","message"}