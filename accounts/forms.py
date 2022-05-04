# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser, Profile


# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('username', 'email')


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')


# class ProfileForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ['user']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['profile_image'].widget.attrs['class'] = 'input'
        self.fields['date_of_birth'].widget.attrs['class'] = 'input'
        self.fields['fav_author'].widget.attrs['class'] = 'input'
        self.fields['description'].widget.attrs['class'] = 'input'
        self.fields['hobbies'].widget.attrs['class'] = 'input'
        self.fields['city'].widget.attrs['class'] = 'input'
        self.fields['phone'].widget.attrs['class'] = 'input'
        self.fields['website'].widget.attrs['class'] = 'input'

    class Meta:
        model = Profile
        fields = ['profile_image', 'date_of_birth', 'fav_author',
                  'description', 'hobbies', 'city', 'phone', 'website']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['first_name'].widget.attrs['class'] = 'input'
        self.fields['last_name'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class ContactForm(forms.Form):
   # message_name = forms.CharField(max_length=25)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email_address = forms.EmailField(max_length=50)
   # message_name = forms.CharField(max_length=25)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
