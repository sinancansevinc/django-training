from django.shortcuts import render
from rest_framework import generics,mixins
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

# Create your views here.


class PlayersListView(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    # def perform_create(self, serializer):
    #     name = serializer.validated_data.get('name')
    #     if name is not None:
    #         name = 'Sinancan Sevinç'
    #     serializer.save(name=name)
        
    
    # permission_classes = [permissions.IsAuthenticated]
    
# class PlayersDetailView(generics.RetrieveAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer

# class PlayersUpdateView(generics.UpdateAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer
#     lookup_field = 'pk'
    
# class PlayersDestroyView(generics.DestroyAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer
#     lookup_field = 'pk'
    
class PlayersMixinView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'pk'
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


    # def perform_create(self, serializer):
    #     content = serializer.validated_data.get('content') or None
    #     if content is None:
    #         content = "This is single view doing cool stuff"
    #     serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    