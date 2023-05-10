from django.shortcuts import render


def handle_404(request, exception):
    context = {'login': request.session.get('login')}
    return render(request, '404.html', context, status=404)


def handle_500(request):
    context = {'login': request.session.get('login')}
    return render(request, '500.html', context, status=500)