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
    template_name = 'bucketlistapp/bucket.html'

    def get_context_data(self, **kwargs):
        context = super(BucketlistAppView, self).get_context_data(**kwargs)
        context['buckets'] = Bucketlist.objects.filter(created_by=self.request.user)
        context['bucketlistform'] = self.form_class
        return context

    def post(self, request, **kwargs):
        name = request.POST.get('name')

        bucketlist = Bucketlist(name=name, created_by=request.user)
        bucketlist.save()

        return redirect('/bucketlists/', context_instance=RequestContext(request))


class BucketlistItemAppView(LoginRequiredMixin, TemplateView):
    form_class = ItemForm
    template_name = 'bucketlistapp/item.html'

    def get_context_data(self, **kwargs):
        context = super(BucketlistItemAppView, self).get_context_data(**kwargs)
        bucket = kwargs['bucketlist']

        context['bucket'] = Bucketlist.objects.get(id=bucket)
        context['items'] = BucketlistItem.objects.filter(bucketlist=context['bucket'])
        context['itemform'] = self.form_class
        return context

    def post(self, request, **kwargs):
        name = request.POST.get('name')

        item = BucketlistItem(name=name, bucketlist=Bucketlist.objects.get(id=kwargs['bucketlist']))
        item.save()

        return redirect('/bucketlists/' + kwargs['bucketlist'] + '/items/', context_instance=RequestContext(request))

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


class DeleteBucketlistView(LoginRequiredMixin, TemplateView):


    def get(self, request, **kwargs):
        pass


class UpdateBucketlistView(LoginRequiredMixin, TemplateView):

    def get(self, request, **kwargs):
        bucketlist = Bucketlist.objects.get(id=kwargs['bucket_id'])
        bucketlist.delete()
        return redirect('/bucketlists/', context_instance=RequestContext(request))

    def post(self, request, **kwargs):
        bucket_list = Bucketlist.objects.get(id=kwargs['bucket_id'])
        name = request.POST.get('name')
        bucket_list.name = name
        bucket_list.save()

        # item = BucketlistItem(name=name, bucketlist=Bucketlist.objects.get(id=kwargs['bucketlist']))
        # item.save()

        # return redirect('/bucketlists/' + kwargs['bucketlist'] + '/items/', context_instance=RequestContext(request))
        return redirect('/bucketlists/', context_instance=RequestContext(request))



class UpdateBucketlistItemView(LoginRequiredMixin, TemplateView):

    def get(self, request, **kwargs):
        item = BucketlistItem.objects.get(id=kwargs[''])

    def post(self, request, **kwargs):
        pass
