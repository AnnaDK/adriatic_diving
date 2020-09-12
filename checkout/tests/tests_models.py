from django.test import TestCase
from checkout.models import Order, OrderLineItem
from courses.models import Course
from django.utils import timezone
import datetime
from mock import patch


class TestModels(TestCase):
    def test_order_model(self):
        with patch.object(timezone, 'now', return_value=datetime.datetime(2020, 9, 11, 23, 18, 32)) as mock_now:
            order = Order.objects.create(
                full_name='Max',
                phone_number='1234567890',
                country='Netherlands',
                postcode='1234',
                town_or_city='Amsterdam',
                street_address1='Greenstreet',
                street_address2='123',
                county='1234',
                date=timezone.now()
                )
        order.save()
        self.assertEquals(order.full_name, 'Max')
        self.assertEquals(order.phone_number, '1234567890')
        self.assertEquals(order.country, 'Netherlands')
        self.assertEquals(order.postcode, '1234')
        self.assertEquals(order.town_or_city, 'Amsterdam')
        self.assertEquals(order.street_address1, 'Greenstreet')
        self.assertEquals(order.street_address2, '123')
        self.assertEquals(order.county, '1234')
        self.assertEquals(order.date, timezone.now())

    def test_order_line_item_model(self):
        with patch.object(timezone, 'now', return_value=datetime.datetime(2020, 9, 11, 23, 18, 32)) as mock_now:
            
            order = Order.objects.create(
                full_name='Max',
                phone_number='1234567890',
                country='Netherlands',
                postcode='1234',
                town_or_city='Amsterdam',
                street_address1='Greenstreet',
                street_address2='123',
                county='1234',
                date=timezone.now()
                 )
            order.save()
        
        course = Course.objects.create(
            name='open water course',
            price='360',

            )
        course.save()
        order_line_item = OrderLineItem.objects.create(
            order=order,
            course=course,
            quantity=1
            )
        self.assertEquals(order_line_item.order, order)
        self.assertEquals(order_line_item.course, course)
        self.assertEquals(order_line_item.quantity, 1)

