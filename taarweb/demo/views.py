from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render

from taar.recommenders import RecommendationManager
from .forms import AddonRecommendationsForm


@login_required
def get_client_recommendations(request):
    form = AddonRecommendationsForm()
    recommendations = []
    if request.method == 'POST':
        form = AddonRecommendationsForm(data=request.POST)
        if form.is_valid():
            # Use addon recommender.
            value = form.cleaned_data['client_id']
            num_items = form.cleaned_data['num_items']
            recommendation_manager = RecommendationManager()
            recommendations = recommendation_manager.recommend(value,
                                                               num_items)
    context = {
        'form': form,
        'recommendations': recommendations
    }

    return render(request, template_name="taar/index.html", context=context)
