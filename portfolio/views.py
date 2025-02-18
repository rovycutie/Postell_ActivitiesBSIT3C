from django.shortcuts import render
def index(request):
    return render(request, "pages/portfolio.html")

from django.utils.timezone import now

def my_view(request):
    return render(request, 'my_template.html', {'timestamp': now().timestamp()})
