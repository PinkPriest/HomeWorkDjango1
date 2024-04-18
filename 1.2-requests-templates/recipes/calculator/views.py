from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:


def omlet(request):
    context = {'recipe': DATA.get('omlet')}
    servings = request.GET['servings']
    ingredients = context.get('recipe')
    for ing in ingredients:
        ingredients[ing] *= int(servings)
    return render(request, 'calculator/index.html', context=context)


def pasta(request):
    context = {'recipe': DATA.get('pasta')}
    servings = request.GET['servings']
    ingredients = context.get('recipe')
    for ing in ingredients:
        ingredients[ing] *= int(servings)
    return render(request, 'calculator/index.html', context=context)


def buter(request):
    context = {'recipe': DATA.get('buter')}
    servings = request.GET['servings']
    ingredients = context.get('recipe')
    for ing in ingredients:
        ingredients[ing] *= int(servings)
    return render(request, 'calculator/index.html', context=context)

def hello(request):
    return HttpResponse('Hello')
render(request, 'calculator/index.html', context)

