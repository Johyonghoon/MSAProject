from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from exrc.auth.exrc_users.repositories import UserRepository
from exrc.auth.exrc_users.serializers import UserSerializer
from exrc.auth.exrc_users.services import UsersService


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@parser_classes([JSONParser])
def user(request):
    if request.method == "GET":
        return Response(UserRepository().find_user_by_email(request.data["user_email"]))
    elif request.method == "POST":
        new_user = request.data
        print(f" 리액트에서 등록한 신규 사용자 {new_user}")
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"result": "SUCCESS"})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        repo = UserRepository()
        modify_user = repo.find_user_by_email(request.data["user_email"])
        db_user = repo.find_by_id(modify_user.id)
        serializer = UserSerializer(data=db_user)
        if serializer.is_valid():
            serializer.update(modify_user, db_user)
            return JsonResponse({'result': 'Success'})
    elif request.method == "DELETE":
        repo = UserRepository()
        delete_user = repo.find_user_by_email(request.data["user_email"])
        db_user = repo.find_by_id(delete_user.id)
        db_user.delete()
        return JsonResponse({'result': 'Success'})


@api_view(['POST'])
@parser_classes([JSONParser])
def create_dummy_accounts(request):
    service = UsersService()
    service.create_acc_hook()
    print(f'### DB에 더미 사용자 100명을 생성했습니다. ###')
    return JsonResponse({'result': 'Success'})


@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request): return UserRepository().select_all()


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request): return UserRepository().login(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def user_list_by_name(request):
    return Response(UserRepository().find_users_by_name(request.data["user_name"]))
