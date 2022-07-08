from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status
from datetime import timedelta
from django.utils import timezone


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

        
class IsCandidateUser(BasePermission):
    """
    유저 타입 candidate 일때만 가능
    """

    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user
        
        #비로그인 사용자는 조회(GET) 만 가능
        if request.method in self.SAFE_METHODS:
            return True
        #그외 request에서 로그인이 안되어있으면, 로그인 하라고 알림
        if not user.is_authenticated:
            response = {
                'detail': "서비스를 이용하기 위해 로그인 해주세요."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
        
        if not user.user_type.user_type == 'candidate':
            response = {
                'detail': "candidate타입의 유저만 인가됩니다."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        return True