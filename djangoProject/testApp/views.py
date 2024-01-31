from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tracks = [
    {"id": 1, "Name": "OS"},
    {"id": 2, "Name": "Python"},
    {"id": 3, "Name": "Java"},
    {"id": 4, "Name": ".Net"},
    {"id": 5, "Name": "AI"},
]


# http-request ,return http-response
def hello(request):
    print(request.method)
    return HttpResponse(
        """ <h1>Welcome To <span  style='color:red;'>Django</span> Application</h1>"""
    )


def track_list(request):
    # return HttpResponse(""" <h1><span style='color:red;'>Track List</span></h1>""")
    # return HttpResponse(tracks)
    context = {}
    context["tracks"] = tracks
    return render(request, "testApp/index.html", context)


def track_details(request, trackID):
    # print(request)
    # return HttpResponse(
    #     f""" <h1><span style='color:red;'>Track Details {trackID}</span></h1>"""
    # )
    track = filter(lambda t: t["id"] == trackID, tracks)
    track = list(track)
    if track:
        return HttpResponse(track)
    else:
        return HttpResponse("<span style='color:red;'>This Id Not Found</span>")
