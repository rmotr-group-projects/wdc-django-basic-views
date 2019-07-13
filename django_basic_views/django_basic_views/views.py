from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    """Return a 'Hello World' string using HttpResponse"""
    
    return HttpResponse("Hello World", status=200)



# Use /date URL
def current_date(request):
    """
        Return a string with current date using the datetime library.

        i.e: 'Today is 5, January 2018'
    """
    now = datetime.now()
    current_date = now.strftime("Today is %-d, %B %Y")
    return HttpResponse(current_date)


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    date_string = ("{} {} {}".format(year, month, day))
    birthdate = datetime.strptime(date_string, '%Y %m %d')
    now = datetime.now()
    age_days = now - birthdate
    age_years = age_days.days / 365.25
    
    return_string = "Your age is {} years old".format(round(age_years))
    return HttpResponse(return_string)


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    date_string = "{}".format(birthday)
    birthday_date = datetime.strptime(date_string, '%Y-%m-%d')
    now = datetime.now()
    days_until = birthday_date - now
    return_string = 'Days until next birthday: {}'.format(days_until.days)
    return HttpResponse(return_string)


# Use /profile URL
def profile(request):
    """
        This view should render the template 'profile.html'. Make sure you return
        the correct context to make it work.
    """
    context = {'my_name':"Alex", 'my_age': 27}
    return render(request, 'profile.html', context=context)



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
    
    return render(request, "authors.html", context=AUTHORS_INFO)
    


def author(request, authors_last_name):
    
    return render(request, 'author.html', context=AUTHORS_INFO[authors_last_name])

    
        
    
    
    pass
