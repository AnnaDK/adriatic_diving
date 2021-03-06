from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from courses.models import Course
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required()
 # Handle the Stripe api checkout the card and payment
def checkout(request):
    if request.method == "POST":
        # two forms that will be used
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            course_count = 0
            discount = 0
            final_total = 0
            for id, quantity in cart.items():
                course = get_object_or_404(Course, pk=id)
                total += quantity * course.price
                course_count += quantity
                discount = total * 15 / 100
                final_total = total - discount
                order_line_item = OrderLineItem(
                    order=order,
                    course=course,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(final_total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('courses'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form,
                                             'payment_form': payment_form,
                                             'publishable': settings.STRIPE_PUBLISHABLE})
