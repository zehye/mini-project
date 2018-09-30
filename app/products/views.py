from django.shortcuts import render

from products.models.exhibition_total_list import ExhibitionTotalList


def exhibition_total_list(request):
    exhibition = ExhibitionTotalList.objects.all()
    context = {
        'exhibition': exhibition,
    }
    return render(request, 'products/exhibition_total_list.html', context)
