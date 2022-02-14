from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(reauest):
    context = {
        'title': 'GeekShop - Продукты',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': 23725,
             'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
             'text': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340,
             'text': 'Плотная ткань. Легкий материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590,
             'text': 'Гладкий кожаный верх. Натуральный материал.'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
             'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ],
    }
    return render(reauest, 'products/products.html', context)


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
