from django.http import JsonResponse
from django.views.generic import View
from .models import Client
import json

class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()
        data = [{'id': client.id_client, 'name': client.name, 'city_of_origin': client.city_of_origin} for client in clients]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            new_client = Client.objects.create(name=data['name'], city_of_origin=data['city_of_origin'])
            response_data = {'id': new_client.id_client, 'name': new_client.name, 'city_of_origin': new_client.city_of_origin}
            return JsonResponse(response_data, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class ClientDetailView(View):
    def get(self, request, client_id):
        try:
            client = Client.objects.get(id_client=client_id)
            data = {'id': client.id_client, 'name': client.name, 'city_of_origin': client.city_of_origin}
            return JsonResponse(data)
        except Client.DoesNotExist:
            return JsonResponse({'error': 'Client not found'}, status=404)

    def put(self, request, client_id):
        try:
            client = Client.objects.get(id_client=client_id)
            data = json.loads(request.body)
            client.name = data.get('name', client.name)
            client.city_of_origin = data.get('city_of_origin', client.city_of_origin)
            client.save()
            response_data = {'id': client.id_client, 'name': client.name, 'city_of_origin': client.city_of_origin}
            return JsonResponse(response_data)
        except Client.DoesNotExist:
            return JsonResponse({'error': 'Client not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, client_id):
        try:
            client = Client.objects.get(id_client=client_id)
            client.delete()
            return JsonResponse({'message': 'Client deleted successfully'})
        except Client.DoesNotExist:
            return JsonResponse({'error': 'Client not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
