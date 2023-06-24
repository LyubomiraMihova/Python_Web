from django import forms
from django.db import models

from forms_demos_part_2.web.models import ToDo
from forms_demos_part_2.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=(
            validate_text,
        )
    )
    is_done = forms.BooleanField(
        required=False,
    )
    priority = forms.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
            # validate_priority,
            # MinValueValidator(1),
            # MaxValueValidator(10),
        )
    )


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('')


