from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    """Return a 'Hello World' string using HttpResponse"""
    # you have to add a return response
    # In contrast to HttpRequest objects, which are created automatically by Django, 
    # HttpResponse objects are your responsibility.
    # Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
    return HttpResponse('Hello World')


# Use /date URL
def current_date(request):
    """
        Return a string with current date using the datetime library.

        i.e: 'Today is 5, January 2018'
    """
    dt = datetime.now()                                        #Return the current local date and time.
    return HttpResponse(dt.strftime('Today is %d, %B %Y'))     #Return a string representing the date and time
    # Today is 10, January 2018


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
#### solution had try and except, what's the better way to handle this again?
    try:
        birthday = datetime(year=year, month=month, day=day)
    except ValueError:
        return HttpResponseBadRequest()
    
    delta = datetime.now() - birthday
    return HttpResponse("Your age is {} years old".format(int(delta.days / 365)))
    # https://i4-p39105.proxy.rmotr.com/my-age/2019/06/25

# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    # if you don't get the correct format return a bad request
    try:
        #     dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
    except ValueError:
        return HttpResponseBadRequest()

    # always get today's date
    today = datetime.now()
    
    #birthday is a datetime object that you can replace specific attributes
    #you check and see if the birthday has passed this current year
    birthday_next = birthday.replace(year=today.year)
    if today > birthday_next:
        # birthday passed this current year
        birthday_next = birthday_next.replace(year=today.year + 1)
   
    days_until_bday = birthday_next - today
    return HttpResponse("Days until next birthday: {}".format(days_until_bday.days + 1))
    #return HttpResponse("DEBUG: today: {} birthday_next: {} (days until: {})".format(today,birthday_next,days_until_bday.days + 1))
    
### Is bad request the HTTP ERROR 400?
    
### When do we use name in urls.py?

# Use /profile URL
def profile(request):
    """
        This view should render the template 'profile.html'. Make sure you return
        the correct context to make it work.
    """
    context_dict = {'my_name': 'Stephen King', 'my_age': 71}
    return render(request, 'profile.html', context=context_dict)
    # My name is {{my_name}} and I'm {{my_age}} years old.



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
    # HARD CODED HTML!
    # {% url 'author' authors_last_name='borges' %}

def author(request, authors_last_name):
    return render(request, 'author.html', context=AUTHORS_INFO[authors_last_name])

### HOW DOES THIS WORK?

# https://medium.com/@samuh/using-jinja2-with-django-1-8-onwards-9c58fe1204dc

# <p><a href="{% url 'authors' %}">Back to Authors</a></p>

# does it search for the URL?

# is it using the path from urls.py ???