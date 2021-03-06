from django.shortcuts import render,redirect
from vendor.models import VendorRegistrationModel
from pwn.models import CuisineModel,CityModel
from django.contrib import messages

def openLogin(request):
    return render(request,"vendor/login.html")


def vendor_login_check(request):
    if request.method == "POST":
        try:
            admin = VendorRegistrationModel.objects.get(contact_1=request.POST.get("vendor_username"),
                                                password=request.POST.get("vendor_password"),status='approved')
            request.session["vendor_status"] = True
            return redirect('vendor_welcome')
        except:
            return render(request, "vendor/login.html", {"error": "Invalid User"})
    else:
        request.session["vendor_status"] = False
        return render(request, "vendor/login.html", {"error": "Vendor Logout Success"})


def vendor_register(request):
    return render(request,"vendor/vendor_register.html",{"cuisine":CuisineModel.objects.all(),"city":CityModel.objects.all()})


def vendor_save(request):
    sn = request.POST.get("v1")
    c1 = request.POST.get("v2")
    c2 = request.POST.get("v3")
    cui = request.POST.get("v4")
    ph = request.FILES["v5"]
    add = request.POST.get("v6")
    cty = request.POST.get("v7")
    pas = request.POST.get("v8")
    otp = 0000
    sta = "pending"
    VendorRegistrationModel(stall_name=sn,contact_1=c1,contact_2=c2,cuisine_type_id=cui,photo=ph,address=add,vendor_city_id=cty,password=pas,OTP=otp,status=sta).save()
    messages.success(request,"Registration is Done, Need Approval from Admin")
    return redirect('vendor_main')


def vendor_welcome(request):
    return render(request,"vendor/welcome.html")