from django.http import JsonResponse
from django.shortcuts import render


def get_sales():
    """Stand-in for a database query, e.g. list(Sale.objects.values("month", "total"))."""
    return [
        {"month": "July", "total": 1200, "note": "Launch"},
        {"month": "August", "total": 1750, "note": "Promo </script> & \"quotes\" are safe"},
        {"month": "September", "total": 1490, "note": ""},
    ]


def index(request):
    sales = get_sales()
    context = {
        # Plain Python objects. Do NOT call json.dumps() here:
        # the template turns them into JSON with the json_script filter.
        "sales": sales,
        "settings_for_js": {"currency": "ZAR", "show_notes": True},
    }
    return render(request, "dashboard/index.html", context)


def sales_api(request):
    """Method 3: return JSON from its own URL and load it with fetch()."""
    # safe=False is required because the top-level object is a list, not a dict.
    return JsonResponse(get_sales(), safe=False)
