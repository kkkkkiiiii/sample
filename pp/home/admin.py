from django.contrib import admin
from .models import Board
from .models import User
from .models import POST
from .models import Student

admin.site.register(Board)

admin.site.register(User)

admin.site.register(POST)

admin.site.register(Student)
# Register your models here.
