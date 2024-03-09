import dataclasses


@dataclasses.dataclass
class Book:
    title: str
    author: str
    price: str
    book_url: str
    book_type: str
    reader: str

book = Book(title='Златан Ибрагимович. Только бог может судить меня',
             author='Драган Маркович',
             price='449',
             book_url='/dragan-markovich/zlatan-ibragimovich-tolko-bog-mozhet-sudit-menya-69956326/',
             book_type='audiobook',
             reader='Илья Кочетков')

book2 = Book(title='Дюна. Первая трилогия',
             author='Фрэнк Герберт',
             price='799',
             book_url='/frenk-gerbert/duna-pervaya-trilogiya-25440524/',
             book_type='book',
             reader='')