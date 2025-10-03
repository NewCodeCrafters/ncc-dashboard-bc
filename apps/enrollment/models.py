from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from apps.base.models import BaseModel
from apps.batch.models import Batch  
STATUS_CHOICES = [
    ("ACTIVE", "Active"),
    ("COMPLETED", "Completed"),
    ("DROPPED", "Dropped"),
    ("SUSPENDED", "Suspended"),
]

class StudentBatchEnrollment(BaseModel):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrollments")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="enrollments")
    enrollment_date = models.DateField(auto_now_add=True)
    enrolled_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrolled_students")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("student", "batch")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.batch.batch_name} ({self.status})"
