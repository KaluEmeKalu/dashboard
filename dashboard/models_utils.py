from django.contrib.humanize.templatetags.humanize import naturaltime
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
from imagekit.models import ProcessedImageField
from imagekit.processors import Transpose



def image_upload_location(instance, filename):
    return "images/{}".format(filename)


class IntegerRangeField(IntegerField):
    def __init__(self, verbose_name=None, name=None,
                 min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class NameTimeStampBaseModel(Model):

    name = CharField(max_length=80, null=True, blank=True)
    timestamp = DateTimeField(
        editable=False, auto_now_add=True, auto_now=False)
    updated = DateTimeField(auto_now=True, blank=True, null=True)

    def time_ago(self):
        return naturaltime(self.timestamp)

    def __str__(self, name=None):
        """
        If model has name set that as name.

        If model has name or name set by subclass
            Then return that name
        Else return "Class_Name object #*number* cretaed on *date*"
        """
        if self.name:
            name = self.name

        if name:
            return name
        else:
            return "{} object #{} created on {}".format(
                self.__class__.__name__, self.id, self.timestamp
            )

    class Meta:
        abstract = True


class Image(NameTimeStampBaseModel):
    # user = OneToOneField(User, related_name="image", null=True, blank=True)
    # content_object = GenericForeignKey('content_type', 'object_id')
    image = ProcessedImageField(processors=[  # ResizeToFill(
        # 100, 50),
        Transpose()],
        upload_to=image_upload_location,
        null=True,
        blank=True,
        format='JPEG',
        options={'quality': 60})
    my_namespace = CharField(
        default="", max_length=128, null=True, blank=True)
    

    def get_timestamp(self, pretty=False):

        if pretty:
            return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

        return self.timestamp.strftime("%Y-%m-%d_%H:%M:%S")
