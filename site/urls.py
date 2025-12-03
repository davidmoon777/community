from django.urls import path
from .views import (
    RegisterUser, LoginUser,
    PostListCreate, CommentListCreate,
    ChatRoomListCreate, MessageListCreate,
    AccessUnderground
)

urlpatterns = [
    # 회원
    path('register/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),

    # 게시판
    path('board/', PostListCreate.as_view()),
    path('board/comments/', CommentListCreate.as_view()),

    # 채팅
    path('chat/', ChatRoomListCreate.as_view()),
    path('chat/<int:room_id>/messages/', MessageListCreate.as_view()),

    # 지하층 접근
    path('underground/access/', AccessUnderground.as_view()),
]
