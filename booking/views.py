from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Facility, Booking
from .forms import BookingForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'bookings/profile.html')
class FacilityListView(ListView):
    model = Facility
    template_name = 'bookings/facility_list.html'
    context_object_name = 'facilities'

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('facility_list')  # Redirect after successful booking

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-date')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('facility_list')  # Redirect to the facility list after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
