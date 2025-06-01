from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from service.models import service
from Orderedfood.models import Order
from service.models import Cart, service, mainpage
from Orderedfood.models import Order
from contactenquery.models import contactenquery
from SysAdmin.models import WebUsers


def Adminlogin(request):
    try:
        if request.user.is_authenticated:
            return redirect('admin_dashboard')

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('/admin')

        return render(request, 'login.html')

    except Exception as e:
        print("Login error:", e)
        messages.error(request, "Something went wrong. Try again.")
        return render(request, 'login.html')



@login_required(login_url='/admin')
def AdminDasboard(request):
    enquiery = contactenquery.objects.all()
    cart = Cart.objects.all()
    orders = Order.objects.all()
    cart_total = cart.count()
    menu = service.objects.all()
    all_menu = menu.count()
    total_order = Order.objects.count()
    users = User.objects.all()
    webusers=WebUsers.objects.all()
    main=mainpage.objects.all()

    return render(request, 'adminpanel.html', {
        'all_menu': all_menu,
        'cart': cart,
        'cart_total': cart_total,
        'menu': menu,
        'total_order': total_order,
        'orders':orders,
        'enquierys':enquiery,
        'users':users,
        'webusers':webusers,
        'main':main,
    })


def logout_view(request):
    try:
        django_logout(request)
        print('logout succesfull')
        return redirect('/admin')# Redirects to login page
    except Exception as e:
        print("Logout error:", e)
        return redirect('/admin')


def add_menu(request):
    if request.method == 'POST':
        Image = request.FILES.get("image")
        Title = request.POST.get("title")
        Price = request.POST.get("price")
        Old_Price = request.POST.get("oldprice")
        Rating = request.POST.get("rating")
        Badge = request.POST.get("badge")
        Description = request.POST.get("desc")
        Deal = request.POST.get("deal")

        # Safely convert strings to integers
        try:
            Price = int(Price) if Price else None
        except ValueError:
            Price = None

        try:
            Old_Price = int(Old_Price) if Old_Price else 0
        except ValueError:
            Old_Price = 0

        try:
            Deal = int(Deal) if Deal else 20
        except ValueError:
            Deal = 20

        # Optional: log for debugging
        food = {
            'Image': Image,
            'Title': Title,
            'Price': Price,
            'Old_Price': Old_Price,
            'Rating': Rating,
            'Badge': Badge,
            'Description': Description,
            'Deal': Deal,
        }
        print(food)

        try:
            service.objects.create(
                service_image=Image,
                service_title=Title,
                service_price=Price,
                service_oldprice=Old_Price,
                service_rating=Rating,
                service_badge=Badge,
                service_desc=Description,
                service_deal=Deal,
            )
            print("✅ Item added successfully")
        except Exception as e:
            print("❌ Error adding item:", e)

        return redirect('admin_dashboard')
    else:
        return redirect('admin_dashboard')

def del_enquiry(request,enqid):
    msg=contactenquery.objects.get(id=enqid)
    msg.delete()
    return redirect('admin_dashboard')

def remove_item(request,item_id):
    item=service.objects.get(id=item_id)
    item.delete()
    return redirect('admin_dashboard')

def add_news(request):
    if request.method == 'POST':
        Image = request.FILES.get("image")
        Title = request.POST.get("title")
        Description = request.POST.get("desc")


        try:
            mainpage.objects.create(
                mainpage_image=Image,
                mainpage_title=Title,
                mainpage_desc=Description,
            )
            print("✅ Item added successfully")
        except Exception as e:
            print("❌ Error adding item:", e)

        return redirect('admin_dashboard')
    else:
        return redirect('admin_dashboard')

def admin(request):
    custom_admin=None
    if request.user.is_authenticated:
        try:
            custom_admin=User.objects.get(user = request.user)
        except User.DoesNotExist:
            custom_admin = None
            return render(request,'adminpanel.html',custom_admin)



def user_from_session(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = WebUsers.objects.get(id=user_id)
            return {'websuser': user}
        except WebUsers.DoesNotExist:
            return {}
    return {}