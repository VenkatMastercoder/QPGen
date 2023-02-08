from typing import Any
from asgiref.sync import sync_to_async
from strawberry.permission import BasePermission
from strawberry.types import Info

from questions.models import FacultiesHandling, Lesson, Question


class IsAFaculty(BasePermission):
    message = "User is not a faculty for this Subject"

    @sync_to_async
    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        if type(kwargs["input"]["lesson"]) is int:
            l = Lesson.objects.get(pk=kwargs["input"]["lesson"])
        else:
            l = Lesson.objects.get(pk=kwargs["input"]["lesson"]["id"].node_id)

        f = FacultiesHandling.objects.get(subject=l.subject)
        user = info.context.request.user
        if f.faculties.contains(user):
            return True
        return False
