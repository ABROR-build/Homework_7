from django.forms import ModelForm
from . import models


class AddCommentForm(ModelForm):
    class Meta:
        model = models.Comments
        fields = ['comment']
        print(fields)
