from django.contrib import admin

from .models import Question, Choice

# StackedInline: big pattern
# TabularInline: small pattern
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    # table head and body publish
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
