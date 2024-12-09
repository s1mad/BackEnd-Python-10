"""
Модуль для создания представлений
"""

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect


def hello_world(request, name: str):
    """
    Возвращает приветствие с именем и возрастом.
    """
    response = HttpResponse()
    response.set_cookie('username', name)
    age = request.GET.get('age', 'unknown')
    return HttpResponse(f"<h1>Hello, {name}! You are {age} years old.</h1>")


def redirect_example(request):
    """
    Перенаправляет на представление hello_world с параметрами по умолчанию.
    """
    return redirect('hello_world_with_name', name='Guest')


def json_example(request):
    """
    Возвращает JSON-ответ с данными пользователя.
    """
    data = {"name": "John", "age": 30}
    return JsonResponse(data)


def show_cookies(request):
    """
    Отображает все куки пользователя.
    """
    cookies = request.COOKIES
    return HttpResponse(f"<h1>Cookies: {cookies}</h1>")
