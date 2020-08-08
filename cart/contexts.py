from django.shortcuts import get_object_or_404
from courses.models import Course


def cart_contents(request):
    """ Cart will be available when rendering every page """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    course_count = 0
    for id, quantity in cart.items():
        course = get_object_or_404(Course, pk=id)
        total += quantity * course.price
        course_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'course': course})
    
    return {'cart_items': cart_items, 'total': total, 'course_count': course_count}