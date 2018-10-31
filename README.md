<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Django Basic Views

### Setup Instruction

```bash
$ mkvirtualenv -p $(which python3) django_basic_views
$ pip install -r requirements.txt
```

You can now run the development server:

```bash
$ make runserver
```


### Your Tasks

The structure of the whole Django project is built for you. Your job is to implement the views that are under `django_basic_views/views.py`, and complete the proper URLs in `django_basic_views/urls.py`.

Running the development server with `$ make runserver`, you'll be able to test your views in the browser pointing to `http://localhost:8080/<some-path>`


#### 1. hello_world view:

Implement a simple view under `/hello-world` URL that returns a 'Hello World' string. Use the function `HttpResponse()` imported from Django.

<img src="https://user-images.githubusercontent.com/2788551/39313217-de76c182-4947-11e8-8aa8-e69b4e817526.png" width="50%" height="50%">

In order to check if you've successfully completed this task you can run the following command. Check code inside `tests.py` if you want to see how a (simple) test is written in Django.

```bash
$ make test
```


#### 2. current_date view:

Implement a view under `/date` URL that returns a string with current date using the datetime library.

<img src="https://user-images.githubusercontent.com/2788551/39313417-53b221e4-4948-11e8-943f-1042b21ad670.png" width="50%" height="50%">


#### 3. my_age view:

Implement a view under `/my-age/<year>/<month>/<day>` URL that returns a string with the format: "Your age is X years old" based on given /year/month/day that come as parameters.

<img src="https://user-images.githubusercontent.com/2788551/39313575-bc4deb34-4948-11e8-81a4-85d681ec5bb7.png" width="50%" height="50%">


#### 4. next_birthday view:

Implement a view under `/next-birthday/<birthday>` URL where `birthday` parameter is a string with the format "YYYY-MM-DD". The view should calculate the amount of days until next birthday and return a string with the format "'Days until next birthday: XYZ'"

<img src="https://user-images.githubusercontent.com/2788551/39313769-3019a1c0-4949-11e8-8688-6184cdbcf187.png" width="50%" height="50%">


#### 5. profile view:

Implement a view under `/profile` URL that renders the `profile.html` sending the given dictionary as context. You'll need to use the `render()` function imported from Django. Also make sure to complete the template with the context data in the proper places.

<img src="https://user-images.githubusercontent.com/2788551/39314078-ce9bff0a-4949-11e8-9f71-87becbd3baae.png" width="50%" height="50%">


#### 6. authors and author views:

The goal for this task is to practice routing between two URLs.
You will have:
* `/authors` --> contains a list of Authors (template is provided to you)
* `/author/<authors_last_name>` --> contains the detail for given author, using the AUTHORS_INFO provided to you.

First view just have to render the given `authors.html` template sending the AUTHORS_INFO as context.

Second view has to take the `authors_last_name` provided in the URL, look for for the proper author info in the dictionary, and send it as context while rendering the `author.html` template. Make sure to complete the given `author.html` template with the data that you send.

<img src="https://user-images.githubusercontent.com/2788551/39314260-3d6cd2f6-494a-11e8-9a05-7533868d64a4.png" width="50%" height="50%">

<img src="https://user-images.githubusercontent.com/2788551/39314282-489c6718-494a-11e8-9734-9be58ea9807e.png" width="50%" height="50%">
