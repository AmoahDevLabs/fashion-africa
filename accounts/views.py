from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import LoginForm, AccountCreateForm, AccountUpdateForm


def next_route(request):
    if 'next' in request.POST:
        return redirect(request.POST.get('next'))
    else:
        return redirect('/')


class Login(LoginView):
    form_class = LoginForm


class SignUpView(FormView):
    form_class = AccountCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@login_required
def my_account(request):
    return render(request, 'accounts/my_account.html')


@login_required
def edit_account(request):
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:my_account')
    else:
        form = AccountUpdateForm(instance=request.user)
    return render(request, 'accounts/edit_my_account.html', {'form': form})
