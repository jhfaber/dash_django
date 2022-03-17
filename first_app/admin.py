from django.contrib import admin

# Register your models here.



from .models import Question, Choice

# FOR QUICK STARTER
# admin.site.register(Question)
# admin.site.register(Choice)


# We can update just a few fields (this can be customize)
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date"]



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)