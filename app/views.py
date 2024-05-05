from django.shortcuts import render
from django.db.models import IntegerField, CharField
from .models import MyModel
import re

def fun(request):
    error_message = None
    if request.method == 'POST':
        field = request.POST.get('field')
        input_value = request.POST.get('input_value', '').strip()
        

        if not re.match(r'^[0-9]+$', input_value):
            error_message = "Invalid input."
            filtered_data = MyModel.objects.all()
            return render(request, 'index.html', {'my_models': filtered_data, 'error_message': error_message})
        
        elif field and input_value:
            field_type = MyModel._meta.get_field(field)
            if isinstance(field_type, IntegerField):
                lookup = 'exact'
            elif isinstance(field_type, CharField):
                lookup = 'icontains'
            else:
                # Handle other field types
                lookup = 'icontains'
            # Construct the filter condition based on the selected field and lookup
            filter_condition = {f"{field}__{lookup}": input_value}
            filtered_data = MyModel.objects.filter(**filter_condition)

            if not filtered_data:
                error_message = f"No Data Found for '{field}' {input_value}"
        else:
            filtered_data = MyModel.objects.all()
            return render(request, 'index.html', {'my_models': filtered_data, 'error_message': error_message})

    else:
        filtered_data = MyModel.objects.all()

    return render(request, 'index.html', {'my_models': filtered_data, 'error_message': error_message})
