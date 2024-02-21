from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from django.db import models


class Subjects(ChoiceEnum):
    aisd = "АиСД (ТА)"
    aitch = "АиТЧ"
    angl = "Английский язык"
    bzch = "БЖЧ"
    vkad = "ВКиАД"
    vma = "ВМА"
    dii = "ДиИИ (МА)"
    dmiml = "ДМиМЛ"
    du = "ДУ"
    iso = "ИСО"
    hist = "История"
    ks = "КС"
    mv = "МВ"
    subd = "МДиСУБД"
    mop = "МОП"
    mo = "МО"
    mt = "МТ" 
    ni = "НИ"
    oviag = "ОВиАГ (ГА)"
    oimp = "ОиМП"
    os = "ОС"
    pp = "ПП"
    rifk = "РиФКА"
    rkpp = "РКПП"
    tvims = "ТВиМС"
    tm = "ТерМех (ТМ)"
    tfkp = "ТФКП"
    tp = "ТП"
    umf = "УМФ (УРЧП)"
    faiiu = "ФАиИУ"
    ma = "ЧиФР"
    chma = "ЧМ (МЧА)"
    chmmf = "ЧММФ"
    econ = "Экономика"
    other = "Другое"


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
