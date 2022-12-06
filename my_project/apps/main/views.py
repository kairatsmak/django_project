from django.shortcuts import (
    render,
    HttpResponse
)
from django.http.request import HttpRequest

def index(request):
    numbers: list[int] = [i for i in range(1, 11)]
    # i: int
    # for i in range(1, 11):
    #     numbers.append(i)


    context_data: dict[str: str] = {
        'ctx_title': "Заголовок главной страницы",
        'ctx_numbers': numbers
    }
    
    return render(
        request,
        template_name='main/index.html',
        context=context_data
    )