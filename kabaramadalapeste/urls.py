from django.urls import path

from .views import (
    game, game2, exchange, island, IslandInfoView, MoveToIslandView,
    SetStartIslandView, PutAnchorView
)


urlpatterns = [
    path('island_info/<int:island_id>',
         IslandInfoView.as_view(), name="island_info"),
    path('set_start_island/<int:dest_island_id>',
         SetStartIslandView.as_view(), name="set_start_island"),
    path('move_to/<int:dest_island_id>',
         MoveToIslandView.as_view(), name="move_to"),
    path('put_anchor', PutAnchorView.as_view(), name="put_anchor"),
    path('', game, name="game"),
    path('low/', game2, name="game2"),
    path('exchange/', exchange, name="exchange"),
    path('island/', island, name="island"),
]
