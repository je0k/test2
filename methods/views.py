from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def checkGet(request):
    errors = []

    if request.method != "GET":
	errors.append("Your request is not a GET request.")
    if len(request.GET) < 2:
	errors.append("Your request contains fewer than 2 GET parameters.")
    if not "andrewid" in request.GET:
	errors.append("Your request does not contain an andrewid parameter.")
    if not "color" in request.GET:
	errors.append("Your request does not contain a color parameter.")

    if len(errors) > 0:
	return render_to_response("incorrect.html", {"errors":errors})

    return render_to_response("correct.html", {})

@csrf_exempt
def checkPost(request):
    errors = []

    if request.method != "POST":
	errors.append("Your request is not a POST request.")
    if len(request.POST) < 2:
	errors.append("Your request contains fewer than 2 POST parameters.")
    if not "andrewid" in request.POST:
	errors.append("Your request does not contain an andrewid parameter.")
    if not "color" in request.POST:
	errors.append("Your request does not contain a color parameter.")

    if len(errors) > 0:
	return render_to_response("incorrect.html", {"errors":errors})

    return render_to_response("correct.html", {})

@csrf_exempt
def index(request):
    return render_to_response("index.html", {})
