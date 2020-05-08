from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Count
from taggit.models import Tag
from .models import Post, Comment
from .forms import CommentForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import viewsets
from .pagination import CustomPagination
from rest_framework import generics
from rest_framework import status




class CommentView(APIView):
    serializer_class = CommentSerializer
   
    pagination_class = CustomPagination
    def get_queryset(self):
        comment = Comment.objects.all()
        return comment
    def get(self, request):
        comment = Comment.objects.filter(active=True)
        serializer = CommentSerializer(comment, many=True)
        return Response({"comment": serializer.data})

    def post(self, request):
        comment = Comment.objects.filter(active=True)
        serializer = CommentSerializer(data=request.data)  
        if serializer.is_valid():
            comment_saved = serializer.save()
            return Response({"success": "comment '{}' created successfully".format(comment_saved.name)})


class PostDetailAp(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = ArticleSerializer
    print(queryset)


class CommDetailAp(generics.RetrieveAPIView):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerializer
    print(queryset)

class Get_update_comm(RetrieveUpdateAPIView):
    serializer_class = CommentSerializer
   
    pagination_class = CustomPagination
    def get_queryset(self):
        comment = Comment.objects.all()
        return comment
    def get(self, request):
        comment = Comment.objects.filter(active=True)
        serializer = CommentSerializer(comment, many=True)
        return Response({"comment": serializer.data})

    def put(self, request):
        
        comment = self.get_queryset()

        if(request.user == comment.creator): 
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

  
class ArticleView(ListAPIView):
    serializer_class = ArticleSerializer
   
    pagination_class = CustomPagination
    
    def get_queryset(self):
        post = Post.objects.all()
        return post

    def get(self, request):
        post = self.get_queryset()
        paginate_queryset = self.paginate_queryset(post)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

 
    
    def retrieve(self,request, pk=None):
        queryset = Post.objects.all()
        user=get_object_or_404(queryset,pk=pk)
        serializer=ArrticleSerializer(user)
        return Response(serializer.data)    
   
class SingleArticleView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = ArticleSerializer
    

def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) 
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag})



    

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    



    
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'post':
       
        comment_form = CommentForm(data=request.post)
        if comment_form.is_valid():
           
            new_comment = comment_form.save(commit=False)
           
            new_comment.post = post
           
            new_comment.save()
    else:
        comment_form = CommentForm()

    
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
