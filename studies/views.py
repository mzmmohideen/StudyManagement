from django.shortcuts import render

def main_view_page(request):
    """Renders the Main View Page template."""
    return render(request, 'studies/main_view_page.html')

def add_study_page(request):
    """Renders the Add Study Page template."""
    return render(request, 'studies/add_study_page.html')

def edit_study_page(request, pk):
    """Renders the Edit Study Page template."""
    context = {'study_id': pk}
    return render(request, 'studies/edit_study_page.html', context)

def view_study_page(request, pk):
    """Renders the View Study Details Page template."""
    context = {'study_id': pk}
    return render(request, 'studies/view_study_page.html', context)