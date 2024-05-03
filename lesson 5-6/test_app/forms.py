from django.forms import ModelForm, Textarea, DateInput
from test_app.models import Author

class AddAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'first_name',
            'last_name',
            'short_biography',
            'birth_date',
            'where_from',
            'photo',
        ]
        widgets = {
            'short_biography': Textarea(attrs={'cols': 60, 'rows': 15}),
            'birth_date': DateInput(attrs={'type': 'date'}),
        }