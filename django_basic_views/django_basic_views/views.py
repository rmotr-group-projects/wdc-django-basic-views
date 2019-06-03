from datetime import datetime, timedelta, date

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Context


# Use /hello-world URL
def hello_world(request):
    """Return a 'Hello World' string using HttpResponse"""
    return HttpResponse('<h1>Hello World</h1>')


# Use /date URL
def current_date(request):
    """
        Return a string with current date using the datetime library.

        i.e: 'Today is 5, January 2018'
    """
    d = datetime.today()
    return HttpResponse('<h1>Today is {}</h1>'.format(d.strftime('%B %d, %Y')))


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    today = datetime.today()
    y = today.year
    m = today.month
    d = today.day
    age = int(y) - int(year) - ((m, d) < (int(month), int(day)))
    return HttpResponse('<h1> Your age is {} years old</h1>'.format(age))


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    dob = birthday.split('-')
    dob_year = int(dob[0])
    dob_month = int(dob[1])
    dob_day = int(dob[2])
    today = date.today()
    y = today.year
    nextbday = date(y, dob_month, dob_day)
    bday = (nextbday - today).days
    if today < nextbday:
        return HttpResponse('<h1>Days until next birthday: {}</h1>'.format(bday))
    elif today == nextbday:
        return HttpResponse('<h1>Happy Birthday</h1>')
    else:
        nextbday = date(y+1, dob_month, dob_day)
        bday = (nextbday - today).days
        return HttpResponse('<h1>Days until next birthday: {}</h1>'.format(bday))


# Use /profile URL
def profile(request):
    """
        This view should render the template 'profile.html'. Make sure you return
        the correct context to make it work.
    """
    return render(request, 'profile.html', context={'my_name': 'Danielle','my_age': 35})



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
    return render(request, 'authors.html', context=AUTHORS_INFO)


def author(request, authors_last_name):
    author_found = AUTHORS_INFO[authors_last_name]
    full_name = author_found['full_name']
    born = author_found['born']
    nationality = author_found['nationality']
    notable_work = author_found['notable_work']
    return render(request, 'author.html', context={'full_name': full_name, 'born': born, 'nationality': nationality, 'notable_work': notable_work})
    
