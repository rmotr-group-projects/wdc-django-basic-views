from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest
import time
from datetime import date

# Use /hello-world URL
def hello_world(request):
    """Return a 'Hello World' string using HttpResponse"""
    return HttpResponse("Hello World")



# Use /date URL
def current_date(request):
    """
        Return a string with current date using the datetime library.

        i.e: 'Today is 5, January 2018'
    """
 
    day = datetime.today().day
    month = datetime.today().strftime("%B")
    year = datetime.today().year
    td = "Today is {}, {} {}".format(day,month,year)
    return HttpResponse(td)


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year,month,day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    
    today = datetime.today()
    age = today.year - year - ((today.month,today.day) < (month,day))
    your_age = "Your age is {} years old".format(age)
    return HttpResponse(your_age)


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    # inspire from this https://docs.python.org/2/library/datetime.html 
    #b_year = birthday[:4]
    b_month = birthday[5:7]
    b_day = birthday[8:10]

    today = date.today()
    my_birthday = date(today.year,int(b_month),int(b_day))
    if my_birthday < today:
        my_birthday = my_birthday.replace(year=today.year + 1)
    time_to_birthday = abs(my_birthday - today)
    how_many_days = time_to_birthday.days

    return HttpResponse("Days until next birthday: {}".format(how_many_days))

 

# Use /profile URL
def profile(request):
    """
        This view should render the template 'profile.html'. Make sure you return
        the correct context to make it work.
    """
    return render(request,'profile.html',{'my_name': "Guido van Rossum",
    'my_age': 62})



"""
    The goal for next task is to practice routing between two URLs.
    You will have:
        - /authors --> contains a list of Authors (template is provided to you)
        - /author/<authors_last_name> --> contains the detail for given author,
        using the AUTHORS_INFO provided below.

    First view just have to render the given 'authors.html' template sending the
    AUTHORS_INFO as context.

    Second view has to take the authors_last_name provided in the URL, look for
    for the proper author info in the dictionary, and send it as context while
    rendering the 'author.html' template. Make sure to complete the given
    'author.html' template with the data that you send.
"""
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
    
    return render(request,'authors.html')


def author(request, authors_last_name):
    
    for key in AUTHORS_INFO:
        if key == authors_last_name:
             full_name =AUTHORS_INFO[key]['full_name']
             born =AUTHORS_INFO[key]['born']
             nationality =AUTHORS_INFO[key]['nationality']
             notable_work =AUTHORS_INFO[key]['notable_work']

    return render(request,'author.html',{
        'full_name':full_name,
        'born': born,
        'nationality':nationality,
        'notable_work':notable_work
    })
