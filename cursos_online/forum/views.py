from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView


from .models import Thread 



# class ForumView(View):

#     # template_name = 'forum/index.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, 'forum/index.html')


# forum = ForumView.as_view()

class ForumView(ListView):

    model = Thread
    paginate_by = 2
    template_name = 'forum/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context


forum = ForumView.as_view()


