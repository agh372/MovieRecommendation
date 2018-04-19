from django.forms import ModelForm, Textarea
from movies.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating']
