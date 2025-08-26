import datetime
import random
import uuid
from django.shortcuts import render,redirect,get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from common.models import userregistration,servicename,addservice,clothtype
from customer.models import Cart,Booking,Feedback
from django.contrib.auth import login,logout,authenticate # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
# Create your views here.
@login_required
def customer(request):
    return render(request, 'Customer/customer.html')

@login_required
def cprofile(request,un):
    if request.method == 'POST':
        customername = request.POST['cname']
        custphone = request.POST['pn']
        custaddress = request.POST['address']
        updatedetails=userregistration.objects.get(username=un)
        updatedetails.Name=customername
        updatedetails.PhoneNumber=custphone
        updatedetails.address=custaddress
        updatedetails.save()
        return redirect('/customer')
    else:
        fetchdetails=userregistration.objects.get(username=un)
        return render(request, 'Customer/cprofile.html',{'fetch':fetchdetails})
    
@login_required
def csl(request,un):
    fetchdetails = servicename.objects.all()
    return render(request, 'Customer/csl.html',{'fetch':fetchdetails})

@login_required
def cdetails(request,un):
    fetchdetails = addservice.objects.filter(servicename=un)
    return render(request, 'Customer/cdetails.html',{'fetch':fetchdetails})

@login_required
def col(request, un):
    if request.method == 'POST':
        serivceselection = request.POST['serviceselect']
        clothselection = request.POST['clothselect']
        quan = int(request.POST['quantity'])

        service_obj = servicename.objects.get(servicename=serivceselection)
        clothtype_obj = clothtype.objects.get(typeofcloth=clothselection)
        addservice_obj = addservice.objects.get(servicename=service_obj, typeofcloth=clothtype_obj)

        price = quan * addservice_obj.price

        latest_booking = Cart.objects.all().order_by('-bookingid').first()
        if latest_booking:
            bookingid = str(int(latest_booking.bookingid) + 1).zfill(8)
        else:
            bookingid = "00000001"

        storedata = Cart(
            bookingid=bookingid,
            servicename=serivceselection,
            typeofcloth=clothselection,
            nopieces=quan,
            price=price,
            username=un
        )
        storedata.save()

        return redirect('cart', un=un)

    else:
        fetchdetails = servicename.objects.all()
        fetchd = clothtype.objects.all()
        return render(request, 'Customer/col.html', {
            'servicefetch': fetchdetails,
            'ctfetch': fetchd
        })

@login_required
def cart(request, un):
    fetchdetails = Cart.objects.filter(username=un)   # fetch only that user's cart
    return render(request, 'Customer/cart.html', {'fetch': fetchdetails})

@login_required
def booking(request, un):
    booking_id = uuid.uuid4().hex[:8].upper() 
    booking_date = datetime.date.today()
    fetchdetails = userregistration.objects.get(username=un)
    fetch = Cart.objects.filter(username=un)
    totalprice = sum(f.price for f in fetch)

    container = {
        'fetch2': fetchdetails,
        'fetch1': fetch,
        'totalprice': totalprice,
        'bookingid': booking_id,
        'booking_date': booking_date
    }

    if request.method == 'POST':
        payment_details = request.POST['paymentdetails']
        booking_instance = Booking.objects.create(
            bookingid=booking_id,
            username=fetchdetails.username,
            paymentdetails=payment_details,
            totalamount=totalprice,
            bookingdate=booking_date
        )
        booking_instance.cartitems.set(fetch)
        return redirect('order_confirmation', un=un)

    return render(request, 'Customer/booking.html', {'fetching': container})

@login_required
def chistory(request, un):
    # Fetch all bookings for the user
    fetchdetails = Booking.objects.filter(username=un).prefetch_related('cartitems')
    return render(request, 'Customer/chistory.html', {'fetch': fetchdetails})

@login_required
def cfeedback(request,un):
        fetchdetails=userregistration.objects.get(username=un)
        if request.method == 'POST':
            bookingid=request.POST['bid']
            rate=request.POST['rating']
            custfeed=request.POST['feed']
            if Booking.objects.filter(bookingid=bookingid).exists():
                storedata = Feedback(username=un, bookingid=bookingid, rating=rate, message=custfeed)
                storedata.save()
                return redirect('feedbacklist', un=un)
            else:
                return render(request, 'Customer/cfeedback.html', {'message': 'Invalid booking ID'})
        return render(request, 'Customer/cfeedback.html',{'fetch':fetchdetails})

@login_required
def fblist(request,un):
    fetchdetails = Feedback.objects.filter(username=un)
    return render(request,'Customer/fblist.html',{'fetch':fetchdetails})

def customlogout(request):
    logout(request)
    return redirect('/')

@login_required
def delete_cart_item(request, un, bookingid):
    item = get_object_or_404(Cart, bookingid=bookingid, username=un)
    item.delete()
    return redirect('cart', un=un)

@login_required
def order_confirmation(request, un):
    return render(request, 'Customer/order_confirmation.html', {'username': un})