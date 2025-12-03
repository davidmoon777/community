from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Post, Comment, ChatRoom, Message, UndergroundAccess
from .serializers import UserSerializer, PostSerializer, CommentSerializer, ChatRoomSerializer, MessageSerializer, UndergroundAccessSerializer

# 회원
class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginUser(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return Response({"message": "Login successful", "user_id": user.id})
            return Response({"message": "Password incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

# 게시판
class PostListCreate(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

# 채팅
class ChatRoomListCreate(generics.ListCreateAPIView):
    serializer_class = ChatRoomSerializer
    queryset = ChatRoom.objects.all()

class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return Message.objects.filter(room_id=room_id)

# 지하층 접근
class AccessUnderground(generics.GenericAPIView):
    serializer_class = UndergroundAccessSerializer
    def post(self, request, *args, **kwargs):
        code = request.data.get('access_code')
        user_level = request.data.get('user_level', 1)
        try:
            access = UndergroundAccess.objects.get(access_code=code, is_active=True)
            if user_level >= access.required_level:
                return Response({"message": "Access granted"})
            return Response({"message": "Level too low"}, status=status.HTTP_403_FORBIDDEN)
        except UndergroundAccess.DoesNotExist:
            return Response({"message": "Invalid access code"}, status=status.HTTP_404_NOT_FOUND)
