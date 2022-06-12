from django.conf import settings
from store.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        for k in self.cart.keys():
            self.cart[str(k)]['product'] = Product.objects.get(pk=k)

        for item in self.cart.values():
            item['total_price'] = item['product'].price * item['quantity']

            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product_id, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1,
                                     'id': product_id}
        if update_quantity:
            self.cart[product_id]['quantity'] += quantity
            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
        self.save()

    def remove(self, product_id):
        """
        Remove a product from the cart.
        """
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def get_total_cost(self):
        for k in self.cart.keys():
            self.cart[str(k)]['product'] = Product.objects.get(pk=k)

        return sum(item['quantity'] * item['product'].price for item in self.cart.values())

    def get_item(self, product_id):
        if str(product_id) in self.cart:
            return self.cart[str(product_id)]
        else:
            return None
