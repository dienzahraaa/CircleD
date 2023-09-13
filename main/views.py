from django.shortcuts import render

def show_main(request):
    context = {
        'nama': 'Dien',
        'kelas': 'F',
    }

    return render(request, "main.html", context)