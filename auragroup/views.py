from django.views.generic import TemplateView, ListView, DetailView
from .models import OurTeam, ContactUs, Services, ServicesDetails, Portfolio, Blog
from .forms import ContactForm
from .bot import send_message
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ServicesDetailsForm
from .bot import send_service_request
from django.views.generic import DetailView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Portfolio
from django.db.models import F



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['advantages'] = Advantage.objects.all()
        context['services'] = Services.objects.all()
        context['team_members'] = OurTeam.objects.all()[:3]
        return context
    
class AboutView(ListView):
    model = OurTeam
    template_name = 'about.html'
    context_object_name = 'our_team'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        context['management'] = OurTeam.objects.all()
        return context
    

class ServicesView(ListView):
    model = Services
    template_name = 'services.html'
    context_object_name = 'services'


class ServicesDetailsView(ListView):
    model = ServicesDetails
    template_name = 'services_details.html'
    context_object_name = 'services_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        context['form'] = ServicesDetailsForm()
        return context


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog_posts'
    paginate_by = 6


class BlogDetailsView(DetailView):
    model = Blog
    template_name = 'blog_details.html'
    context_object_name = 'post'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ProjectView(ListView):
    model = Portfolio
    template_name = 'project.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Portfolio.objects.values_list('proect_type', flat=True).distinct()
        return context


class ProjectDetailsView(DetailView):
    model = Portfolio
    template_name = 'project_details.html'
    context_object_name = 'project'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        viewed = request.session.get('viewed_projects', [])  
        proj_id = str(self.object.pk)

        if proj_id not in viewed:
            Portfolio.objects.filter(pk=self.object.pk).update(view_count=F('view_count') + 1)
            self.object.refresh_from_db()
            viewed.append(proj_id)
            request.session['viewed_projects'] = viewed

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class LikeProjectView(DetailView):
    model = Portfolio
    template_name = 'project_details.html'
    context_object_name = 'project'

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Portfolio, pk=self.kwargs['pk'])
        session_key = f'liked_project_{project.id}'
        is_liked = request.session.get(session_key, False)

        if not is_liked:
            project.like_count += 1
            request.session[session_key] = True
            liked = True
        else:
            project.like_count = max(0, project.like_count - 1)
            request.session[session_key] = False
            liked = False

        project.save()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'like_count': project.like_count,
                'liked': liked
            })
        return self.get(request, *args, **kwargs)
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            send_message(
                name=instance.full_name,
                email=instance.email,
                phone_number=instance.phone_number,
                description=instance.message
            )
            messages.success(request, "Xabaringiz yuborildi!")
            return redirect('contact')
        else:
            messages.error(request, "Formani to‘g‘ri to‘ldiring!")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def service_request_view(request):
    if request.method == "POST":
        form = ServicesDetailsForm(request.POST)
        if form.is_valid():
            instance = form.save()

            send_service_request(
                company=instance.Company_nomi,
                phone=instance.phone_number,
                service=instance.service_type.name,
                contact_name=instance.name,
                description=instance.description
            )
            messages.success(request, "Xizmat so'rovingiz yuborildi!")
            return redirect('services')
        else:
            messages.error(request, "Iltimos, formani to‘g‘ri to‘ldiring")
    else:
        form = ServicesDetailsForm()
    services = Services.objects.all()
    return render(request, 'services_details.html', {"form": form, "services": services})


