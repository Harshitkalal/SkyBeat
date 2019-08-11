from django.urls import reverse
from django.shortcuts import render,get_object_or_404,redirect
#from .models import Music
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
######################################
from django.contrib.auth import authenticate, login,logout
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from .models import Album
from .models import Song
from django.urls import reverse_lazy
from .forms import UserForm,LoginForm,AlbumForm
from django.db.models import Q
from django.http import  HttpResponseRedirect
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class IndexView(generic.ListView):

    template_name = 'music/index.html'
    context_object_name = 'all_albums'



    def get(self,request):
        if not request.user.is_authenticated:
            form = LoginForm
            return render(request,'music/login.html',{'form':form})
        else:
            all_albums=Album.objects.filter(user=request.user)
            albums = Album.objects.filter(user=request.user)
            song_result = Song.objects.all()
            query = request.GET.get("q")
            if query:
                albums = albums.filter(
                Q(album_title__icontains=query)|
                Q(artist__icontains=query)
                ).distinct()
                song_result = song_result.filter(
                Q(song_title__icontains=query)
                ).distinct()
                return render(request,'music/index.html',{
                'albums':albums,
                'songs':song_result,
                })
            else:
                return render(request,'music/index.html',{'albums':albums,'all_albums':all_albums})


class VisitorView(View):
    template_name = 'music/base_visitor.html'

    def get(self,request):
        return render(request,'music/base_visitor.html')




class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'



def create_album(request):
    if not request.user.is_authenticated:
        form = LoginForm
        return render(request,'music/login.html',{'form':form})
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if  form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.album_logo = request.FILES['album_logo']
            file_type = album.album_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                'album':album,
                'form':form,
                'error_message':'Image file must be PNG,JPG, or JPEG',
                }
                return render(request,'music/album_form.html',context)
            album.save()
            return render(request,'music/detail.html',{'album':album})
        context = {
        'form':form,
        }
        return render(request,'music/album_form.html',context)





class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

    def post(self,*args,**kwargs):
        self.object = self.get_object()

        if self.object.is_favorite:
            self.object.is_favorite = False
        else:
            self.object.is_favorite = True
        self.object.save()

        return redirect('music:index')

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class SongCreate(CreateView):
    model = Song
    template_name='music/song.html'
    context_object_name='album'
    fields = ['album','audio_file','song_title','is_favorite']

    #def get(self,request,album):
        #return render(request,'music/song.html',{'album':album})

class SongUpdate(UpdateView):
    model = Song
    fields = ['album','file_type','song_title','is_favorite']

    def post(self,*args,**kwargs):
        self.object = self.get_object()

        if self.object.is_favorite:
            self.object.is_favorite = False
        else:
            self.object.is_favorite = True
        self.object.save()

        #return HttpResponseRedirect(self.request.path_info)


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalised ) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User object if credential are correct

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('music:index')
        return render(request,self.template_name,{'form':form})



class LoginView(FormView):
    content ={}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super(LoginView,self).dispatch(request,*args,**kwargs)

    def get(self,request):
        content = {}
        if request.user.is_authenticated:
            return redirect(reverse('music:index'))
        content['form'] = LoginForm
        return render(request,'music/login.html',content)

    def post(self,request):
        content = {}
        username = request.POST['username']
        password = request.POST['password']

        try:
            #users = users.objects.filter()
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('music:index'))

        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with Provided credentials '
            return render('music/login.html',content)

class LogoutView(FormView):
    def get(self,request):
        form = LoginForm
        logout(request)
        return render(request,'music/login.html',{'form':form})


def songs(request,filter_by):
    if not request.user.is_authenticated:
        form = LoginForm
        return render(request,'music/login.html',{'form':form})
    else:
        try:
            song_id = []
            for album in Album.objects.filter(user=request.user):
                for song in album.song_set.all():
                    song_id.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_id)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Album.DoesNotExist:
            users_songs = []
        return render(request,'music/song_list.html',{
        'song_list':users_songs,
        'filter_by':filter_by,
        })
