from django.shortcuts import render
from .utils import get_info

def index(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        country = request.POST.get("country")
        city = request.POST.get("city")

        if name and country and city:
            result = get_info(name, country, city)
            context["result"] = result
        else:
            context["error"] = "Please provide name, country, and city."

    return render(request, "timezone_app/index.html", context)
