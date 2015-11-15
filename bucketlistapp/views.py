from django.http.response import Http404
from django.shortcuts import render
from django.contrib.auth.models import User

from bucketlistapp.models import Bucketlist, BucketlistItem
from bucketlistapp.forms import LoginForm, RegisterForm


from django.views.generic import View, TemplateView

# Create your views here.


class IndexView(TemplateView):
    initial = {'key': 'value'}
    template_name = 'account/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.add_message(
                request, messages.SUCCESS, 'Welcome back!')
            return redirect(
                '/home',
                context_instance=RequestContext(request)
            )
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['loginform'] = LoginForm()
        context['registerform'] = RegisterForm()
        return context


class LoginView(IndexView):
    form_class = LoginForm

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(
                        request, messages.SUCCESS, 'Logged in Successfully!')
                    return redirect(
                        '/bucketlist',
                        context_instance=RequestContext(request)
                    )
            else:
                messages.add_message(
                    request, messages.ERROR, 'Incorrect username or password!')
                return redirect(
                    '/',
                    context_instance=RequestContext(request)
                )
        else:
            context = super(LoginView, self).get_context_data(**kwargs)
            context['loginform'] = form
            return render(request, self.template_name, context)


class RegisterView(IndexView):
    form_class = RegisterForm

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            login(request, new_user)
            messages.add_message(
                request, messages.SUCCESS, 'Registered Successfully!')

            return redirect(
                '/bucketlist/' + self.request.user.username,
                context_instance=RequestContext(request)
            )
        else:
            context = super(RegisterView, self).get_context_data(**kwargs)
            context['registerform'] = form
            return render(request, self.template_name, context)


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)



# class BucketlistAppView(TemplateView):
#     template_name = 'bucketlistapp/base.html'


