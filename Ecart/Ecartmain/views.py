from django.shortcuts import render

from django.http import HttpResponse

from .models import product,KHOBOR,orders,orderupdate
from math import ceil
import json

from django.core.mail import send_mail
import zerosms




def index(request):
    #Product = product.objects.all()
    #print(Product)

   # n = len(Product)
    #nslides = n // 4 + ceil((n / 4) - (n // 4))
    allprods=[]
    catprods=product.objects.values('category','id')
    cats={item['category']for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])

   # params = {'NO_of_slides': nslides, 'range': range(1, nslides), 'products': Product}
    #allprods=[[Product,range(1,nslides),nslides],[Product,range(1,nslides),nslides]]
    params={'allprods':allprods}

    return render(request, 'Ecartmain/index.html', params)



def searchmatch(query, item):
    if query in item.product_name.lower() or query in item.category.lower() or query in item.product_desc:

      return True


def search(request):
    query=request.GET.get('search')
    if len(query)==0:
        return HttpResponse("<html><head><script> alert('No search result');window.location.href='http://127.0.0.1:8000/shop/';</script></head></html>")
    # Product = product.objects.all()
    # print(Product)

    # n = len(Product)
    # nslides = n // 4 + ceil((n / 4) - (n // 4))
    allprods = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp= product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchmatch(query,item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
         allprods.append([prod, range(1, nslides), nslides])

    # params = {'NO_of_slides': nslides, 'range': range(1, nslides), 'products': Product}
    # allprods=[[Product,range(1,nslides),nslides],[Product,range(1,nslides),nslides]]
    params = {'allprods': allprods}
    return render(request, 'Ecartmain/search.html', params)

def about(request):
    return render(request, "Ecartmain/about.html")


def contact(request):
    if request.method=="POST":

         name=request.POST['name']
         email = request.POST['email']
         mobile= request.POST['phone']
         Query = request.POST['Query']
         Eid=request.POST['E_id']
         print(mobile)

         K=KHOBOR(name=name,phone=mobile,email=email,Eid=Eid,query=Query)
         K.save()



    return render(request, "Ecartmain/contact.html")


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        print(email,orderId)
        try:
            order = orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{hi}')


    return render(request, 'Ecartmain/tracker.html')




def productView(request,id_ac):
    prods = product.objects.filter(id=id_ac)
    print(prods)
    return render(request, "Ecartmain/productview.html",{'product_temp':prods[0]})


def checkout(request):
    if request.method=="POST":
        try:
         item_json = request.POST['itemsjson']
         name = request.POST['Name']
         email = request.POST['email']
         address = request.POST['address']+""+request.POST['address2']
         zipcode = request.POST['zip']
         state = request.POST['state']
         city = request.POST['city']
         phone = request.POST['phone']

         ord=orders(item_json=item_json,name=name,email=email,Address=address,Zipcode=zipcode,state=state,city=city,phone=phone)
         ord.save()
         #send_mail('no-reply(Order confirmation)', "Thanks! {name}\nYour order Hasbeen placed.Your can track Your Order using OrderID\n\t\twith regrads~ Ecartmain", EMAIL_HOST_USER, [email], fail_silently=False)
         update=orderupdate(order_id=ord.order_id,update_desc="Your order hasbeen placed ready to ship:")
         update.save()
         thank=True
         id=ord.order_id
         name1=ord.name

         from django.conf.global_settings import EMAIL_HOST_USER
         send_mail('no-reply(Order confirmation)',
                   f"Thanks! {name} \U0001F603 \nYour order Hasbeen placed.Your Order Id is: {id}  Your can track Your Order using OrderID\n"
                   f"Your Ordered item is {item_json}\t with regrads~ Ecartmain",
                   EMAIL_HOST_USER, [email], fail_silently=False)



         return render(request,"Ecartmain/orderscnfrm.html",{'thanks':thank,'id':id,'name1':name})
        except:
            return HttpResponse("FILL CORRECTLY:")

    return render(request, "Ecartmain/checkout.html")

