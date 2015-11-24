from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from bucketlistapp.models import Bucketlist, BucketlistItem
from bucketlistapp.forms import LoginForm, RegisterForm, BucketlistForm, ItemForm


from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.template import RequestContext

# Create your views here.


class IndexView(TemplateView):
    initial = {'key': 'value'}
    template_name = 'bucketlistapp/index.html'

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

                    return redirect(
                        '/bucketlists/',
                        context_instance=RequestContext(request)
                    )
            else:

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

            return redirect(
                '/bucketlists/',
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


class BucketlistAppView(LoginRequiredMixin, TemplateView):
    form_class = BucketlistForm
    template_name = 'bucketlistapp/bucketlists.html'

    def get_context_data(self, **kwargs):
        context = super(BucketlistAppView, self).get_context_data(**kwargs)
        context['bucketlistform'] = self.form_class
        return context

    def post(self, request, **kwargs):
        name = request.POST.get('name')

        bucketlist = Bucketlist(name=name, created_by=request.user)
        bucketlist.save()
        return redirect('/api/bucketlists/', context_instance=RequestContext(request))


        # if form.is_valid():
        #
        #     # import pdb
        #     # pdb.set_trace()
        #     bucketlist = form.save()
        #     bucketlist.created_by = request.user
        #     bucketlist.save()
        #     # import pdb
        #     # pdb.set_trace()
        #     return redirect('/api/bucketlists/', context_instance=RequestContext(request))

        # else:
        #     context = super(BucketlistAppView, self).get_context_data(**kwargs)
        #     context['bucketlistform'] = form
        #     return render(request, self.template_name, context)


class BucketlistItemAppView(LoginRequiredMixin, TemplateView):
    template_name = 'bucketlistapp/bucket.html'