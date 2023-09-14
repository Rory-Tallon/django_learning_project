from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .utils.graph_generator import graph_maker
import requests
import datetime
import time

# Create your views here.
def index(request):
    return render(request, "price_collector/index.html")


def collect_data(request):
    coin = request.POST["coin"]

    # date returns as YYYY-MM-DD
    date = request.POST["date"]
    date = date.split("-")

    try:    
        #this is just the date they entered in unix time
        print(date)
        to_date = str(int(time.mktime(datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 12, 0).timetuple())))
        #this is the date entered minus 30 days
        from_date =  str(int(to_date) - 2592000)

        request_str = "https://api.coingecko.com/api/v3/coins/"+coin+"/market_chart/range?vs_currency=usd&from="+from_date+"&to="+to_date

        
        r = requests.get(request_str)
        list_of_prices = r.json()["prices"]


        dates = []
        prices = []

        for i in list_of_prices:
            #need to convert the dates to datetime objects
            date_corrected = datetime.datetime.fromtimestamp(i[0]/1000)
            dates.append(date_corrected)
            #convert the unix time into normal time
            prices.append(i[1])

    except(KeyError):
        return render(request, "price_collector/index.html", {"error_message": "Invalid Date or Coin. Please enter a different one."})

    if r.status_code != 200:
        return render(request, "price_collector/index.html", {"error_message": "There has been an error collecting the price for that coin. Please try again"})

    #if all has gone well time to generate a graph
    graph = graph_maker(dates, prices)

    #most recent price is at the end of the list 
    price = str(prices[-1])
    return render(request, "price_collector/coin_price.html", {"name_of_coin": coin, "price": price, "graph": graph})

