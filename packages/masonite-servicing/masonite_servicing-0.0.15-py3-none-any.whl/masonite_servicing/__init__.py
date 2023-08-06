# flake8: noqa F401
from .providers.ServicingProvider import ServicingProvider
from masonite.validation import Validator

import uuid

# result status constants
OK = True 
NOT_OK = False 

# service result class
class ServiceResult: 
    def __init__(self, status, message, value): 
        self.id = ServiceResult.generate_id() 
        self.status = status 
        self.message = message 
        self.value = value

    def is_ok(self): 
        """ 
            Checks if the service result is ok.
        """ 
        return self.status == OK 

    def is_not_ok(self): 
        """ 
            Checks if the service result is not ok.
        """ 
        return self.status == NOT_OK 

    def generate_id():
        """ 
            Generates an id for the service result.
        """ 
        return str(uuid.uuid4())

    def get(self):
        """
            Gets the value in a service result.   
        """
        return self.value
 
def relay(value): 
    return value

def ok(message, value): 
    """ 
        Creates an affirmative ResultObject.
    """ 
    return ServiceResult(OK, message, value)

def not_ok(message, value): 
    """
        Creates a non-affirmative ServiceResult object. 
    """ 
    return ServiceResult(NOT_OK, message, value)

def same(result_a, result_b):
    """
        Checks if two results are the same.  
    """ 

    # check if types are the same first 
    if type(result_a) is not type(result_b): 
        raise Exception(f"Type Error: Result A {result_a} must of the same type of Result B {result_b}")

    # check if values are the same
    return (
        (result_a.id == result_b.id) 
        and 
        (result_a.status == result_b.status)
        and 
        (result_a.message == result_b.message)
    )

def respond(request, validations, callback): 
    """ 
        Encapsulates a route response from a service call.
    """ 

    # check if there are errors 
    errors = request.validate(*validations) 
    
    # if there are errors, return validation error messages
    # as the response 
    if errors: 
        return {
            "status": "input-error", 
            "message": "VALIDATION_ERROR", 
            "value": errors.all(), 
            "is_validation_error": True
        }

    # call and return callback function
    result = callback() 

    # transform result to dictionary 
    result_dict = {
        "status" : "ok" if result.status else "not-ok", 
        "message" : result.message, 
        "value" : result.value
    }

    return result_dict 

class ValidationTester: 
    def __init__(self): 
        self.should_error = [] 
        self.should_pass = []  
        self.validation = None 

    def run(self, context): 
        should_error = self.should_error
        should_pass = self.should_pass 

        _errors = []

        # handle should error cases 
        for value in should_error: 
            errors = Validator().validate({ "field" : value }, self.validation("field"))
            if not errors: 
                _errors.append("Value [" + str(value) + "] should error for validation [" + str(self.validation) + "]")

        # handle should pass cases 
        for value in should_pass: 
            errors = Validator().validate({ "field" : value }, self.validation("field"))
            if errors: 
                _errors.append("Value [" + str(value) + "] should pass for validation [" + str(self.validation) + "]")

        for error in _errors:
            context.dump(error) 

        if len(_errors) > 0: 
            assert(False)

class RouteTester: 
    def __init__(self):
        self.should_error = [] 
        self.should_pass = [] 
        self.route = "/" 
        self.method = "get"

    def run(self, context):
        should_error = self.should_error
        should_pass = self.should_pass 

        route_caller = getattr(context, self.method) 
        
        # handle should error cases
        for _input in should_error:
            route_caller(self.route, _input).assertJson({
                "status": "input-error", 
                "message": "VALIDATION_ERROR"
            })

        # handle should pass cases 
        for _input in should_pass: 
            route_caller(self.route, _input).assertJsonMissing("is_validation_error")

        

