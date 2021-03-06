from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.
class ProjectModel(models.Model):
    name = models.CharField(max_length=265, null=False, unique=True)
    languages = models.ManyToManyField("Language", related_name="languages")
    technologies = models.ManyToManyField("Technology", related_name="technologies")
    description = models.TextField(null=False)
    image = models.ImageField( blank=True, upload_to="Project_Images")
    link_to_code = models.CharField("link To code", max_length=100, null=True)
    link_to_project = models.CharField("Link to project", max_length=100, null=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name= models.CharField(_(""), max_length=50, blank=False, null=False, unique=True)
    logo = models.ImageField( blank=True, upload_to="Language_Images")

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Language_detail", kwargs={"pk": self.pk})

class Technology(models.Model):
    name = models.CharField(_(""), max_length=50, null=False, unique=True)
    logo = models.ImageField( blank=True, upload_to="Tech_Images")


    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologyies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Technology_detail", kwargs={"pk": self.pk})
