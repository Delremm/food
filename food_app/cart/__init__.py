from django.conf import settings
from prices import Price
from satchless import cart

from food_app.models import Menu

CART_SESSION_KEY = 'carts'


class SessionCartLine(cart.CartLine):
    def get_price_per_item(self, **kwargs):
        gross = self.data['unit_price_gross']
        net = self.data['unit_price_net']
        return Price(net=net, gross=gross, currency=settings.DEFAULT_CURRENCY)

    def for_storage(self):
        return {
            'product': self.product.id,
            'quantity': self.quantity,
            'data': self.data}

    @classmethod
    def from_storage(cls, data_dict):
        product = Menu.objects.get(id=data_dict['product'])
        quantity = data_dict['quantity']
        data = data_dict['data']
        instance = SessionCartLine(product, quantity, data)
        return instance


class SessionCart(cart.Cart):
    timestamp = None

    @classmethod
    def from_storage(cls, cart_data):
        cart = SessionCart()
        for line_data in cart_data['items']:
            cart._state.append(SessionCartLine.from_storage(line_data))
        cart.timestamp = cart_data['timestamp']
        return cart

    def for_storage(self):
        cart_data = {
            'items': [i.for_storage() for i in self],
            'timestamp': self.timestamp}
        return cart_data

    def create_line(self, product, quantity, data):
        return SessionCartLine(product, quantity, data)
