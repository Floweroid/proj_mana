from django.core.management.base import BaseCommand
from yourapp.models import Task, Member, Assignment
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create Member instances
        member1 = Member.objects.create(name='Member 1')
        member2 = Member.objects create(name='Member 2')

        # Create Task instances with formatted time and status
        task1 = Task(
            title='Task 1',
            description='Description for Task 1',
            start_time=datetime.strptime('09-17-2023 12-30-00', "%m-%d-%Y %H-%M-%S"),
            end_time=datetime.strptime('09-17-2023 14-00-00', "%m-%d-%Y %H-%M-%S"),
            status='Pending',
        )
        task1.save()

        task2 = Task(
            title='Task 2',
            description='Description for Task 2',
            start_time=datetime.strptime('09-18-2023 10-00-00', "%m-%d-%Y %H-%M-%S"),
            end_time=datetime.strptime('09-18-2023 11-30-00', "%m-%d-%Y %H-%M-%S"),
            status='InProgress',
        )
        task2.save()

        # Create Assignment instances to associate members with tasks
        assignment1 = Assignment(member=member1, task=task1)
        assignment1.save()

        assignment2 = Assignment(member=member2, task=task2)
        assignment2.save()

        # Add more data as needed