from django.db import models


class MenuAbsctractModel(models.Model):
    """ Basic fields for menu models """
    name = models.CharField(max_length=100, verbose_name='Name')
    slug = models.SlugField(max_length=100, verbose_name='Slug')
    order = models.IntegerField(default=0, verbose_name='Order')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    class Meta:
        abstract = True


class Menu(MenuAbsctractModel):
    """ Menu model """

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        ordering = ("order",)

    def __str__(self):
        return self.name


class MenuItem(MenuAbsctractModel):
    """ Menu Item model """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                             verbose_name='Menu')
    parent = models.ForeignKey("self", null=True, blank=True,
                               on_delete=models.SET_NULL,
                               verbose_name='Parent Item')

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
        ordering = ("order",)

    def __str__(self):
        return f'{self.menu.name}/{self.name}'
