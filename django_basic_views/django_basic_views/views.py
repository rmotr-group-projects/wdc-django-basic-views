from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


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
    today = datetime.now()
    response =  f"Today is {today.day}, {today:%B} {today:%Y}"
    return HttpResponse(response)


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    try:
        datetime(year, month, day)
    except:
        raise ValueError("Invalid Birthday")
    now = datetime.now()
    age = now.year - year
    if now.month - month < 0:
        age -= 1
    elif now.month == month and now.day - day < 0:
        age -= 1
    return HttpResponse(f"Your age is {age} years old")


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    now = datetime.now()
    try:
        dt_birthday = datetime.strptime(birthday, "%Y-%m-%d")
    except:
        raise ValueError("Invalid Birthday. Birthday must be in the format YYYY-MM-DD")
    next_birthday = datetime(now.year, dt_birthday.month, dt_birthday.day)
    if now > next_birthday:
        next_birthday += timedelta.years(1)
    days_til_next_birthday = (next_birthday - now).days + 1
    return HttpResponse(f"Days until next birthday: {days_til_next_birthday}")


# Use /profile URL
def profile(request):
    """
        This view should render the template 'profile.html'. Make sure you return
        the correct context to make it work.
    """
    my_age = datetime.now().year - 1977
    if datetime.now().month - 8 < 0:
        my_age -= 1
    elif datetime.now().day - 3 < 0:
        my_age -= 1

    context = {"my_name": "Dan Martz", "my_age": my_age}
    return render(request,'profile.html', context=context)



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
    return render(request, 'author.html', context=AUTHORS_INFO[authors_last_name])
