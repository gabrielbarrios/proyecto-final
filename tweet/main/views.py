from django.shortcuts import render_to_response
from main.models import User


def users(request):
    users = User.objects.all()
    return render_to_response('users.html', {
        'users': users,
    })


