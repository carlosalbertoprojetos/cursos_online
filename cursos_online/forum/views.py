from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView, View

from .forms import Replyform
from .models import Thread, Reply


# class ForumView(View):

#     # template_name = 'forum/index.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, 'forum/index.html')


# forum = ForumView.as_view()

class ForumView(ListView):

    paginate_by = 2
    template_name = 'forum/index.html'

    # model = Thread
    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')

        tag = self.kwargs.get('tag', '')
        if tag:
            queryset = queryset.filter(tags__slug__icontains=tag)

        return queryset

    # acrescentou 'tags' ao contexto
    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context


forum = ForumView.as_view()


class ThreadView(DetailView):
    model = Thread
    template_name = 'forum/thread.html'
    
    def get(self, request, *args, **kwargs):
        response = super(ThreadView, self).get(request, *args, **kwargs)
        if not self.request.user.is_authenticated or (self.object.author != self.request.user):
            self.object.views = self.object.views + 1
            self.object.save()
        return response            

    # acrescentou 'tags' ao contexto
    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        context['form'] = Replyform(self.request.POST or None)
        return context

    def post(self, request, *arts, **kwargs):
        # verifica se está logado para inclusão de resposta
        if not self.request.user.is_authenticated:
            messages.success(
                self.request, 'Precisa estar logado para responder ao tópico.')
            return redirect(self.request.path)

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = self.object
            reply.author = self.request.user
            reply.save()
            messages.success(
                self.request, 'A sua resposta foi enviada com sucesso!!!')
            context['form'] = Replyform()
        return self.render_to_response(context)


thread = ThreadView.as_view()


class ReplyCorrectView(View):
    
    correct = True
    
    def get(self, request, pk):
        reply = get_object_or_404(Reply, pk=pk, author=request.user)
        reply.correct = self.correct
        reply.save()
        messages.success(request, 'Resposta atualizada com sucesso!!!')
        return redirect(reply.thread.get_absolute_url())


reply_correct = ReplyCorrectView.as_view()
reply_incorrect = ReplyCorrectView.as_view(correct=False)