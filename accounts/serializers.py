from rest_framework import serializers
from .models import *

# 회원가입용 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User

        # 필요한 필드값 지정, 회원가입은 email까지 필요하므로 email도 추가
        fields = ['username', 'email', 'password']

    # create() 함수를 재정의(오버라이딩)
    def create(self, validated_data):

        # 비밀번호 분리
        password = validated_data.pop('password')

        # user 객체 생성
        user = User(**validated_data)

        # 비밀번호는 해싱해서 저장
        user.set_password(password)
        user.save()

        return user
    
    # email 유효성 검사 함수
    def validate_email(self,input):

        # 이메일 형식이 맞는지 검사
        if not "@" in input:
            raise serializers.ValidationError("Invalid email format")
        
        # 이메일 중복 여부 검사
        if User.objects.filter(email=input).exists():
            raise serializers.ValidationError("Email already exists.")
        
        return input
