from rest_framework.permissions import BasePermission, SAFE_METHODS

from artists.models import Artist


class Artist_perm(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method in SAFE_METHODS:
                return True
            if len(Artist.objects.filter(owner_id=request.user)) > 0:
                return True
            return  False
        except:
            return False
