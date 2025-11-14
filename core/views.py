from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.urls import reverse_lazy

from core.forms import AttendanceConfirmationCodeForm, AttendanceForm
from .models import Event, Attendance

class EventListView(LoginRequiredMixin, ListView):
  model = Event
  template_name = 'event_list.html'
  context_object_name = 'events'

  def get_queryset(self):
    return Event.objects.filter(created_by=self.request.user).order_by('-date')

class EventDetailView(LoginRequiredMixin, DetailView):
  model = Event
  template_name = 'event_detail.html'
  context_object_name = 'event'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    event = self.get_object()
    attendances = Attendance.objects.filter(event=event)

    context['attendances'] = attendances
    context['total_confirmed'] = attendances.filter(status='confirmed').count()
    context['total_declined'] = attendances.filter(status='declined').count()
    context['total_guests'] = sum(a.total_guests for a in attendances.filter(status='confirmed'))

    return context

class EventCreateView(LoginRequiredMixin, CreateView):
  model = Event
  template_name = 'event_form.html'
  fields = ['name', 'date', 'location', 'description']
  success_url = reverse_lazy('event-list')

  def form_valid(self, form):
    form.instance.created_by = self.request.user
    return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
  model = Event
  template_name = 'event_form.html'
  fields = ['name', 'date', 'location', 'description']
  success_url = reverse_lazy('event-list')

  def get_queryset(self):
    return Event.objects.filter(created_by=self.request.user)

class EventDeleteView(LoginRequiredMixin, DeleteView):
  model = Event
  template_name = 'event_confirm_delete.html'
  success_url = reverse_lazy('event-list')

  def get_queryset(self):
    return Event.objects.filter(created_by=self.request.user)

class AttendanceConfirmationView(FormView):
  template_name = 'attendance_confirmation.html'
  form_class = AttendanceConfirmationCodeForm

  def dispatch(self, request, *args, **kwargs):
    self.access_code = kwargs.get('access_code')

    if self.access_code:
      self.event = get_object_or_404(Event, access_code=self.access_code)
      self.form_class = AttendanceForm
    else:
      self.event = None
      self.form_class = AttendanceConfirmationCodeForm
    return super().dispatch(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    if self.event:
      context['event'] = self.event
    return context

  def form_valid(self, form):
    if not self.event:
      try:
        Event.objects.get(access_code=form.cleaned_data['access_code'])
      except Event.DoesNotExist:
        form.add_error('access_code', 'Invalid access code')
        return self.form_invalid(form)

      return redirect('attendance-confirm', access_code=form.cleaned_data['access_code'])
    else:
      Attendance.objects.create(
        event=self.event,
        guest_name=form.cleaned_data['guest_name'],
        total_guests=form.cleaned_data['total_guests'],
        status=form.cleaned_data['status'],
        notes=form.cleaned_data['notes']
      )
    return render(self.request, 'confirmation_success.html', {'event': self.event})
