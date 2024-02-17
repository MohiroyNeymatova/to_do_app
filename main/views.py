from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_204_NO_CONTENT


@api_view(['GET'])
def get_tasks(request):
    serialized_data = TaskSerializer(Task.objects.all(), many=True).data
    return Response(serialized_data)


@api_view(['POST'])
def create_task(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    serialized_data = TaskSerializer(Task.objects.create(name=name, description=description))
    return Response(serialized_data.data)


@api_view(['PUT'])
def update_task(request, pk):
    try:
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        t = Task.objects.get(id=pk)
        t.name = name
        t.description = description
        t.status = status
        t.save()
        serialized_data = TaskSerializer(t)
        data = {
            'success': True,
            'error': serialized_data.data
        }
        return Response(data, status=HTTP_200_OK)
    except Exception as e:
        data = {
            'success': False,
            'error': f'{e}'
        }
        return Response(data, status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_task(request, pk):
    Task.objects.get(id=pk).delete()
    return Response({'message: deleted'}, status=HTTP_204_NO_CONTENT)
