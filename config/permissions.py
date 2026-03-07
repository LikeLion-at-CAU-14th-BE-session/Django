from rest_framework.permissions import BasePermission,IsAuthenticatedOrReadOnly
from rest_framework.permissions import SAFE_METHODS
from django.utils import timezone

class IsAvailableTime(BasePermission):
    message = "밤 10시부터 아침 7시 까지는 게시판을 이용하실 수 없습니다"
    
    def has_permission(self,request,view):
        # 시간 검사
        current_time = timezone.localtime(timezone.now())
        if 0 <= current_time.hour < 7 or 22 <= current_time.hour < 24 :
            return False
        return True

class IsOwnerOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self,request,view,obj):
        # 읽기 권한은 모두에게 허용, 작성자만 수정 권한 부여
        if request.method in SAFE_METHODS:
            return True
        print(f"{obj.user} : {request.user}")
        return obj.user == request.user