from django.shortcuts import render


def index(request):
    name = "Django"

    if request.method == 'GET':
        return render(request, 'base.html', {'name': name})
    else:
        pass
