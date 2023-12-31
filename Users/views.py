from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from Users.models import User
from Users.serializers import UpdateUserSerializer


class UpdateUserView(UpdateAPIView):
    """
    View for updating a new user.
    """
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
