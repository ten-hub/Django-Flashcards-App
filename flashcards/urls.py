
from django.contrib import admin
from django.urls import path, include

# An empty route is added in line 9 and include() informs the 'flashcards' project that the 'cards' app will take care of all routes that match the string pattern. Since it's an empty string, 'cards' listend to all root URLs. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("cards.urls")),
]
