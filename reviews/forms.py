import django.forms as forms

# import in the review model
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'book', 'content', 'date')
