import sys
import logging 

'''
just created a custom exception class that behaves like a normal python error but also stores file name and line number where the error happened 
'''
def error_message_details(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()   
    ##execution info(returns 3 values (type, value, traceback), we just need the third one)

    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="error occured in python script name [{0}] line number [{1} error message [{2}]]".format(
      file_name,
      exc_tb.tb_lineno, 
      str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):  ##constructor
        super().__init__(error_message)  ##callparent class constructor(exception)
        self.error_message=error_message_details(error_message, error_detail)  ##store value inside the object

    def __str__(self):
        return self.error_message
    

