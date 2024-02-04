from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from goods.models import Products
from django.db.models import Q


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    # 4 вариант полиска
    vector = SearchVector('name', 'description')
    query = SearchQuery(query)
    return Products.objects.annotate(rank=SearchRank(vector,query)).order_by('-rank')

    # 3 вариант поиска
    # return Products.objects.annotate(search=SearchVector('name','description')).filter(search=query)

    # 2 вариант поиска
    return Products.objects.filter(description__search=query)

    # 1 первый вариант поиска
    keywords = [word for word in query.split() if len(word) > 2]

# q_objects = Q()

# for token in keywords:
#     q_objects |= Q(description__icontains=token)
#     q_objects |= Q(name__icontains=token)

# return Products.objects.filter(q_objects)
