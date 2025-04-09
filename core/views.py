import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Task


def taskList(request):
  tasks = Task.objects.all().order_by('-created_at').values()
  
  return JsonResponse({
    'tasks': list(tasks),
    "success": True
  })

def taskView(request, id):
  task = get_object_or_404(Task, pk=id)
  
  return JsonResponse({
    'id': task.id,
    'title': task.title,
    'description': task.description,
    'status': task.status
  })

@csrf_exempt
def create_task(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)

      title = data.get('title')
      description = data.get('description')
      status = data.get('status', 'pendente')

      if not title:
        return JsonResponse({'error': 'title is required'}, status=400)

      task = Task.objects.create(title=title, description=description, status=status)

      return JsonResponse({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status
      }, status=201)
      
    except json.JSONDecodeError:
      return JsonResponse({'error': 'JSON invalid!'}, status=400)

  return JsonResponse({'error': 'Method not allowed'}, status=405)
