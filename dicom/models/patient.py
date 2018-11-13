from django.db import models
from django.urls import reverse
from research.models import Subject
from .choices import Sex
from .validators import digits_only


class Patient(models.Model):
    patient_uid = models.CharField(
        max_length=64,
        unique=True,
        validators=[digits_only],
    )
    given_name = models.CharField(max_length=64, blank=True)
    family_name = models.CharField(max_length=64, blank=True)
    middle_name = models.CharField(max_length=64, blank=True)
    name_prefix = models.CharField(max_length=64, blank=True)
    name_suffix = models.CharField(max_length=64, blank=True)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    sex = models.CharField(
        max_length=6,
        choices=Sex.choices(),
        blank=True,
    )

    subject = models.OneToOneField(
        Subject,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.patient_uid

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])

    def get_name_id(self):
        return f'{self.family_name[:2]}{self.given_name[:2]}'

    def get_subject_attributes(self) -> dict:
        return {
            'first_name': self.given_name,
            'last_name': self.family_name,
            'date_of_birth': self.date_of_birth,
            'sex': self.sex,
            'id_number': self.patient_uid,
        }

    def find_subject(self):
        return Subject.objects.filter(id_number=self.patient_uid).first()

    def create_subject(self):
        return Subject.objects.create(**self.get_subject_attributes())

    def get_subject(self):
        if not self.subject:
            existing_subject = self.find_subject()
            if not existing_subject:
                return self.create_subject()
            return existing_subject
        return self.subject
