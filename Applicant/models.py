from django.db import models
import uuid
from unixtimestampfield.fields import UnixTimeStampField

class Post(models.Model):
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.TextField()
    email = models.EmailField(max_length=256)
    phone = models.TextField() 
    full_address = models.TextField()
    name_of_university = models.TextField()
    graduation_year = models.IntegerField()
    cgpa = models.FloatField()
    experience_in_months = models.IntegerField()
    current_work_place_name = models.TextField()
    applying_in = models.TextField()
    expected_salary = models.IntegerField()
    field_buzz_reference = models.TextField()
    github_project_url = models.URLField(max_length=512)
    cv_file = models.URLField(max_length=512)
    on_spot_update_time = UnixTimeStampField(auto_now=True)
    on_spot_creation_time = UnixTimeStampField(auto_now_add=True)          
     

    def __str__(self):
        return self.tsync_id, self.name, self.email, self.phone, self.full_address, self.name_of_university, self.graduation_year, self.cgpa, self.experience_in_months, self.current_work_place_name, self.applying_in, self.expected_salary, self.field_buzz_reference, self.github_project_url, self.cv_file, self.on_spot_update_time, self.on_spot_creation_time



       