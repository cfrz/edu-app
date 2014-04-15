from django.contrib import admin

from .models import Article, Pathogen, Iso, Prevention, HAI, PathType

class PathogenAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)}
    class Meta:
        model = Pathogen
        
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Article
        
class IsoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)}
    class Meta:
        model = Iso
        
class PreventionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)}
    class Meta:
        model = Prevention
        
class HAIAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)}
    class Meta:
        model = HAI
        
class PathTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)}
    class Meta:
        model = PathType
        

admin.site.register(Prevention, PreventionAdmin)
admin.site.register(Pathogen, PathogenAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Iso, IsoAdmin)
admin.site.register(PathType, PathTypeAdmin)
admin.site.register(HAI, HAIAdmin)

