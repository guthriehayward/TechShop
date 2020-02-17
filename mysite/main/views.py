from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, ProductCategory, ProductManufacturer
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

def single_slug(request, single_slug):
    categories = [c.category_slug for c in ProductCategory.objects.all()]
    if single_slug in categories:
        matching_manufacturers = ProductManufacturer.objects.filter(product_category__category_slug=single_slug)
        product_urls = {}

        for m in matching_manufacturers.all():
            first_product = Product.objects.filter(product_manufacturer__product_manufacturer=m.product_manufacturer).earliest("uploadDate")
            product_urls[m] = first_product.product_slug

        return render(request=request,
                      template_name='main/category.html',
                      context={'Manufacturers': matching_manufacturers, 'first_products': product_urls})

    products = [p.product_slug for p in Product.objects.all()]
    if single_slug in products:
        return HttpResponse(f"{single_slug} is a product!")

    return HttpResponse(f"{single_slug} does not correspond to anything.")

def homepage(request):
    return render(request=request,
                  template_name='main/categories.html',
                  context={'Categories': ProductCategory.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form=NewUserForm
    return render(request,
                  "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form":form})
