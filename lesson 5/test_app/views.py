from django.shortcuts import render

# Create your views here.
def date_time_response(request):
    return render(request, 'test_app/index.html')