from django.shortcuts import render

from products.models.exhibition_total_list import ExhibitionTotalList


def exhibition_total_list(request):

    if len(ExhibitionTotalList.objects.all()) == 0:
        exhibition_lists = ExhibitionTotalList.objects.create()
        exhibition_lists.create_exhibition_total_list()
        exhibition = ExhibitionTotalList.objects.all()
    else:
        exhibition = ExhibitionTotalList.objects.all()

    context = {
        'exhibition': exhibition,
    }
    return render(request, 'products/exhibition_total_list.html', context)
