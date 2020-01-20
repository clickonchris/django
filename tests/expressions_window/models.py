from django.db import models


class EmployeeClassification(models.Model):
    code = models.CharField(max_length=10, blank=False, null=False, primary_key=True)
    description = models.CharField(max_length=50, blank=False, null=False)

class Employee(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    salary = models.PositiveIntegerField()
    department = models.CharField(max_length=40, blank=False, null=False)
    hire_date = models.DateField(blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    classification = models.ForeignKey(
        to=EmployeeClassification,
        default='fte',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.name, self.department, self.salary, self.hire_date)
