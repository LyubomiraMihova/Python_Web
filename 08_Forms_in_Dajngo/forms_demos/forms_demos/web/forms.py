from django import forms


# Create your forms here
class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school students'),
        (3, 'Student'),
        (4, 'Adult')
    )

    your_name = forms.CharField(
        label='Your name',
        max_length=100,
        help_text='Enter your name here',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your name',
                'class': 'form-control',

            }
        )
    )
    age = forms.IntegerField(
        required=False,
        label='Your age',
        initial=0,
        help_text='Enter your age here',
        widget=forms.NumberInput()
    )
    story = forms.CharField(
        widget=forms.Textarea
    )

    # email = forms.CharField(
    #     widget=forms.EmailInput(),
    # )
    #
    # url = forms.CharField(
    #     widget=forms.URLInput,
    # )
    #
    # secrets = forms.CharField(
    #     widget=forms.PasswordInput(),
    # )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
    )
    #
    # occupancy2 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.RadioSelect()
    # )
    #
    # occupancy3 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.SelectMultiple()
    # )
