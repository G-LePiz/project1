from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from pybo.forms import BoardForm
from pybo.models import Board


@login_required(login_url='common:login')
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:freeboard')
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'freeboard/board_form.html', context)


@login_required(login_url='common:login')
def board_modify(request, question_id):
    question = get_object_or_404(Board, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:board_detail', question_id=question.id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:board_detail', question_id=question.id)
    else:
        form = BoardForm(instance=question)
    context = {'form': form}
    return render(request, 'freeboard/board_form.html', context)


@login_required(login_url='common:login')
def board_delete(request, question_id):
    question = get_object_or_404(Board, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:board_detail', question_id=question.id)
    question.delete()
    return redirect('pybo:freeboard')


@login_required(login_url='common:login')
def board_vote(request, question_id):
    question = get_object_or_404(Board, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:board_detail', question_id=question.id)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip