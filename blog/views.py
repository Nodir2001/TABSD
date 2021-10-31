from django.shortcuts import render
from mysite import urls
def post_list(request):
    return render(request, 'html/post_list.html', {})