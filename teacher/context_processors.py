# from case.models import Case
# from client.models import Client
# from task.models import Task
from .forms import SearchForm


def search(request):
    form = SearchForm(request.GET)
    search_results = []

    if form.is_valid():
        search_query = form.cleaned_data["search_query"]
        search_category = form.cleaned_data["search_category"]

        # if search_category == "cases":
        #     search_results = Case.objects.filter(title__icontains=search_query)
        # elif search_category == "tasks":
        #     search_results = Task.objects.filter(title__icontains=search_query)
        # elif search_category == "clients":
        #     search_results = Client.objects.filter(first_name__icontains=search_query)

    return {"form": form, "search_results": search_results}
