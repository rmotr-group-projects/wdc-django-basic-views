from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    return HttpResponse("Hello World")


# Use /date URL
def current_date(request):
    """
        Return a string with current date using the datetime library.

        i.e: 'Today is 5, January 2018'
    """
    today = datetime.now().strftime("Today is %d, %B %Y")
    return HttpResponse(today)


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    your_age = int((datetime.now() - datetime(year,month,day)).days / 365)

    return HttpResponse("Your age is {your_age} years old".format(your_age=your_age))


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    birthday_to_datetime = datetime.strptime(birthday,"%Y-%m-%d")
    time_now = datetime.now()
    next_birthday = datetime(time_now.year, birthday_to_datetime.month, birthday_to_datetime.day) - time_now
    return HttpResponse("Days until next birthday: {next_birthday}".format(next_birthday=next_birthday.days))


# Use /profile URL
def profile(request):
    """
        This view should render the template 'profile.html'. Make sure you return
        the correct context to make it work.
    """
    profile_context = {
        'my_name': "Jordan Schultz",
        'my_age': 27
    }
    return render(request,'profile.html',profile_context)



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
    for author in AUTHORS_INFO.keys():
        print(author)
        if author.lower() == authors_last_name.lower():
            author_context = AUTHORS_INFO[author]
    return render(request,'author.html',author_context)
