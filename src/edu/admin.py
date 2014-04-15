from django.contrib import admin

from .models import Article, Pathogen, Iso, Prevention, HAI, PathType

class PathogenAdmin(admin.ModelAdmin):
    class Meta:
        model = Pathogen
        
class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article
        
class IsoAdmin(admin.ModelAdmin):
    class Meta:
        model = Iso
        
class PreventionAdmin(admin.ModelAdmin):
    class Meta:
        model = Prevention
        
class HAIAdmin(admin.ModelAdmin):
    class Meta:
        model = HAI
        
class PathTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = PathType
        

admin.site.register(Prevention, PreventionAdmin)
admin.site.register(Pathogen, PathogenAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Iso, IsoAdmin)
admin.site.register(PathType, PathTypeAdmin)
admin.site.register(HAI, HAIAdmin)

