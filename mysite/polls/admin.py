from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_txt', 'pub_date']
    fieldsets = [
        (None,                  {'fields': ['question_txt']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_txt', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_txt']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
