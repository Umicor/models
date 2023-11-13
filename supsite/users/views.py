from django.shortcuts import render
from django.http import JsonResponse
from .models import User,Issue
from django.views.decorators.http import require_POST
import json

def get_all_users(request):
    users = User.objects.all()
    user_list = [
        {
            'user1name': user.first_name,
            'user2name': user.last_name,
            'email': user.email,
            'id': user.role_id
         }
        for user in users
    ]
    return JsonResponse({'users': user_list})


def create_user(request):
    try:
        # Предполагается, что тело запроса содержит данные в формате JSON
        data = json.loads(request.body.decode('utf-8'))

        # Ваша логика создания экземпляра пользователя в базе данных
        # Например, предположим, что у вас есть модель User
        from .models import User
        new_user = User.objects.create(
            username=data['username'],
            email=data['email'],
            # Добавьте другие поля по мере необходимости
        )

        # Возвращаем созданный экземпляр в формате JSON
        return JsonResponse({
            'id': new_user.id,
            'username': new_user.username,
            'email': new_user.email,
            # Добавьте другие поля по мере необходимости
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Неверный формат JSON в теле запроса'}, status=400)

    except KeyError as e:
        return JsonResponse({'error': f'Отсутствует обязательное поле: {e}'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def create_issue(request):
    try:
        # Предполагается, что тело запроса содержит данные в формате JSON
        data = json.loads(request.body.decode('utf-8'))

        # Ваша логика создания экземпляра проблемы в базе данных
        # Например, предположим, что у вас есть модель Issue
        from .models import Issue
        new_issue = Issue.objects.create(
            title=data['title'],
            description=data['description'],
            # Добавьте другие поля по мере необходимости
        )

        # Возвращаем созданный экземпляр в формате JSON
        return JsonResponse({
            'id': new_issue.id,
            'title': new_issue.title,
            'description': new_issue.description,
            # Добавьте другие поля по мере необходимости
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Неверный формат JSON в теле запроса'}, status=400)

    except KeyError as e:
        return JsonResponse({'error': f'Отсутствует обязательное поле: {e}'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_all_issues(request):
        try:
            # Получаем все экземпляры проблемы из базы данных
            issues = Issue.objects.all()

            # Преобразуем результат в список словарей
            issues_list = [
                {
                    'id': issue.id,
                    'title': issue.title,
                    'description': issue.description,
                    # Добавьте другие поля по мере необходимости
                }
                for issue in issues
            ]

            # Возвращаем список проблем в формате JSON
            return JsonResponse({'issues': issues_list})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)