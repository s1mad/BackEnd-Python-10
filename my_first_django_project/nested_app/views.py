"""
Модуль для создания представлений
"""

from django.http import HttpResponse


def nested_view1(request):
    """
    Представление 1 для nested_app.
    """
    return HttpResponse("<h1>Nested View 1</h1>")


def nested_view2(request):
    """
    Представление 2 для nested_app.
    """
    return HttpResponse("<h1>Nested View 2</h1>")
