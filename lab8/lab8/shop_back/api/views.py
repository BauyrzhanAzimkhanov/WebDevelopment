from django.http.response import HttpResponse, JsonResponse
import random
from api.models import Product, Category

def greetings(request):
    return HttpResponse('Hello user!')

def get_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe = False)

def get_product(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    return JsonResponse(product.to_json())
    # for product in products:
    #     if(product['id'] == id):
    #         return JsonResponse(product)
    # return JsonResponse({'exception': 'Product not found'})

def get_categories(request):
    category = Category.objects.all()
    category_json = [category.to_json() for categor in category]
    return JsonResponse(category_json, safe = False)

def get_category(request, id):
    return HttpResponse(f'Category {id}')

products = [
    {
        'id': i,
        'name': 'Van\'s mask',
        'price': 300 + i,
        'description': 'Mask ' + str(i),
        'count': random.randint(0, 1001),
        'is_active': True
    } for i in range(1, 1001)
]

category = [
    {
        'name': 'masks ' + str(i)
    } for i in range(1, 1001)
]