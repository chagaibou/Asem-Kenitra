from django.contrib import admin
from backend_frontend import models
# Register your models here.

class CategorieEvenementAdmin(admin.ModelAdmin):
    pass

class EvenementAdmin(admin.ModelAdmin):
    pass

class CategoriePostAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.CategorieEvenement,CategorieEvenementAdmin)
admin.site.register(models.Evenement,EvenementAdmin)
admin.site.register(models.CategoriePost,CategoriePostAdmin)
admin.site.register(models.Post,PostAdmin)