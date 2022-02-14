from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def products(reauest):
    return render(reauest, 'products/products.html')


def test_context(request):
    context = {
        'title': 'GeekShop - Тестовый контекст',
        'header': 'Welcome!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ],
        'is_promotion': False,
    }
    return render(request, 'products/test-context.html', context)
