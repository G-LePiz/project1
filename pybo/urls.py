from django.urls import path

from .views import base_views, question_views, answer_views, board_view, freeboard_views, comment_views

app_name = 'pybo'

urlpatterns = [
    # base
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # answer
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),

    path('freeboard/', board_view.index, name='freeboard'),
    path('freeboard/<int:question_id>/', board_view.detail, name='board_detail'),

    path('freeboard/create/', freeboard_views.board_create, name='board_create'),
    path('freeboard/modify/<int:question_id>/', freeboard_views.board_modify, name='board_modify'),
    path('freeboard/delete/<int:question_id>/', freeboard_views.board_delete, name='board_delete'),
    path('freeboard/vote/<int:question_id>/', freeboard_views.board_vote, name='board_vote'),

    path('freeboard/comment/create/<int:question_id>/', comment_views.answer_create, name='comment_create'),
    path('freeboard/comment/modify/<int:answer_id>/', comment_views.answer_modify, name='comment_modify'),
    path('freeboard/comment/delete/<int:answer_id>/', comment_views.answer_delete, name='comment_delete'),
    path('freeboard/comment/vote/<int:answer_id>/', comment_views.answer_vote, name='comment_vote'),
]