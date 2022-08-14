from django.shortcuts import render

from shops.models import IceCream


def get_ice_cream(request, ice_cream_id):
    ice_cream = IceCream.objects.get(id=ice_cream_id)
    context = {"ice_cream": {
        'name': ice_cream.name,
        'shop': ice_cream.shop,
        'stock': ice_cream.stock
    }
    }
    return render(request, 'ice_cream_detail.html', context)



def get_ice_creams(request):
        ice_creams = IceCream.objects.all()
        context = {
            'ice_creams': ice_creams
        }
        return render(request, 'ice_cream_list.html', context)

