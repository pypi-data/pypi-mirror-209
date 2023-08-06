from collections.abc import Sequence

#
# Random Stuff
#

def RaisesError(code: str, Ignore: Sequence[Exception] = [None,], GlobalVars: dict[str, any] = {}):
    """Runs the code and returns (True, ReturnValue) if run successfully or (False, Error) if there was an error. Can return (True, Exception) if code raised a ignored error"""
    try: 
        iter(Ignore)
    except ValueError: 
        raise ValueError("Ignore Should be an iterable")
    try: 
        dict(GlobalVars)
    except ValueError: 
        raise ValueError("GlobalVars Should be an dict")
    if not isinstance(code, str):
        raise ValueError("Code needs to be a string or isinstance(code, str) should return true")
    
    try:
        Value = eval(compile(code, '<string>', 'eval'), GlobalVars)
    except Exception as e:
        if e in Ignore:
            return (True, e)
        else:
            return (False, e)
    
    return (True, Value)
