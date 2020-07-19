from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=32, unique=True)
    icon = models.CharField(max_length=32, verbose_name='图标', null=True, blank=True)
    weight = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = '菜单表'
        verbose_name = '菜单表'

    def __str__(self):
        return self.title

class Permission(models.Model):
    title = models.CharField(max_length=32,verbose_name="标题")
    url = models.CharField(max_length=32,verbose_name="权限")
    menu = models.ForeignKey('Menu', null=True, blank=True,on_delete=models.CASCADE)
    parent = models.ForeignKey('Permission', null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=32,null=True,blank=True,unique=True)

    class Meta:
        verbose_name_plural = '权限表'
        verbose_name = '权限表'

    def __str__(self):
        return self.title

class Role(models.Model):
    name = models.CharField(max_length=32,verbose_name="角色名称")
    permissions = models.ManyToManyField(to='Permission',verbose_name="角色权限",blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField(to='Role', verbose_name='用户所拥有的角色', blank=True)

    def __str__(self):
        return self.name