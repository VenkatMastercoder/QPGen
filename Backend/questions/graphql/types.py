from typing import List
from strawberry.relay.types import GlobalID
from strawberry.scalars import JSON
import strawberry_django
from strawberry import relay
from strawberry import auto
from questions.models import *
from users.graphql.types import UserType


@strawberry_django.type
class HelloType:
    message: JSON


@strawberry_django.type(BloomsTaxonomyLevel)
class BloomsTaxonomyLevelType(relay.Node):
    id: GlobalID
    name: auto
    description: auto


@strawberry_django.type(PreviousYearsQP)
class PreviousYearsQPType(relay.Node):
    id: GlobalID
    month: auto
    year: auto


@strawberry_django.type(Programme)
class ProgrammeType(relay.Node):
    id: GlobalID
    name: auto


@strawberry_django.type(Degree)
class DegreeType(relay.Node):
    id: GlobalID
    name: auto
    full_form: auto


@strawberry_django.type(Regulation)
class RegulationType(relay.Node):
    id: GlobalID
    year: auto


@strawberry_django.type(Department)
class DepartmentType(relay.Node):
    id: GlobalID
    programme: ProgrammeType
    degree: DegreeType
    branch: auto
    branch_code: auto
    hod: UserType


@strawberry_django.type(Subject)
class SubjectType(relay.Node):
    id: GlobalID
    code: auto
    subject_name: auto
    co: auto
    # co_description: auto
    # course_outcome: auto
    # coe: List[UserType]


@strawberry_django.type(Lesson)
class LessonType(relay.Node):
    id: GlobalID
    name: auto
    subject: SubjectType
    objective: auto
    outcome: auto


@strawberry_django.type(Topic)
class TopicType(relay.Node):
    id: GlobalID
    name: auto
    active: auto


@strawberry_django.type(Course)
class CourseType(relay.Node):
    id: GlobalID
    regulation: RegulationType
    semester: auto
    department: DepartmentType
    active: auto


@strawberry_django.type(Syllabus)
class SyllabusType(relay.Node):
    id: GlobalID
    course: CourseType
    unit: auto
    lesson: LessonType


@strawberry_django.type(MarkRange)
class MarkRangeType(relay.Node):
    id: GlobalID
    start: auto
    end: auto


@strawberry_django.type(FacultiesHandling)
class FacultiesHandlingType(relay.Node):
    id: GlobalID
    course: CourseType
    subject: SubjectType
    faculties: List[UserType]


@strawberry_django.type(Question)
class QuestionType(relay.Node):
    id: GlobalID
    lesson: LessonType
    question: auto
    answer: auto
    mark: MarkRangeType
    start_mark: auto
    end_mark: auto
    btl: BloomsTaxonomyLevelType
    difficulty: auto
    created_by: UserType
    topics: List[TopicType]
    previous_years: List[PreviousYearsQPType]
    priority: auto
    created_at: auto
    updated_at: auto
    scenario_based: auto
