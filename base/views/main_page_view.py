from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'base.html'


class SomeContent:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def get_args(self):
        content = {
            "title": self.title,
            "description": self.description
        }


def some_view(request):
    instance_1 = SomeContent(
        title="some tittle 1",
        description="some description 1"
    )
    instance_2 = SomeContent(
        title="some tittle 2",
        description="some description 2"
    )
    instance_3 = SomeContent(
        title="some tittle 3",
        description="some description 3"
    )
    data = []
    data.append(instance_1)
    data.append(instance_2)
    data.append(instance_3)
    context = {
        "data": data
    }

    # context = {
    #     "title": "some tittle",
    #     "description": "some description"
    # }
    return render(request, 'index.html', context=context)
