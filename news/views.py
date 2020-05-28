from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 9
    template_name = 'news/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,  status='published',  publish__year=year,  publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
    else:
        comment_form = CommentForm()

    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()

    return render(request,
               'news/post/detail.html',
               {'post': post,
                'comments': comments,
                'new_comment': new_comment,
                'comment_form': comment_form})


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"

    template_name = "F:/newsite/templates/registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)



