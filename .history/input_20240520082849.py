import os
import django

# Configure Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from your_app.models import Requirement, RequirementRelationship

# Define data to be saved
requirement_data = [
    {
        'name': 'Requirement 1',
        'status': '未开始',
        'description': 'Description for Requirement 1',
        'priority': 1,
        # Add more fields as needed
    },
    {
        'name': 'Requirement 2',
        'status': '进行中',
        'description': 'Description for Requirement 2',
        'priority': 2,
        # Add more fields as needed
    },
    # Add more requirement data as needed
]

relationship_data = [
    {
        'from_requirement_name': 'Requirement 1',
        'to_requirement_name': 'Requirement 2',
    },
    # Add more relationship data as needed
]

# Save Requirement instances
for data in requirement_data:
    requirement = Requirement.objects.create(**data)
    print(f"Saved Requirement: {requirement}")

# Save RequirementRelationship instances
for data in relationship_data:
    from_requirement_name = data.pop('from_requirement_name')
    to_requirement_name = data.pop('to_requirement_name')

    from_requirement = Requirement.objects.get(name=from_requirement_name)
    to_requirement = Requirement.objects.get(name=to_requirement_name)

    relationship = RequirementRelationship.objects.create(from_requirement=from_requirement, to_requirement=to_requirement, **data)
    print(f"Saved RequirementRelationship: {relationship}")
