from django.http import JsonResponse 
from  drinks.models import Drinks
from drinks.serializers import DrinkSerializer

def drink_list (request):

    #getallthedrinks
    #serialize them 
    #return json
    drinks = Drinks.objects.all()
    serializer = DrinkSerializer(drinks, many = True)
    return JsonResponse(serializer.data, safe=False)