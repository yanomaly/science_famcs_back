from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField


class Subjects(ChoiceEnum):
    linal = "Линейная алгебра"
    ma = "Математический анализ"


class Categories(ChoiceEnum):
    conspect = "Конспект"
    manual = "Методичка"
    book = "Книга"
    other = "Другое"


class File(models.Model):
    subject = EnumChoiceField(enum_class=Subjects, null=False)
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    category = EnumChoiceField(enum_class=Categories, null=False)
    file = models.FileField(upload_to='files/')
    
    def __str__(self) -> str:
        return self.name
