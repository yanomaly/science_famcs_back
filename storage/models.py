from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField


class Subjects(ChoiceEnum):
    ma = "Математический анализ"
    linal = "Линейная алгебра"


class Categories(ChoiceEnum):
    conspect = "Конспект"
    manual = "Методичка"
    book = "Книга"
    other = "Другое"


class File(models.Model):
    subject = EnumChoiceField(enum_class=Subjects, null=False, blank=True)
    name = models.CharField(max_length=100, null=False, blank=True)
    author = models.CharField(max_length=100, null=False, blank=True)
    category = EnumChoiceField(enum_class=Categories, null=False, blank=True)
    file = models.FileField(upload_to='files/')
    