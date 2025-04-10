from django.shortcuts import render
from .models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'Todo/index.html',context)


@csrf_exempt  # optional if you handle CSRF properly in JS
def delete_todo(request, todo_id):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=todo_id)
            todo.delete()
            return JsonResponse({'success': True})
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)