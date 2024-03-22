import inspect
import typing

def validate_types(func):
    signature = inspect.signature(func)
    
    def wrapper(*args, **kwargs):
        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()
        
        for param_name, param_value in bound_arguments.arguments.items():
            param_annotation = signature.parameters[param_name].annotation
            
            # Skip type checking if the annotation is Any or not provided
            # noqa: flake8
            if param_annotation == inspect.Parameter.empty or param_annotation == typing.Any:
                continue
            
            # Perform type checking
            # noqa: flake8
            if not isinstance(param_value, param_annotation):
                raise TypeError(f"Parameter '{param_name}' expected type '{param_annotation}', got '{type(param_value)}'")
        
        return func(*args, **kwargs)
    
    return wrapper
