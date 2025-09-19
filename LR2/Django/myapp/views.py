from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

Course_data = [
    {
        'title' : 'Математика в ИТ', 
        'instructor' : 'Дубенцова А.В.', 
        'date' : '13.12.2023', 
        'image' : '1.svg', 
        'duration' : '6',
        'description' : 'Взаимосвязанные области знаний, где математика служит фундаментальной основой для разработки новых методов и инструментов.'
    },
    {
        'title' : 'Информатика в бизнесе', 
        'instructor' : 'Неткор Г.Д.', 
        'date' : '23.02.2024', 
        'image' : '2.svg', 
        'duration' : '14',
        'description' : 'Междисциплинарная область, объединяющая информационные технологии и экономические знания.'
    },
    {
        'title' : 'Искусство и живопись', 
        'instructor' : 'Малевич Ж.З.', 
        'date' : '15.01.2023', 
        'image' : '3.svg', 
        'duration' : '5',
        'description' : 'Это художественное творчество в целом, общий класс пространственных искусств, который объединяет разные творческие направления: живопись, скульптуру, графику, архитектуру, дизайн и фотографию.'
    },
    {
        'title' : 'Английский для ИТ специалистов', 
        'instructor' : 'Гаймори Л.С.', 
        'date' : '18.08.2022', 
        'image' : '4.svg', 
        'duration' : '25',
        'description' : 'Включает информацию о целях изучения языка, необходимых навыках и методах обучения, а также о ресурсах для изучения.'
    },
    {
        'title' : 'Польский в описательных формах', 
        'instructor' : 'Живцова П.С.', 
        'date' : '21.12.2023', 
        'image' : '5.svg', 
        'duration' : '12',
        'description' : 'Включает информацию о целях изучения языка, необходимых навыках и методах обучения, а также о ресурсах для изучения.'
    },
    {
        'title' : 'Трансцендентность производства', 
        'instructor' : 'Йелова К.С.', 
        'date' : '22.04.2022', 
        'image' : '6.svg', 
        'duration' : '8',
        'description' : 'Трансцендентность в производстве связана с влиянием непознанной составляющей внешней среды на происходящие процессы. Это влияние может быть как спонтанным, так и спровоцированным человеком.'
    },
    {
        'title' : 'Начала физики', 
        'instructor' : 'Габен Ф.Р.', 
        'date' : '16.03.2024', 
        'image' : '7.svg', 
        'duration' : '7',
        'description' : 'Подробно изложен теоретический материал по всем темам программы физики средней школы, а также приведены решения более 450 примеров и задач.'
    },
    {
        'title' : 'Веб-дизайн', 
        'instructor' : 'Жульман Й.Г.', 
        'date' : '11.01.2021', 
        'image' : '8.svg', 
        'duration' : '5',
        'description' : 'Включает в себя не только визуальные элементы, но и структуру, функциональность и взаимодействие с пользователем.'
    },
    {
        'title' : 'Машинное обучение на практике', 
        'instructor' : 'Айдахо К.Ж.', 
        'date' : '10.05.2023', 
        'image' : '9.svg', 
        'duration' : '10',
        'description' : 'Описание машинного обучения включает принцип работы, виды, алгоритмы и области применения.'
    },
]

def index(request):
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')

    context = {
        'courses' : Course_data,
        'theme' : theme,
        'language' : language,
    }
    return render(request, 'myapp/index.html', context)

def settings_view(request):
    if request.method == 'POST':
        # Сохраняем настройки в cookies
        theme = request.POST.get('theme')
        language = request.POST.get('language')
        
        response = redirect('index')
        response.set_cookie('theme', theme, max_age=30*24*60*60)
        response.set_cookie('language', language, max_age=30*24*60*60)
        return response
    
    # Получаем текущие настройки
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    
    return render(request, 'myapp/settings.html', {
        'theme': theme,
        'language': language
    })