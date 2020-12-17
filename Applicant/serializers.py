from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ("tsync_id", "name", "email", "phone", "full_address", "name_of_university", "graduation_year", "cgpa", "experience_in_months", "current_work_place_name", "applying_in", "expected_salary", "field_buzz_reference", "github_project_url", "cv_file", "on_spot_update_time", "on_spot_creation_time")


