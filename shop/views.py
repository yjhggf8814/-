from django.shortcuts import render

def katalog(request):
    return render(request, 'shop/katalog.html')  