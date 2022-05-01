from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from .forms import ContactUs
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 


class HomePageView(LoginRequiredMixin, UserPassesTestMixin,TemplateView):
    template_name = 'home.html'

    def test_func(self):
        return self.request.user.profile

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            subject = "Customer Service"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'phone': form.cleaned_data['phone'],
                'address': form.cleaned_data['address'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
                
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@admin.com',
                          ['admin@admin.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("thanks")

    form = ContactUs()
    return render(request, "contact.html", {'form': form})

@login_required
def booking(request):
    context = {}
    template_name = 'booking.html'
    return render(request, 'booking.html', {})
@login_required
def about(request):
    context = {}
    template_name = 'about.html'
    return render(request, 'about.html', {})
@login_required
def thanks(request):
    context = {}
    template_name = 'thanks.html'
    
    return render(request, 'thanks.html', {})