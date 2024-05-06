from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, OrderForm
from .models import Service, Order
import stripe
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('place_order')
    else:
        form = UserRegistrationForm()
    return render(request, 'services/register.html', {'form': form})

def list_services(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

from django.contrib.auth.models import User
def place_order(request):
    services = Service.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            print("request.user", request.user)
            order.user = User.objects.get(pk=request.user.pk)  # Casting to User object
            order.save()
            return redirect('process_payment', order.id)
    else:
        form = OrderForm()
    return render(request, 'services/place_order.html', {'form': form, 'services': services})



def process_payment(request, order_id):
    order = Order.objects.get(id=order_id)
    service = order.service

    if request.method == 'POST':
        token = request.POST.get('stripeToken')

        try:
            charge = stripe.Charge.create(
                amount=int(service.fee * 100),
                currency='usd',
                source=token,
                description=f'Payment for {service.name}',
            )

            order.payment_status = True
            order.save()

            return render(request, 'services/payment_success.html', {'order': order})
        except stripe.error.CardError as e:
            return render(request, 'services/payment_error.html', {'error': e.error.message})
    else:
        stripe_key = settings.STRIPE_PUBLISHABLE_KEY
        context = {
            'order': order,
            'stripe_key': stripe_key,
        }
        return render(request, 'services/process_payment.html', context)