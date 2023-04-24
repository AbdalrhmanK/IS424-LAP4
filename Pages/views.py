from django.shortcuts import render
from django.http import HttpResponse
price = 0 
tax_rate = 0 
# Create your views here.
def index(request) :
   return render(request , 'Pages/index.html')

def anyNumber(request , number) :
     try:
      price = int(number)
      tax = price * 1.15
      number = {'Tax':tax}
      return render(request , 'Pages/price.html' , number)
     except:
      return HttpResponse("<h1 style = \"color : red ;  text-align: center\";>Error please write valid Number</h1>")
def taxrate(request) :
     tax_rate = {'Tax_rate': '15%'}
     return render(request ,'Pages/percent.html' ,tax_rate  )   
       