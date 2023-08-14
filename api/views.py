from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random


@csrf_exempt
def get_random_array(request):
    if request.method == 'POST':
        try:
            sentence = request.POST.get("sentence")
            if sentence is None:
                return JsonResponse({'error': 'Invalid input format'}, status=400)
            
            words = sentence.split()
            if all([word.isnumeric() for word in words]):
                return JsonResponse({'error': 'Invalid input format'}, status=400)

            # Generate a random 500-dimensional array of floats
            random_array = [round(random.uniform(-2, 2),4) for _ in range(500)]

            response = {
                'random_array': random_array
            }
            return JsonResponse(response, status=200)

        except KeyError:
            return JsonResponse({'error': 'Invalid input format'}, status=400)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)