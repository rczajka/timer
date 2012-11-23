import json
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import TimerForm
from .models import Timer

def show_timer(request, slug=''):
	timer = Timer.get(slug)
	return render(request, "timer/show.html", {"timer": timer})

@permission_required("timer.change_timer")
def set_timer(request, slug=''):
    timer = Timer.get(slug)
    if request.method == "POST":
        form = TimerForm(request.POST, instance=timer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    else:
        form = TimerForm(instance=timer)
    return render(request, "timer/set.html", {
        "form": form,
        "timer": timer
    })

def state(request, slug=''):
	timer = Timer.get(slug)
	response_data = {
		"change_stamp": timer.change_stamp,
		"state": timer.state,
		"minutes": timer.minutes,
		"seconds": timer.seconds,
	}	
	return HttpResponse(json.dumps(response_data), mimetype="application/json")
