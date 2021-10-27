from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Count
from django.template import loader
from datetime import datetime
from django.shortcuts import render
from django.http import Http404

from .models import User, Record

# Create your views here.

def index(request):
    latest_record_list = Record.objects.order_by('-pub_date')[:5]
    user_list = User.objects.order_by('name')[:5]
    #template = loader.get_template('appstrava/index.html')
    context = {'latest_record_list': latest_record_list, 'user_list': user_list}
    #output = ', <br>'.join([r.record_name() for r in latest_record_list])
    return render(request, 'appstrava/index.html', context)
    #return HttpResponse(template.render(context, request))

def detail(request, record_id):
    authors = Record.objects.filter(id=record_id)
    #template = loader.get_template('appstrava/record_detail.html')
    context = {'authors': authors,}
    return render(request, 'appstrava/record_detail.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("You're looking at record %s." % record_id)

def user_detail(request, user_name):
    records = Record.objects.filter(user__name=user_name).order_by('-pub_date')[:10]
    users = user_name
    #template = loader.get_template('appstrava/user_detail.html')
    context = {'records': records, 'users': users}
    #output = ', <br>'.join([r.record_name() for r in records])
    return render(request, 'appstrava/user_detail.html', context)
    #return HttpResponse(template.render(context, request))
# Homepage - displays your latest 5 entries
# Year-based archive
# Month-based archive
# day-based archive
# feed page - all records by all users, sorted by pub_date with newest higher.
# Top User by number of entries page: group by user, sort by count
# Top user by sports category - Running. Group by user, sort by amount total.



def year_top(request):
    current_period = timezone.now().year
    formatted_period = current_period
    records = Record.objects.filter(pub_date__year=current_period).order_by('-amount')[:10]
    #template = loader.get_template('appstrava/top.html')
    context = {'current_period': current_period, 'records': records, 'formatted_period': formatted_period}
    #output = ', <br>'.join([r.record_name() for r in year_records])
    return render(request, 'appstrava/top.html', context)
    #return HttpResponse(template.render(context, request))

def month_top(request):
    current_period = timezone.now().month
    records = Record.objects.filter(pub_date__month=current_period).order_by('-amount')[:10]
    formatted_period = timezone.now().strftime("%B")
    context = {'current_period': current_period, 'records': records, 'formatted_period': formatted_period}
    return render(request, 'appstrava/top.html', context)

def top(request):
    #filter(sport_type='jogging')
    formatted_period = 'All-Time in All-Sports'
    records = (Record.objects.annotate(Count('user', distinct=True)).order_by('-amount'))[:10]
    context = {'records': records, 'formatted_period': formatted_period}
    return render(request, 'appstrava/top.html', context)

def top_pullups(request):
    formatted_period = 'All-Time in Pull-ups'
    records = (Record.objects.filter(sport_type='Pull-ups').order_by('-amount'))[:10]
    context = {'records': records, 'formatted_period': formatted_period}
    return render(request, 'appstrava/top.html', context)

def top_crunches(request):
    formatted_period = 'All-Time in Crunches'
    records = (Record.objects.filter(sport_type='Crunches').order_by('-amount'))[:10]
    context = {'records': records, 'formatted_period': formatted_period}
    return render(request, 'appstrava/top.html', context)

def top_squats(request):
    formatted_period = 'All-Time in Squats'
    records = (Record.objects.filter(sport_type='Squats').order_by('-amount'))[:10]
    context = {'records': records, 'formatted_period': formatted_period}
    return render(request, 'appstrava/top.html', context)

def top_pushups(request):
    formatted_period = 'All-Time in Pushups'
    records = (Record.objects.filter(sport_type='Push-ups').order_by('-amount'))[:10]
    context = {'records': records, 'formatted_period': formatted_period}
    return render(request, 'appstrava/top.html', context)
   

def like(request, record_id):
    return HttpResponse("You liked record %s." % record_id)


#def homepage(request, user_name):
    #return HttpResponse('Youre at home page of %s.' % user_name)