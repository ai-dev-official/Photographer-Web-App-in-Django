from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Photo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect


@login_required
def likeView(request, pk):
    #photo = Photo.objects.get(id=pk)
    photo = get_object_or_404(Photo, id=request.POST.get('photo_id'))
    photo.likes.add(request.user)
    return HttpResponseRedirect(reverse('photo', args=[pk]))

@login_required
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


class PhotoDetailView(DeleteView):
    model = Photo
    template_name = 'photos/photo.html'

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(PhotoDetailView, self).get_context_data
        stuff = get_object_or_404(Photo, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context = {'total_likes': total_likes}
        return context

@login_required
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

@login_required
def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        elif data['new-location'] != '':
            category, created = Category.objects.get_or_create(
                name=data['new-location'])

        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)


class editPhoto(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = ('title', 'category', 'image', 'description')
    template_name = 'photo_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class deletePhoto(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo_delete')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# def photo(request, slug):
#     template_name = 'photo.html'
#     photo = get_object_or_404(Photo, slug=slug)
#     comments = photo.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current photo to the comment
#             new_comment.photo = photo
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'photo': photo,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})
