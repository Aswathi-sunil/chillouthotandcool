from django.shortcuts import render, redirect
from .models import (About,Feature,MenuCategory,MenuItem,SignatureDish,Branch,Client,GalleryImage,ContactMessage,SiteSettings)

def home(request):
    site_settings = SiteSettings.objects.first()
    about = About.objects.first()
    features = Feature.objects.filter(is_active=True)
    menu_categories = MenuCategory.objects.filter(is_active=True)[:5]
    signature_dishes = SignatureDish.objects.filter(is_active=True)[:3]
    branches = Branch.objects.filter(is_active=True)[:6]
    clients = Client.objects.filter(is_active=True)

    context = {
        'site_settings': site_settings,
        'about': about,
        'features': features,
        'menu_categories': menu_categories,
        'signature_dishes': signature_dishes,
        'branches': branches,
        'clients': clients,
    }
    return render(request, 'restaurant/home.html', context)


def about(request):
    site_settings = SiteSettings.objects.first()
    about_obj = About.objects.first()
    features = Feature.objects.filter(is_active=True)

    context = {
        'site_settings': site_settings,
        'about_obj': about_obj,
        'features': features,
    }
    return render(request, 'restaurant/about.html', context)


def menu(request):
    site_settings = SiteSettings.objects.first()

    context = {
        'site_settings': site_settings,
    }
    return render(request, 'restaurant/menu.html', context)

def signature_dishes(request):
    site_settings = SiteSettings.objects.first()
    dishes = SignatureDish.objects.filter(is_active=True)

    context = {
        'site_settings': site_settings,
        'dishes': dishes,
    }
    return render(request, 'restaurant/signature_dishes.html', context)


def branches(request):
    site_settings = SiteSettings.objects.first()

    context = {
        'site_settings': site_settings,
    }
    return render(request, 'restaurant/branches.html', context)


def contact(request):
    site_settings = SiteSettings.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            message=message
        )
        return redirect('contact')

    context = {
        'site_settings': site_settings,
    }
    return render(request, 'restaurant/contact.html', context)