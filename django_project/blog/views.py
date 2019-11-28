from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Richard McClintock',
        'title': 'Ancient Latin Literature Series - 1',
        'content': '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis doloribus repellendus dignissimos voluptas
        veritatis quia necessitatibus suscipit expedita. Quis recusandae aspernatur atque praesentium ipsum laudantium
        doloribus aliquam mollitia saepe provident quos, veritatis dignissimos quas excepturi ullam quidem, quam quia iure
        animi sint velit. Ipsum accusantium pariatur autem iusto commodi et aliquam modi ullam, reprehenderit suscipit eius
        aspernatur doloremque alias repellendus iure id quae voluptatem obcaecati nesciunt, rem corporis vero hic nam?
        Soluta deserunt quam quaerat non. Non totam soluta sit.''',
        'date_posted': 'Near 45 BC'
    },
    {
        'author': 'Richard McClintock',
        'title': 'Ancient Latin Literature Series - 2',
        'content': '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis doloribus repellendus dignissimos voluptas
        veritatis quia necessitatibus suscipit expedita. Quis recusandae aspernatur atque praesentium ipsum laudantium
        doloribus aliquam mollitia saepe provident quos, veritatis dignissimos quas excepturi ullam quidem, quam quia iure
        animi sint velit. Ipsum accusantium pariatur autem iusto commodi et aliquam modi ullam, reprehenderit suscipit eius
        aspernatur doloremque alias repellendus iure id quae voluptatem obcaecati nesciunt, rem corporis vero hic nam?
        Soluta deserunt quam quaerat non. Non totam soluta sit.''',
        'date_posted': 'Near 45 BC'
    },

]


def home(request):
    context = {
        'context_post': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
