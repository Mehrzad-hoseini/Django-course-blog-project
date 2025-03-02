from django.views import generic
from django.urls import reverse_lazy



from blog.models import Post
from .forms import PostForm






class PostListView(generic.ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_updated')




class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'



class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/create_post.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('post_list')

# def post_delete_view(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('post_list')
#
#
#     return render(request,'blog/delete_post.html', {'post': post})

# def post_update_view(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#
#     return render(request,'blog/create_post.html', {'form': form})

# def post_create_view(request):
#     if request.method == "POST":
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = NewPostForm()
#
#
#     return render(request, 'blog/create_post.html', {'form': form})

# Create your views here.

# def post_list_view(request):
#     posts = Post.objects.filter(status="pub").order_by('-datetime_updated')
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
