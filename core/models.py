from django.db import models

class Task(models.Model):

  STATUS_TASK = (
    ("doing", "Doing"),
    ("done", "Done"),
    ("pending", "Pending"),
  )

  title = models.CharField(max_length=250)
  description = models.TextField()
  status = models.CharField(
    max_length=7,
    choices=STATUS_TASK,
    default="pending"
  )

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
