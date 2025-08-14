from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationAdmin
from django.contrib.admin import ModelAdmin
from .models import OurTeam, ContactUs, Services, ServicesDetails, Portfolio, ImagesPortfolio, Blog


# --- ImagesPortfolio Inline for Portfolio ---
class ImagesPortfolioInline(admin.TabularInline):
    model = ImagesPortfolio
    extra = 1
    fields = ('image',)


# --- OurTeam ---
@admin.register(OurTeam)
class OurTeamAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'position_uz', 'image')
    search_fields = ('name', 'position_uz')
    list_filter = ('position_uz',)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # faqat _uz maydonlarini qoldiramiz
        if db_field.name.endswith('_en') or db_field.name.endswith('_ru'):
            return None
        return super().formfield_for_dbfield(db_field, request, **kwargs)


# --- ContactUs ---
@admin.register(ContactUs)
class ContactUsAdmin(TabbedTranslationAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'message_uz')
    search_fields = ('full_name', 'email')
    list_filter = ('email',)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # faqat _uz maydonlarini qoldiramiz
        if db_field.name.endswith('_en') or db_field.name.endswith('_ru'):
            return None
        return super().formfield_for_dbfield(db_field, request, **kwargs)

# --- Services ---
@admin.register(Services)
class ServicesAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'description_uz')
    search_fields = ('name',)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # faqat _uz maydonlarini qoldiramiz
        if db_field.name.endswith('_en') or db_field.name.endswith('_ru'):
            return None
        return super().formfield_for_dbfield(db_field, request, **kwargs)


# --- ServicesDetails ---
@admin.register(ServicesDetails)
class ServicesDetailsAdmin(TabbedTranslationAdmin):
    list_display = ('name_uz', 'Company_nomi', 'phone_number', 'service_type')
    search_fields = ('name_uz', 'Company_nomi')
    list_filter = ('service_type',)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # faqat _uz maydonlarini qoldiramiz
        if db_field.name.endswith('_en') or db_field.name.endswith('_ru'):
            return None
        return super().formfield_for_dbfield(db_field, request, **kwargs)


# --- Portfolio ---
@admin.register(Portfolio)
class PortfolioAdmin(TabbedTranslationAdmin):
    list_display = ('name_uz', 'proect_type', 'view_count', 'like_count')
    search_fields = ('name', 'proect_type')
    list_filter = ('proect_type',)
    inlines = [ImagesPortfolioInline]

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # faqat _uz maydonlarini qoldiramiz
        if db_field.name.endswith('_en') or db_field.name.endswith('_ru'):
            return None
        return super().formfield_for_dbfield(db_field, request, **kwargs)


# --- ImagesPortfolio ---
@admin.register(ImagesPortfolio)
class ImagesPortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio',)


# --- Blog ---
@admin.register(Blog)
class BlogAdmin(TabbedTranslationAdmin):
    list_display = ('name_uz', 'created_at')
    search_fields = ('name_uz',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # faqat _uz maydonlarini qoldiramiz
        if db_field.name.endswith('_en') or db_field.name.endswith('_ru'):
            return None
        return super().formfield_for_dbfield(db_field, request, **kwargs)
