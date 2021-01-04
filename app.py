from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application
import os
import sys


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bootcamp.settings')


settings.configure(
    DEBUG=True,
    SECRET_KEY = 'mt_pme9e$4c)1sm57m(ol1^-3bp^%sn_=$78n=7+qklbziti4@',
    ALLOWED_HOSTS=['*'] ,
    ROOT_URLCONF=__name__,
)

def home_view(request, *args, **kwargs):
    return HttpResponse(
    '<h1>Programming Reading List</h1>'
    '<h3><a href="https://www.barnesandnoble.com/w/elements-of-programming-interviews-in-python-tsung-hsien-lee/1131448692">Elements of Python Programming</h3>'
    '<h3><a href="https://www.barnesandnoble.com/w/introduction-to-algorithms-third-edition-thomas-h-cormen/1137257033?ean=9780262033848">Introduction to Algorithms</a></h3>'
    '<h3><a href="https://www.barnesandnoble.com/s/cracking%20the%20coding%20interview/_/N-8q8">Cracking the Coding Interview</a></h3>'
    '<h3><a href="https://www.barnesandnoble.com/w/the-pragmatic-programmer-david-thomas/1132520344?ean=9780135957059">The Pragmatic Programmer</a></h3>'
    '<h3><a href="https://www.barnesandnoble.com/w/structure-and-interpretation-of-computer-programs-second-edition-harold-abelson/1137256005?ean=9780262510875">Structure and Interpretation of Computer Programs</a></h3>'
    '<h3><a href="https://www.barnesandnoble.com/w/clean-code-robert-martin/1137736320?ean=9780132350884">Clean Code</a></h3>'
    '<h3><a href="https://www.barnesandnoble.com/w/zero-bugs-and-program-faster-kate-thompson/1123269711?ean=9780996193306">Zero Bugs and Program Faster</a></h3>'
    )


urlpatterns = [
    path('', home_view),
]

application = get_wsgi_application()

if __name__ == '__main__':
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you"
            "forget to activate a virtual environment?"
    ) from exc 
    execute_from_command_line(sys.argv)
