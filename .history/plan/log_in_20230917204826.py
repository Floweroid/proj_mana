import yaml
from datetime import datetime
from django.utils import timezone
from models import Task

# Load and parse the YAML data
with open('data.yml', 'r') as yaml_file:
    yaml_data_list = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Define the input format of the time strings in your YAML data
input_time_format = "%m-%d-%Y %H-%M-%S"

# Iterate through the list of YAML objects
for yaml_data in yaml_data_list:
    # Convert time strings to datetime objects
    start_time_str = yaml_data["start_time"]
    end_time_str = yaml_data["end_time"]

    start_time = datetime.strptime(start_time_str, input_time_format)
    end_time = datetime.strptime(end_time_str, input_time_format)

    # Set the timezone if needed (e.g., UTC)
    start_time = timezone.make_aware(start_time)
    end_time = timezone.make_aware(end_time)

    # Create a Task instance with the parsed data
    task = Task(
        title=yaml_data["title"],
        description=yaml_data["description"],
        start_time=start_time,
        end_time=end_time,
    )

    # Save the Task instance to the database
    task.save()