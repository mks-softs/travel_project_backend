from rest_framework import permissions



class IsAdminUser(BasePermission):
    """
    Permet l'accès uniquement aux administrateurs.
    
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

