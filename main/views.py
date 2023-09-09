from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'KitKat',
        'amount': '10',
        'description': 'coklat',
    }

    return render(request, "main.html", context)