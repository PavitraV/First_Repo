from django.shortcuts import render
import csv
from testing.models import Load
from django.db import connection
import json 
# connection.connection.text_factory = lambda x: (x, "utf-8", "ignore")
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def loadData(request):
	csv_filepathname = "C:\Users\Pavitra\Downloads\Test.csv"

	dataReader = csv.reader(open(csv_filepathname), delimiter=',')
	next(dataReader,None)
	for row in dataReader:
		load=Load()
		load.ROWID = row[0]
		load.OrderID = row[1]
		load.OrderDate = row[2]
		load.OrderPri = row[3]
		load.OrderQt = row[4]
		load.Sales = row[5]
		load.Disc = row[6]
		load.ShipMode =row[7]
		load.Profit = row[8]
		load.UnitPrice = row[9]
		load.Cost = row[10]
		load.Name = row[11]
		load.Province = row[12]
		load.Region =row[13]
		load.CustSeg = row[14]        
		load.Category = row[15]
		load.SubCat = row[16]
		load.ProdName = row[17]
		load.ProdCont =row[18]
		load.Margin = row[19]
		load.ShipDate = row[20]
		load.save()
	return HttpResponse("Done")

def viewData(request):
	loading = Load.objects.values('Category').distinct()
	#loading = Load.objects.values('SubCat').distinct()
	#serialized_obj = serializers.serialize('json', [ loading ])
	loading = json.dumps(list(loading))
	return render(request,'testing/test.html',{'loading':loading})