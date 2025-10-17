import requests
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from django.http import JsonResponse
from datetime import datetime, timezone

def me_view(request):
    try:
        # Fetch random cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=10)
        data = response.json()
        cat_fact = data.get("fact", "Cats are mysterious creatures!")
    except Exception:
        cat_fact = "Could not fetch cat fact at the moment."

    # Build response
    return JsonResponse({
        "status": "success",
        "user": {
            "email": "michealadefehinti09@gmail.com",
            "name": "Michael Adefehinti",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    })
