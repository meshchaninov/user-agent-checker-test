from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime
from .models import Visitor, UserAgent


def index(request):
    user_agent = request.user_agent
    user = None if request.user.is_anonymous else request.user
    Visitor.objects.create(
        address = request.META['REMOTE_ADDR'],
        user_agent = UserAgent.objects.create(
            is_mobile = user_agent.is_mobile,
            is_touch = user_agent.is_touch_capable,
            is_tablet = user_agent.is_tablet,
            is_pc = user_agent.is_pc,
            is_bot = user_agent.is_bot,
            browser_family = user_agent.browser.family,
            browser_version = user_agent.browser.version_string,
            os_family = user_agent.os.family,
            os_version = user_agent.os.version_string,
            device_family = user_agent.device.family
        ),
        user = user
    )
    visitors_list = Visitor.objects.all().order_by('id')

    paginator = Paginator(visitors_list, 5)
    page = request.GET.get('page')
    if page is None:
        page = paginator.num_pages
    visitors = paginator.get_page(page)

    return render(request, "index.html", {"visitors": visitors})