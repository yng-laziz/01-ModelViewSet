from django.db import models

# Create your models here.

class UniversityModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class FacultyModel(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class GroupModel(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(FacultyModel, models.CASCADE)

    def __str__(self):
        return self.name
    

class TeacherModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class SubjectModel(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class StudentModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    