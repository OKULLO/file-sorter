class ResponseException(Exception):
   def __init_(self,errorType, message =''):
      self.statuscode = statuscode
      self.message =message

   def __str__(self):
      return self.errorType + f"Ooops! An error occured: {self.message}"

     