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


def index(request):
    first_sections = FirstSection.objects.all()
    first_section = first_sections.first()
    context = {}


    try:
        context = {'first_sections': first_sections, 'first_section': first_section}

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
