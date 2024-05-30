from django.shortcuts import render


def index(request):
    return render(request, 'GAK/index.html')


def calculate(request):
    result = None
    side_length = None
    if request.method == 'POST':

        if 'reset' in request.POST:
            side_length = ''
            result = None
        else:

            try:
                side_length = int(request.POST.get('side_length', ''))
                result = side_length ** 2
            except (ValueError, TypeError):
                result = "Invalid input"
    return render(request, 'GAK/calculate.html', {'result': result, 'side_length': side_length})

