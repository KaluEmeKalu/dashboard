from django.contrib.auth.models import User
from . models_utils import (
    IntegerRangeField,
    image_upload_location,
    video_upload_location,
    NameTimeStampBaseModel,
    TimeStampBaseModel,
    Image
)

from dashboard.models import Article, Text

from django.db.models import (
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    ImageField,
    DecimalField,
    BooleanField,
    TextField,
    OneToOneField,
    ManyToManyField,
    FileField,
    Model
)


class Blog(TimeStampBaseModel):
    title = CharField(max_length=380, null=True, blank=True)
    content = TextField(null=True, blank=True)
    featured_image = ForeignKey(
        'Image', related_name="blogs_fm", null=True, blank=True)
    images = ManyToManyField('Image', blank=True, related_name="blogs_m" )

class Button(TimeStampBaseModel):
    button_text = CharField(max_length=180, null=True, blank=True)
    button_text_url = CharField(max_length=180, null=True, blank=True)


class Footer(TimeStampBaseModel):
    text = TextField(null=True, blank=True)
    image = ForeignKey(
        'Image', related_name="footers", null=True, blank=True)
    icons = ManyToManyField('Icon', blank=True,
                            related_name='footers')


class Icon(TimeStampBaseModel):
    icon = CharField(max_length=180, null=True, blank=True)
    url = CharField(max_length=180, null=True, blank=True)


class ImageSubsection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    chinese_title = CharField(max_length=180, null=True, blank=True)

    subtitle = CharField(max_length=180, null=True, blank=True)
    chinese_subtitle = CharField(max_length=180, null=True, blank=True)

    button_text = CharField(max_length=180, null=True, blank=True)
    chinese_button_text = CharField(max_length=180, null=True, blank=True)

    button_text_url = CharField(max_length=180, null=True, blank=True)
    chinese_button_text_url = CharField(max_length=180, null=True, blank=True)

    content = TextField(null=True, blank=True)
    chinese_content = TextField(null=True, blank=True)

    icon_class = CharField(max_length=180, null=True, blank=True)
    image = ForeignKey(
        'Image', related_name="image_subsections", null=True, blank=True)

    def __str__(self):
        return self.title


class MailingListEntry(TimeStampBaseModel):
    email = CharField(max_length=180, null=True, blank=True)
    name = CharField(max_length=180, null=True, blank=True)


class Subsection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    chinese_title = CharField(max_length=180, null=True, blank=True)

    chinese_subtitle = CharField(max_length=180, null=True, blank=True)
    subtitle = CharField(max_length=180, null=True, blank=True)

    button_text = CharField(max_length=180, null=True, blank=True)
    chinese_button_text = CharField(max_length=180, null=True, blank=True)

    chinese_content = TextField(null=True, blank=True)
    content = TextField(null=True, blank=True)

    icon_class = CharField(max_length=180, null=True, blank=True)
    button_text_url = CharField(max_length=180, null=True, blank=True)

    def __str__(self):
        return self.title


class UserProfile(TimeStampBaseModel):
    profile_pic = ForeignKey(
        'Image', null=True, blank=True, related_name='profile_pic')
    all_profile_pics = ManyToManyField(
        'Image', blank=True, related_name="all_user_profiles")
    is_student = BooleanField(default=True)
    is_faculty = BooleanField(default=False)
    points = IntegerField(default=0, blank=True, null=True)
    job_title = CharField(max_length=180, null=True, blank=True)
    user = OneToOneField(User, related_name="profile")

    def __str__(self):
        return self.user.username


class Video(NameTimeStampBaseModel):
    file = FileField(null=True, blank=True, upload_to=video_upload_location)


class Widget(TimeStampBaseModel):
    text = CharField(max_length=180, null=True, blank=True)
    icon = CharField(max_length=100, null=True, blank=True)
    count = IntegerField(default=0, null=True, blank=True)
    text_2 = CharField(max_length=180, null=True, blank=True)

    def __str__(self):
        return self.text


####################

# Numbered Sections

####################
class FirstSection(TimeStampBaseModel):
    image = ForeignKey('Image', related_name="slides", null=True, blank=True)
    section = ForeignKey('Subsection', related_name='slides',
                         null=True, blank=True)


class SecondSection(TimeStampBaseModel):
    section = ForeignKey('Subsection',
                         related_name='second_sections',
                         null=True, blank=True)
    subsection_1 = ForeignKey('Subsection',
                              related_name='second_sections_ones',
                              blank=True)
    subsection_2 = ForeignKey('Subsection',
                              related_name='second_sections_twos',
                              blank=True)
    subsection_3 = ForeignKey('Subsection',
                              related_name='second_sections_threes',
                              blank=True)
    subsection_4 = ForeignKey('Subsection',
                              related_name='second_sections_fours',
                              blank=True)


