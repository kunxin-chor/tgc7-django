# a context processor for shopping cart
def cart_contents(request):
    # make the content of the shopping cart available to all
    cart = request.session.get("shopping_cart", {})
    return {
        'shopping_cart': cart,
        'number_of_items': len(cart)
    }
