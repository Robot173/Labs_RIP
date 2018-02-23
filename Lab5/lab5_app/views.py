from django.shortcuts import render

# Create your views here.
def main_view(request):
    data = {
        'products':[
            {'name': 'Картошка', 'id': 1},
            {'name': 'Морковка', 'id': 2},
            {'name': 'Огурцы', 'id': 3},
            {'name': 'Помидоры', 'id': 4},
            {'name': 'Баклажан', 'id': 5},
            {'name': 'Пицца', 'id': 6}
        ]
    }
    return render(request, 'index.html', data)

def product_view(request, id):
    data = {
        'product': {
            'id': id
        }
    }
    return render(request, 'product.html', data)