class ThirdSection(TimeStampBaseModel):
    section = ForeignKey('Subsection', related_name='third_sections',
                         null=True, blank=True)
    image = ForeignKey('Image', related_name="third_sections",
                       null=True, blank=True)


class FourthSection(TimeStampBaseModel):
    section = ForeignKey('Subsection', null=True, blank=True,
                         related_name="fourth_sections")
    subsection_1 = ForeignKey('Subsection',
                              related_name='fourth_sections_ones',
                              blank=True)
    subsection_2 = ForeignKey('Subsection',
                              related_name='fourth_sections_twos',
                              blank=True)
    subsection_3 = ForeignKey('Subsection',
                              related_name='fourth_sections_threes',
                              blank=True)
    subsection_4 = ForeignKey('Subsection',
                              related_name='fourth_sections_fours',
                              blank=True)
    image = ForeignKey('Image',
                       related_name="fourth_sections",
                       null=True, blank=True)


class FifthSection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    subsection_1 = ForeignKey('ImageSubsection',
                              related_name='fourth_sections_ones',
                              blank=True)
    subsection_2 = ForeignKey('ImageSubsection',
                              related_name='fourth_sections_twos',
                              blank=True)
    subsection_3 = ForeignKey('ImageSubsection',
                              related_name='fourth_sections_threes',
                              blank=True)
    subsection_4 = ForeignKey('ImageSubsection',
                              related_name='fourth_sections_fours',
                              blank=True)


class SixthSection(TimeStampBaseModel):
    subsection = ForeignKey('Subsection', null=True,
                            blank=True, related_name='sixth_sections')
    video_embed_url = TextField(null=True, blank=True)


class SeventhSection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    content = TextField(null=True, blank=True)
    subsection_1 = ForeignKey('ImageSubsection',
                              related_name='seventh_sections_ones',
                              blank=True)
    subsection_2 = ForeignKey('ImageSubsection',
                              related_name='seventh_sections_twos',
                              blank=True)
    subsection_3 = ForeignKey('ImageSubsection',
                              related_name='seventh_sections_threes',
                              blank=True)


class EighthSection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    subtitle = CharField(max_length=180, null=True, blank=True)
    button_1 = ForeignKey('Button', null=True, blank=True,
                          related_name='eight_section_ones')
    button_2 = ForeignKey('Button', null=True, blank=True,
                          related_name='eight_section_twos')


class NinthSection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    content = TextField(null=True, blank=True)
    faculty_1 = ForeignKey('UserProfile', null=True, blank=True,
                           related_name='eight_section_ones')
    faculty_2 = ForeignKey('UserProfile', null=True, blank=True,
                           related_name='eight_section_twos')

    faculty_3 = ForeignKey('UserProfile', null=True, blank=True,
                           related_name='eight_section_threes')
    faculty_4 = ForeignKey('UserProfile', null=True, blank=True,
                           related_name='eight_section_fours')


class TenthSection(TimeStampBaseModel):
    image = ForeignKey(
        'Image', related_name="tenth_subsections", null=True, blank=True)
    widget_1 = ForeignKey('Widget', null=True, blank=True,
                          related_name='tenth_section_ones')
    widget_2 = ForeignKey('Widget', null=True, blank=True,
                          related_name='tenth_section_twos')
    widget_3 = ForeignKey('Widget', null=True, blank=True,
                          related_name='tenth_section_threes')
    widget_4 = ForeignKey('Widget', null=True, blank=True,
                          related_name='tenth_section_fours')


class EleventhSection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    content = TextField(null=True, blank=True)
    articles = ManyToManyField(Article, blank=True, related_name="eleven_sections")


class TwelfthSection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    subtitle = CharField(max_length=180, null=True, blank=True)
    image = ForeignKey(
        'Image', related_name="twelfth_sections", null=True, blank=True)


class ThirteenthSection(TimeStampBaseModel):
    title = CharField(max_length=180, null=True, blank=True)
    widget_1 = ForeignKey('Widget', null=True, blank=True,
                          related_name='thirteenth_section_ones')
    widget_2 = ForeignKey('Widget', null=True, blank=True,
                          related_name='thirteenth_section_twos')
    widget_3 = ForeignKey('Widget', null=True, blank=True,
                          related_name='thirteenth_section_threes')
