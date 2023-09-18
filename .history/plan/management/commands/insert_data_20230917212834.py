import yaml
from django.core.management.base import BaseCommand
from plan.models import Member, Task

class Command(BaseCommand):
    help = 'Insert data into Django models from a YAML file'

    def add_arguments(self, parser):
        # Define an argument named 'file_path' which expects a file path as input
        parser.add_argument('file_path', type=str, help='Path to the YAML file')

    def handle(self, *args, **kwargs):
        # Get the file_path argument from command line
        file_path = kwargs['file_path']
        
        print(f'file_path:{file_path}')

        # Open and read the YAML file
        with open(file_path, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)

        # Loop through the data and create model instances
        for entry in data:
            model_name = entry['model']
            fields = entry['fields']

            # Create Member instances
            if model_name == 'yourapp.member':
                Member.objects.create(**fields)

            # Create Task instances
            elif model_name == 'yourapp.task':
                Task.objects.create(**fields)
