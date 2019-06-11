from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    return HttpResponse('Hello World')
  


# Use /date URL
def current_date(request):
    current_day = datetime.now()
    string_date = current_day.strftime('%d, %B %Y')
    return HttpResponse("Today is {}".format(string_date))


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    dob = datetime.strptime('{year} {month} {day}'.format(year=year,month=month,day=day), '%Y %m %d')
    age = datetime.now() - dob
    str_age = int(age.total_seconds()/60/60/24/365)	
    return HttpResponse("Your age is {age} old".format(age=str_age))
    

# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    dob = datetime.strptime(birthday,'%Y-%m-%d')
    next_bday = datetime.strptime('{}{}{}'.format(datetime.now().year,dob.month,dob.day),'%Y%m%d')
	
    if next_bday < datetime.now():
        next_bday = datetime.strptime('{}{}{}'.format(datetime.now().year + 1 ,dob.month,dob.day),'%Y%m%d')  
    return HttpResponse('Days untill next birthday: {days}'.format(days=(next_bday - datetime.now()).days))

# Use /profile URL
def profile(request):
    return render(request, 'profile.html',{'my_name': 'Tom',
											'my_age': '33'})

AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
    }
}

# Use provided URLs, don't change them
def authors(request):
    return render(request, 'authors.html')


def author(request, authors_last_name):
    return render(request, 'author.html',{'full_name':AUTHORS_INFO[authors_last_name]['full_name'],
										'born': AUTHORS_INFO[authors_last_name]['born'],
										'nationality': AUTHORS_INFO[authors_last_name]['nationality'],
										'notable_work': AUTHORS_INFO[authors_last_name]['notable_work']
										})
