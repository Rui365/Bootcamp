from django.shortcuts import render
from django.http import HttpResponse
from api.models import nasa
import requests
from django.utils.dateparse import parse_date
from django.shortcuts import redirect

# Create your views here.
def create_comment(request):
    # if get request direct to form
    # if post request save object and then go to detail view of object
    if(request.method == 'GET'):
        api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"
        exp_date = request.GET.get("nasa-date")
        #date = "2017-06-13" #TODO change
        r = requests.get(f'https://api.nasa.gov/planetary/apod?date={exp_date}&api_key={api_key}')
        url = r.json()["url"]
        return render(request, 'create_comment.html', {'image_url': url, "date": exp_date})

    elif(request.method == 'POST'):
        not_comment = request.POST.get("comment")
        rating = request.POST.get("rating")
        date = request.POST.get("date")
        print(not_comment, rating, date)
        # Created nasa object
        nasa_comment = nasa.objects.create(comment = not_comment, rating = rating, date = parse_date(date) )
        # Redirect to detail view
        redirect_url = f'/nasa/comment/detail/{nasa_comment.id}'
        print(redirect_url)
        return redirect(redirect_url)
    else:
        print("How did you come here?")


def detail_view(request,nasa_id):
    comment_detail = nasa.objects.get(id=nasa_id)

    return render(request,'comment_detail.html', {"comment_detail": comment_detail})

def comment_list(request):
    nasa_comments = nasa.objects.all()
    return render(request, 'comment_list.html', {"nasa_comments": nasa_comments})

def pick_date(request):
    # if the method is get render the date date_picker form
    if(request.method == "GET"):
        return render(request, 'date_picker.html')
        # Render date_picker
    elif(request.method == "POST"):
        date_p = request.POST.get('nasa-date')
        # get the date from the post data and redirect to create_comment
    # if the method is post get the date from the post data
    # and redirect to the create_comment view with the date as a query parameter

    return redirect(f'/nasa/comment/?nasa-date={date_p}')
