from django.shortcuts import render, redirect
from home.models import *
import requests
from datetime import datetime, timedelta


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    products = Product.objects.all().order_by('-created_at')
    banner = Banner.objects.last()

    context = {
        'products': products,
        'banner': banner
    }
    return render(request, 'index.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    telegram_bot = TelegramBot.objects.last()

    now = datetime.now()

    if request.method == 'POST':
        data = Order()
        data.title = product.title
        data.category = product.category
        data.price = product.price
        data.image = product.image

        data.first_name = request.POST.get('first_name')
        data.last_name = request.POST.get('last_name')
        data.phone_number = request.POST.get('phone_number')
        data.address = request.POST.get('address')
        data.comment = request.POST.get('comment')
        data.ip = get_client_ip(request)
        data.save()

        if telegram_bot:
            try:
                text = f'🇺🇿 YANGI BUYURTMA! 🇺🇿 \n' \
                       f'\n 👨  FISH: {data.first_name} {data.last_name}' \
                       f'\n 🛒  Maxsulot: {data.title}' \
                       f'\n 📩  Xabar: {data.comment}' \
                       f'\n ' \
                       f'\n 📲  Telefon raqam: {data.phone_number}' \
                       f'\n 🏠 Manzil: {data.address}' \
                       f'\n 🌐  IP RAQAM: {data.ip}' \
                       f'\n 📅  VAQT: {now.strftime("%H:%M / %d-%b, %Y")}'
                result = "".join(text)

                bot_token = telegram_bot.bot_token
                bot_chatID = telegram_bot.chat_id

                url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={result}'

                requests.get(url)
            except Exception as e:
                print(e)

        return redirect('success-page')

    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


def success(request):
    return render(request, 'success-page.html')
