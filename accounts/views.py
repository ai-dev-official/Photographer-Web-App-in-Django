from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from django.views.generic import UpdateView
from .forms import SignUpForm,  ProfileForm, ContactForm
from .models import Profile
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profileform = ProfileForm(request.POST)

        if form.is_valid() and profileform.is_valid():
            user = form.save()

            accounts = profileform.save(commit=False)
            accounts.user = user
            accounts.save()

            login(request, user)

            return redirect('login')
    else:
        form = SignUpForm()
        profileform = ProfileForm()

    return render(request, 'registration/register.html', {'form': form, 'profileform': profileform})



@login_required
def profile(request):
    return render(request, 'registration/user_profile.html')


# @login_required
# def get_or_create_profile(request):
#     profile = None
#     user = request.user
#     try:
#         profile, created = Profile.objects.get_or_create(user=user)
#     except Profile.DoesNotExist:
#         profile = Profile.objects.create(user, ...)
#     return render(request, 'registration/user_profile.html')


class UserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = '__all__'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user.profile

    def test_func(self):
        return self.request.user.profile

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Customer Service"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'x00191169@mytudublin.ie',
                          ['x00191169@mytudublin.ie'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("thanks")

    form = ContactForm()
    return render(request, "registration/customer__service.html", {'form': form})


# class ProfilePageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Profile
#     template_name = 'registration/user_profile.html'
#     success_url = reverse_lazy('home')
#     def get_object(self):
#         return self.request.user
#     def test_func(self):
#         return self.request.user.profile
