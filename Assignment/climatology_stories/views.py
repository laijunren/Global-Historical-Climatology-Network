from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.core.paginator import Paginator
from .models import Climate, Year
import csv
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'climatology_stories/index.html')


def years(request):
    try:
        year = int(request.GET.get('year', None))
    except:
        year = 1880
        years = Year.objects.all()
        paginator = Paginator(years, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'climatology_stories/years.html', {'page_obj': page_obj, 'year': year})
    else:
        if year:
            years = Year.objects.filter(year=year)
        else:
            years = Year.objects.all()
        paginator = Paginator(years, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'climatology_stories/years.html', {'page_obj': page_obj, 'year': year})


def year_detail(request, yearid):
    climates = Climate.objects.filter(year=yearid)
    paginator = Paginator(climates, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'climatology_stories/climate_data.html', {'page_obj': page_obj})


def dashboard(request):
    years = range(1880, 2017, 1)
    months = range(1, 13, 1)
    # lats = ["85-90N", "80-85N", "75-80N", "70-75N", "65-70N", "60-65N", "55-60N", "50-55N", "45-50N", "40-45N", "35-40N", "30-35N", "25-30N", "20-25N", "15-20N", "10-15N", "5-10N", "0-5N", "0-5S", "5-10S", "10-15S", "15-20S", "20-25S", "25-30S", "30-35S", "35-40S", "40-45S", "45-50S", "50-55S", "55-60S", "60-65S", "65-70S", "70-75S", "75-80S", "80-85S", "85-90S"]
    lats = ["85-90N", "80-85N", "75-80N", "70-75N", "65-70N", "60-65N", "55-60N", "50-55N", "45-50N", "40-45N", "35-40N", "30-35N", "25-30N", "20-25N", "15-20N", "10-15N", "5-10N", "0-5N",
            "0-5S", "5-10S", "10-15S", "15-20S", "20-25S", "25-30S", "30-35S", "35-40S", "40-45S", "45-50S", "50-55S", "55-60S", "60-65S", "65-70S", "70-75S", "75-80S", "80-85S", "85-90S"]
    yearid = 1880
    monthid = 1
    latid = "35-40S"

    yearid2 = 1880
    monthid2 = 5
    latid2 = "35-40S"
    if request.method == "POST":
        if (request.POST.get('year') != None):
            yearid = int(request.POST.get('year'))
            monthid = int(request.POST.get('month'))
            latid = request.POST.get('lat')
        if (request.POST.get('year2') != None):
            yearid2 = int(request.POST.get('year2'))
            monthid2 = int(request.POST.get('month2'))
            latid2 = request.POST.get('lat2')

    climate = Climate.objects.filter(
        year=yearid, month=monthid, lat=latid).first()
    if (climate.lon_175_180W == -9999):
        climate.lon_175_180W = -99
    if (climate.lon_170_175W == -9999):
        climate.lon_170_175W = -99
    if (climate.lon_165_170W == -9999):
        climate.lon_165_170W = -99
    if (climate.lon_160_165W == -9999):
        climate.lon_160_165W = -99
    if (climate.lon_155_160W == -9999):
        climate.lon_155_160W = -99
    if (climate.lon_150_155W == -9999):
        climate.lon_150_155W = -99

    climate2 = Climate.objects.filter(
        year=yearid2, month=monthid2, lat=latid2).first()
    if (climate2.lon_175_180W == -9999):
        climate2.lon_175_180W = -99
    if (climate2.lon_170_175W == -9999):
        climate2.lon_170_175W = -99
    if (climate2.lon_165_170W == -9999):
        climate2.lon_165_170W = -99
    if (climate2.lon_160_165W == -9999):
        climate2.lon_160_165W = -99
    if (climate2.lon_155_160W == -9999):
        climate2.lon_155_160W = -99
    if (climate2.lon_150_155W == -9999):
        climate2.lon_150_155W = -99

    return render(request, 'climatology_stories/dashboard.html', {'months': months, 'years': years, 'lats': lats, 'climate': climate, 'climate2': climate2})


def climate_data(request):
    # Add logic to handle climate_data requests here.
    # context = {}

    try:
        year = int(request.GET.get('year', None))
    except:
        year = 1880
        climates = Climate.objects.all()
        paginator = Paginator(climates, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'climatology_stories/climate_data.html', {'page_obj': page_obj, 'year': year})
    else:
        if year:
            climates = Climate.objects.filter(year=year)
        else:
            climates = Climate.objects.all()
        paginator = Paginator(climates, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'climatology_stories/climate_data.html', {'page_obj': page_obj, 'year': year})


def climate_data_graph(request, yearid, monthid, latid):

    yearid = int(request.POST.get('year'))
    monthid = int(request.POST.get('month'))
    latid = request.POST.get('lat')
    climate = Climate.objects.filter(
        year=yearid, month=monthid, lat=latid).first()

    return render(request, 'climatology_stories/dashboard.html', {'climate': climate})


def settings(request):
    context = {}
    return render(request, 'climatology_stories/settings.html', context)


def download(request):
    year = request.GET.get('year')
    data = Climate.objects.filter(year=year)

    # get all model fields
    model_fields = Climate._meta.get_fields()

    # create a csv response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{year}.csv"'

    # write data to csv
    writer = csv.writer(response)
    writer.writerow([field.name for field in model_fields])
    for obj in data:
        writer.writerow([getattr(obj, field.name) for field in model_fields])

    return response
