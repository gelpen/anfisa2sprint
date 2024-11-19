# # homepage/views.py
# from django.shortcuts import render

# from ice_cream.models import IceCream

# def index(request):
#     template_name = 'homepage/index.html'
#     # Возьмём нужное. А ненужное не возьмём:
#     ice_cream_list = IceCream.objects.values(
#             'id', 'title', 'description'
#         # Верни только те объекты, у которых в поле is_on_main указано True:
#         #).filter(is_on_main=True)
#         # Исключи те объекты, у которых is_published=False:
#         #).exclude(is_published=False)
#         #).filter(is_published=True, is_on_main=True) # Два в одном!
#          ).filter(
#         # Делаем запрос, объединяя два условия
#         # через Q-объекты и оператор AND:
#         Q(is_published=True) & Q(is_on_main=True)
#     )
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     return render(request, template_name, context)


###################################################################

# # homepage/views.py
# from django.shortcuts import render
# from django.db import connection

# def index(request):
#     template_name = 'homepage/index.html'

#     # Прямой SQL-запрос для выборки данных
#     query = """
#         SELECT "ice_cream_icecream"."id",
#        "ice_cream_icecream"."title",
#        "ice_cream_icecream"."description"
#         FROM "ice_cream_icecream"
#         WHERE ("ice_cream_icecream"."is_published" AND ("ice_cream_icecream"."is_on_main" OR "ice_cream_icecream"."title" LIKE '''%пломбир%''' LIKE '\'))
#     """
#     def get_ice_cream_list():
#         with connection.cursor() as cursor:
#             cursor.execute(query)
#             rows = cursor.fetchall()
#             columns = [col[0] for col in cursor.description]
#             return [
#                 dict(zip(columns, row))
#                 for row in rows
#             ]

#     # Получение списка мороженого с использованием прямого SQL-запроса
#     ice_cream_list = get_ice_cream_list()
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     return render(request, template_name, context)


####################### вариант решения из урока

from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    # Для переноса длинной строки замыкаем её в скобки.
    # Будьте внимательны.
    ice_cream_list = IceCream.objects.values(
        'title', 'description'
    ).filter(
        Q(is_on_main=True)
        & Q(is_published=True)
        | Q(title__contains='пломбир')
        & Q(is_published=True)
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)