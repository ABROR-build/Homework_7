from django.forms import ModelForm
from . import models


class AddCommentForm(ModelForm):
    class Meta:
        model = models.Comments
        fields = ['comment']
        print(fields)


class EditCommentForm(ModelForm):
    class Meta:
        model = models.Comments
        fields = ['comment']
        print(fields)


class EditProfileForm(ModelForm):
    class Meta:
        model = models.Accounts
        fields = ['password', 'username', 'bio', 'age', 'profile_picture']