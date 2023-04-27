from .models import Drinks
from django.http import JsonResponse
from .serializers import DrinkSerializer

def showdrinks(request):
    #get all drinks
    #serialize them
    #return data in Json Format
    all_drinks = Drinks.objects.all()
    serializer = DrinkSerializer(all_drinks, many=True)
    return JsonResponse({'drinks': serializer.data}, safe=False)



