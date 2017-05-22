from django.contrib import admin
from .models import (
    Venue,
    Address,
    Review,
    UserProfile,
    Image,
    WordSearch,
    Question,
    Exam,
    ExamPaper,
    Answer,
    Selection,
    OldSelection,
    AnkiImportTextFile,
    Course,
    StudentProfile,
    SchoolClass,
    TeacherProfile,
    Post,
    UserAchievement,
    Achievement,
    Article,
    Video,
    Text,
    Step,
    Word)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_1', 'address_2', 'city', 'state', 'zip_code',
                    'country', 'area_of_city',)


class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description', 'average_cost',
                    'delivery_available',
                    'pick_up_available', 'is_banned', 'timestamp', 'id',
                    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'rating', 'is_banned', 'timestamp', 'venue')


class UserImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'user')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'timestamp')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_pic', )


class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'full_json_response', 'definition', 'timestamp')


class WordSearchAdmin(admin.ModelAdmin):
    list_display = ('search', 'timestamp')


class AnswerInline(admin.StackedInline):
    model = Answer

class SelectionInline(admin.StackedInline):
    model = Selection

class OldSelectionInline(admin.StackedInline):
    model = OldSelection


class AchievementInline(admin.StackedInline):
    model = Achievement

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'exam', 'image')
    inlines = [AnswerInline, ]


class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'created_by', 'school_class')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'question', 'is_right_answer')


class ExamPaperAdmin(admin.ModelAdmin):
    list_display = ('exam_taker', 'exam')
    inlines = [SelectionInline, OldSelectionInline]

class SelectionAdmin(admin.ModelAdmin):
    list_display = ('answer', 'exam_paper', 'timestamp')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')


class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'course', 'timestamp')
    inlines = [AchievementInline]

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('year', 'gpa', 'timestamp', 'user')

class OldSelectionAdmin(admin.ModelAdmin):
    list_display = ('answer', 'exam_paper',
                    'old_timestamp', 'timestamp',
                    'old_updated_timestamp')


class PostAdmin(admin.ModelAdmin):
    list_display = ['content', 'user',
                    'timestamp', 'school_class']


class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'points',
                    'school_class', 'created_by', 'step']


class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement', 'timestamp']


class StepAdmin(admin.ModelAdmin):
    list_display = ['name', 'school_class', 'description', 'order',
                    'exam', 'url', 'timestamp']

class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'timestamp']


class AritcleAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'order', 'url', 'image']


class AnkiImportTextFieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'user', 'title', 'timestamp']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['file', 'name', 'timestamp', 'updated']

admin.site.register(Video, VideoAdmin)
admin.site.register(AnkiImportTextFile, AnkiImportTextFieldAdmin)
admin.site.register(Article, AritcleAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
admin.site.register(UserAchievement, UserAchievementAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(WordSearch, WordSearchAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(ExamPaper, ExamPaperAdmin)
admin.site.register(Selection, SelectionAdmin)
admin.site.register(OldSelection, OldSelectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Exam, ExamAdmin)

