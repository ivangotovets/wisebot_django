from django.db import models


class Message(models.Model):
    text = models.TextField("Мудрость", blank=False, null=False)
    pub_date = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Цитаты"
        verbose_name = "Цитата"
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:16]
