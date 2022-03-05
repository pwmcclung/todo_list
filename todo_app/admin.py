from django.contrib import admin
from todo_app.models import ToDoItems, ToDoList
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(ToDoItems)

