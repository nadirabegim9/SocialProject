from .models import Post, Comment, Group
from modeltranslation.translator import TranslationOptions,register


@register(Post)
class ProductTranslationOptions(TranslationOptions):
    fields = ('caption', )


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text', )


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('description', )