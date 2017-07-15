from django.shortcuts import render
from . models import (
    FirstSection,
    SecondSection,
    ThirdSection,
    FourthSection,
    FifthSection,
    SixthSection,
    SeventhSection,
    EighthSection,
    NinthSection,
    TenthSection,
    EleventhSection,
    TwelfthSection,
    ThirteenthSection,
    Footer,
)
from dashboard.models import Article, Text
from django.shortcuts import get_object_or_404

def blog_list(request, isChinese=None):
    blogs = Article.objects.all()

    context = {'blogs': blogs, 'isChinese': isChinese}
    return render(request, 'frontpage/blog_list.html', context)


def blog_detail(request, pk, isChinese=None):
    blog = get_object_or_404(Article, pk=int(pk))
    context = {'blog': blog, 'isChinese': isChinese}

    return render(request, 'frontpage/blog_detail.html', context)


def index(request, isChinese=None):

    first_sections = FirstSection.objects.all()
    first_section = first_sections.first()
    context = {'isChinese': isChinese}


    try:
        context['first_sections'] = first_sections
        context['first_section'] = first_section

        # Get Second SubSection
        context['second_subsection'] = SecondSection.objects.first()

        # Get Third SubSection
        context['third_subsection'] = ThirdSection.objects.first()

        # Get Fourth SubSection
        context['fourth_subsection'] = FourthSection.objects.first()


        # Get Fifth SubSection
        context['fifth_section'] = FifthSection.objects.first()

        # Get Sixth SubSection
        context['sixth_section'] = SixthSection.objects.first()

        # Get Seventh SubSection
        context['seventh_section'] = SeventhSection.objects.first()

        # Get eighth SubSection
        context['eighth_section'] = EighthSection.objects.first()

        # Get eighth SubSection
        context['eighth_section'] = EighthSection.objects.first()

        # Get ninth SubSection
        context['ninth_section'] = NinthSection.objects.first()

        # Get tenth SubSection
        context['tenth_section'] = TenthSection.objects.first()

        # Get Eleventh Section
        context['eleventh_section'] = EleventhSection.objects.first()

        # Get Twelfth Section
        context['twelfth_section'] = TwelfthSection.objects.first()

        # Get ThirteenthSection Section
        context['thirteenth_section'] = ThirteenthSection.objects.first()

        # Get Footer Section
        context['footer'] = Footer.objects.first()
    except:
        pass



    return render(request, "frontpage/index.html", context)


def blog(request, isChinese=None):
    context = {'isChinese': isChinese}
    return render(request, 'frontpage/blog.html', context)
