from django.shortcuts import render
from .models import Todo
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    session_key = request.session.session_key  # Get the session key
    if not session_key:
        request.session.create()  # Create a new session if it doesn't exist
        session_key = request.session.session_key

    todos = Todo.objects.filter(session_key=session_key)  # Filter todos by session key
    context = {'todos': todos}
    return render(request, 'Todo/index.html', context)


@csrf_exempt  # optional if you handle CSRF properly in JS
def delete_todo(request, todo_id):
    if request.method == 'POST':
        
        try:
            session_key = request.session.session_key
            todo = Todo.objects.get(id=todo_id, session_key=session_key)
            todo.delete()
            return JsonResponse({'success': True})
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description') 

            session_key = request.session.session_key  # Get the session key
            if not session_key:
                request.session.create()  # Create a new session if it doesn't exist
                session_key = request.session.session_key


            todo = Todo(title=title, description=description, session_key=session_key)
            todo.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)