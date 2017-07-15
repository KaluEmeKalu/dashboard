from django.contrib import admin

from . models import (
    Button,
    Blog,
    Widget,
    FirstSection,
    Image,
    Subsection,
    SecondSection,
    FourthSection,
    ThirdSection,
    FifthSection,
    ImageSubsection,
    SixthSection,
    SeventhSection,
    EighthSection,
    UserProfile,
    Video,
    NinthSection,
    TenthSection,
    EleventhSection,
    TwelfthSection,
    ThirteenthSection,
    Footer,
    Icon,
    Article,
    Text,
    UniversitySection,
)


class UniversitySectionAdmin(admin.ModelAdmin):
    list_display = ['image_1', 'image_2', 'image_3', 'image_4']


class FirstSectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'image']


class SubsectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'subtitle', 'chinese_subtitle',
                    'icon_class', 'chinese_content', 'content', 'chinese_content',
                    'button_text', 'chinese_button_text', 'button_text_url']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'my_namespace', 'timestamp']


class SecondSectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'subsection_1', 'subsection_2',
                    'subsection_3', 'subsection_4']


class ThirdSectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'image']


class FourthSectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'subsection_1', 'subsection_2',
                    'subsection_3', 'subsection_4']


class FifthSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'subsection_1', 'subsection_2',
                    'subsection_3', 'subsection_4']



class ImageSubsectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'image', 'subtitle',
                    'chinese_subtitle', 'icon_class', 'chinese_content',
                    'content', 'button_text', 'chinese_button_text',
                    'button_text_url']


class SixthSectionAdmin(admin.ModelAdmin):
    list_display = ['subsection', 'video_embed_url']


class SeventhSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'content', 'chinese_content', 'subsection_1',
                    'subsection_2', 'subsection_3']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated', 'file']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_pic', 'is_faculty', 'is_student',
                    'job_title', 'points']


class EighthSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'subtitle', 'chinese_subtitle', 'button_1', 'button_2']


class NinthSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'content']


class ButtonAdmin(admin.ModelAdmin):
    list_display = ['button_text', 'chinese_button_text', 'button_text_url']


class WidgetAdmin(admin.ModelAdmin):
    list_display = ['text', 'chinese_text', 'text_2', 'chinese_text_2', 'icon', 'count']


class TenthSectionAdmin(admin.ModelAdmin):
    list_display = ['image', 'widget_1', 'widget_2',
                    'widget_3', 'widget_4']

class EleventhSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title',]


class ThirteenthSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'widget_1', 'widget_2',
                    'widget_3']


class IconAdmin(admin.ModelAdmin):
    list_display = ['icon', 'url']


class FooterAdmin(admin.ModelAdmin):
    list_display = ['text', 'image']


class TwelfthSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'subtitle', 'chinese_subtitle', 'image']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 'content', 'chinese_content', 'featured_image']


admin.site.register(UniversitySection, UniversitySectionAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Icon, IconAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(TwelfthSection, TwelfthSectionAdmin)
admin.site.register(EleventhSection, EleventhSectionAdmin)
admin.site.register(ThirteenthSection, ThirteenthSectionAdmin)
admin.site.register(TenthSection, TenthSectionAdmin)
admin.site.register(Widget, WidgetAdmin)
admin.site.register(Button, ButtonAdmin)
admin.site.register(NinthSection, NinthSectionAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EighthSection, EighthSectionAdmin)
admin.site.register(SeventhSection, SeventhSectionAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(SixthSection, SixthSectionAdmin)
admin.site.register(ImageSubsection, ImageSubsectionAdmin)
admin.site.register(FifthSection, FifthSectionAdmin)
admin.site.register(ThirdSection, ThirdSectionAdmin)
admin.site.register(SecondSection, SecondSectionAdmin)
admin.site.register(FirstSection, FirstSectionAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(FourthSection, FourthSectionAdmin)
