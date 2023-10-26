from django.shortcuts import render,redirect
from .forms import TimeEntryForm
from .models import TimeEntry
# Create your views here.


def timesheet(request):
    entries = TimeEntry.objects.filter(user=request.user)
    context = {'entries': entries}
    return render(request, 'app1/timesheet.html', context)

def add_entry(request):
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('timesheet')
    else:
        form = TimeEntryForm()
    context = {'form': form}
    return render(request, 'timesheet_app/add_entry.html', context)