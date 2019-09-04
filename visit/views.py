from django.shortcuts import render
from datetime import datetime
from .models import Visitor


def index(request):
    visitor = Visitor.objects.create(
        user_agent = request.headers.get('User-Agent'),
        address = request.META['REMOTE_ADDR'] 
    )

    return render(request, "index.html", {"visitor": visitor})