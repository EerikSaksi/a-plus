from rest_framework import serializers
from lib.api.serializers import AplusModelSerializer, AlwaysListSerializer

from ..models import UserProfile


__all__ = [
    'UserBriefSerializer',
    'UserListField',
]


class UserBriefSerializer(AplusModelSerializer):
    id = serializers.IntegerField(source='user.id', read_only=True) # NOTE: userprofile.id != user.id
    username = serializers.CharField(source='user.username')

    class Meta(AplusModelSerializer.Meta):
        model = UserProfile
        fields = (
            'username',
        )
        extra_kwargs = {
            'url': {
                'view_name': 'api:user-detail',
                'lookup_map': 'userprofile.api.views.UserViewSet',
            }
        }


class UserListField(AlwaysListSerializer, UserBriefSerializer):
    pass

