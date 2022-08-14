from django.shortcuts import render

# Create your views here.


def string(request, lang):
    context = {'text': []}
    if lang == 'original':
        context['text'] = ["«We are the champions, my friends", "And we’ll keep on fighting till the end». "]
    elif lang == 'ukr':
        context['text'] = ["«Ми чемпіони, друзі, і будемо боротися до кінця»."]
    elif lang == 'fr':
        context['text'] = ["«Nous sommes les champions, mes amis", "Et nous continuerons à nous battre jusqu'au bout»."]
    elif lang == 'de':
        context['text'] = ["«Wir sind die Champions, meine Freunde,", "und wir werden bis zum Ende weiterkämpfen»."]
    elif lang == 'es':
        context['text'] = ["«Somos los campeones, amigos míos,", "y seguiremos luchando hasta el final»."]
    else:
        context['text'] = ["«We are the champions, my friends", "And we’ll keep on fighting till the end». "]
        context['error'] = 'Sorry, there is not such language'

    context['author'] = 'Queen, We are the champions'
    return render(request, 'index1.html', context=context)


def cars(request, name):
    context = dict()
    if name == 'toyota':
        context['name'] = 'Toyota'
        context['img'] = 'https://cdn.f1ne.ws/userfiles/toyota/53703.jpg'
    elif name == 'honda':
        context['name'] = 'Honda'
        context['img'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Honda.svg/800px-Honda.svg.png'
    elif name == 'renault':
        context['name'] = 'Renault'
        context['img'] = 'https://upload.wikimedia.org/wikipedia/commons/' \
                         'thumb/a/ad/RENAULT_LOGO.png/800px-RENAULT_LOGO.png'
    else:
        context['error'] = 'We do not have such directory'
    return render(request, 'index2.html', context=context)


def week(request, day):
    context = dict()
    days = {'mon': ['Monday', 'https://previews.123rf.com/images/novelo/novelo1301/'
                              'novelo130100005/17358043-monday-day-of-the-week-multicolored-over-white-background.jpg'],
            'tue': ['Tuesday', 'https://image.shutterstock.com/shutterstock/photos/118245319/display_1500/'
                               'stock-photo-tuesday-day-of-the-week-multicolored-over-white-background-118245319.jpg'],
            'wed': ['Wednesday', 'https://previews.123rf.com/images/novelo/novelo1301/novelo130100010/'
                                 '17358046-wednesday-day-of-the-week-multicolored-over-white-background.jpg'],
            'thu': ['Thursday', 'https://previews.123rf.com/images/novelo/novelo1301/novelo130100008/'
                                '17358048-thursday-day-of-the-week-multicolored-over-white-background.jpg'],
            'fr': ['Friday', 'https://cdn.w600.comps.canstockphoto.ru/'
                             'неделю-над-пятница-многоцветный-стоковая-иллюстрация_csp11531367.jpg'],
            'sat': ['Saturday', 'https://image.shutterstock.com/shutterstock/photos/118245331/display_1500/'
                                'stock-photo-saturday-day-of-the-week-multicolored-over-white-background-118245331.jpg'],
            'sun': ['Sunday', 'https://cdn.w600.comps.canstockphoto.com/'
                              'sunday-day-of-the-week-multicolored-picture_csp11531372.jpg']}
    context['day'] = days[day][0]
    context['img'] = days[day][1]
    return render(request, 'index3.html', context=context)
