import string
import random
from .models import CustomUser

def generate_identyficator():
    characters = string.ascii_uppercase+string.digits
    while True:
        identyficator = ''.join(random.choices(characters, k=5))
        if not CustomUser.objects.filter(identyficator=identyficator).exists():
            return identyficator
        