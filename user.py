#!/user/bin/python3
"""Defines the user from BaseModel."""
from models.base_models import BaseModel


class User(BaseModel)
      """Represent a User.
      
        Attributes: 
         email(str): The email of the user.
         password(str): The password of the user.
         fistName(str): The first name of the user.
         lastName(str): The lastName of the user.
         """
    
       email = ""
       password = ""
       fist_name = ""
       last_name = ""
  
