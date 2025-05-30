from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from service.models import service, mainpage, Cart
from contactenquery.models import contactenquery
from Orderedfood.models import Order
from SysAdmin.models import WebUsers
from django.utils import timezone
from functools import wraps
from django.core.exceptions import ValidationError

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = WebUsers.objects.get(username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id
                user.last_login = timezone.now()
                user.save()
                return redirect('menu')
            else:
                messages.error(request, "Invalid password")
        except WebUsers.DoesNotExist:
            messages.error(request, "User not found")

    return render(request, 'userlogin.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mob_no')
        image = request.FILES.get('image')

        if WebUsers.objects.filter(username=username).exists():
            return render(request, 'userregister.html', {'error': 'Username already exists.'})

        try:
            user = WebUsers(
                username=username,
                date_joined=timezone.now(),
                email_id=email,
                mob_no=mobile,
                user_image=image
            )
            user.set_password(password)
            user.save()
            return redirect('user-login')

        except ValidationError as ve:
            return render(request, 'userregister.html', {'error': f'Validation error: {ve}'})
        except Exception as e:
            return render(request, 'userregister.html', {'error': f'An error occurred: {e}'})

    return render(request, 'userregister.html')

def user_logout(request):
    request.session.flush()
    return redirect('home')

def require_login(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('user-login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def index_page(request):
    mainpage_data = mainpage.objects.all()
    Cart.objects.all().delete()
    return render(request, "index.html", {"mainpage_data": mainpage_data})

def menu_page(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(WebUsers, id=user_id)
    cart = Cart.objects.filter(cart_user=user)
    total_price = sum(item.item_price * item.item_quantity for item in cart)
    total_item = sum(item.item_quantity for item in cart)
    all_items = [item.item_title for item in cart]

    query = request.GET.get('servicename', '')
    service_data = service.objects.filter(service_title__icontains=query) if query else service.objects.all()

    return render(request, 'menu.html', {
        'service_data': service_data,
        'cart': cart,
        'all_items': all_items,
        'total_price': total_price,
        'total_item': total_item
    })

@require_login
def menu_detail(request, slug):
    menu_detail = get_object_or_404(service, menu_slug=slug)
    return render(request, "menu_detail.html", {"menu_detail": menu_detail})

def promotion_page(request):
    return render(request, "promotions.html")

def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("text")
        contactenquery.objects.create(name=name, email=email, message=comment)
    return render(request, "contact.html")

def karaoke_page(request):
    return render(request, "karaoke.html")

def form_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("text")
        context = {"name": name, "email": email, "comment": comment}
        return render(request, "form.html", context)
    return render(request, "form.html")

def submitform(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("text")
        return HttpResponse("Form submitted successfully")
    return render(request, "test.html")

def home(request):
    return render(request, "index.html")

@require_login
def order_page(request, slug):
    item = service.objects.get(menu_slug=slug)
    return render(request, "order.html", {'item': item})

@require_login
def ordercart_page(request):
    user = get_object_or_404(WebUsers, id=request.session.get('user_id'))
    cart = Cart.objects.filter(cart_user=user)
    total_price = sum(item.item_price * item.item_quantity for item in cart)
    all_items = [item.item_title for item in cart]
    return render(request, "order.html", {'total_price': total_price, 'all_items': all_items})

@require_login
def ordersubmit(request):
    if request.method == "POST":
        user_id = request.session.get('user_id')
        webuser = get_object_or_404(WebUsers, id=user_id)

        address = request.POST.get("address")
        food = request.POST.get("food_title")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        special_instructions = request.POST.get("addons")
        order_type = request.POST.get("order_type")
        payment = request.POST.get("payment")

        Order.objects.create(
            name=webuser.username,
            email=webuser.email_id,
            phone=webuser.mob_no,
            food=food,
            Price=price,
            Quantity=quantity,
            Special_Instructions=special_instructions,
            order_type=order_type,
            payment_mode=payment,
            address=address
        )
        return redirect('order-sucess')

    return render(request, "index.html")

@require_login
def cart_page(request):
    user = get_object_or_404(WebUsers, id=request.session.get('user_id'))
    cart = Cart.objects.filter(cart_user=user)
    return render(request, "cart.html", {'cart': cart})

@require_login
def addtocart(request, item_id):
    user_id = request.session.get('user_id')
    user = get_object_or_404(WebUsers, id=user_id)
    food = get_object_or_404(service, id=item_id)

    cart_item = Cart.objects.filter(cart_user=user, item_slug=food.menu_slug).first()

    if cart_item:
        cart_item.item_quantity += 1
        cart_item.save()
        return JsonResponse({'message': f'One more {food.service_title} added to your plate!'})

    Cart.objects.create(
        cart_user=user,
        item_image=food.service_image,
        item_title=food.service_title,
        item_rating=food.service_rating,
        item_price=food.service_price,
        item_slug=food.menu_slug,
        item_quantity=1
    )
    return JsonResponse({'message': f'{food.service_title} added to your plate!'})

@require_login
def remove_item(request, item_id):
    try:
        item = Cart.objects.get(id=item_id)
        item.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('menu')

@require_login
def remove_all(request):
    user = get_object_or_404(WebUsers, id=request.session.get('user_id'))
    Cart.objects.filter(cart_user=user).delete()
    return JsonResponse({'message': 'All items removed from your cart.'})

@require_login
def order_sucess(request):
    return render(request,'ordersucess.html')

def order_deatil(request):
    return render(request,'order_detail.html')

@require_login
def track_order(request):
    order = Order.objects.all()
    return render(request,'trackorder.html')

def page_not_found(request,path):
    return render(request,'404_error.html')

def page_not_found1(request,path,ank):
    return render(request,'404_error.html')

def page_not_found2(request,pa,an,er):
    return render(request,'404_error.html')

def page_not_found3(request,path,ank,error,error1):
    return render(request,'404_error.html')
