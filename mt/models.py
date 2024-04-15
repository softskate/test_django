from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)
    menu_name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.named_url:
            from django.urls import reverse
            return reverse(self.named_url)
        return self.url
    
    def get_descendants(self, include_self=False):
        """
        Возвращает список всех потомков данного пункта меню (включая внуков и т.д.).
        """
        descendants = []
        if include_self:
            descendants.append(self)
        for child in self.children.all():
            descendants.extend(child.get_descendants(include_self=True))
        return descendants