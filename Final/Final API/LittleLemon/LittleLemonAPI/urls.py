
from django.urls import path
from .views import (
    CategoryView,
    MenuItemView,
    SingleMenuItemView,
    GroupUsersView,
    FeaturedMenuItemView,
    CartView,
    OrderView,
    SingleOrderView,
)

urlpatterns = [
    path("categories/", CategoryView.as_view(), name="categories"),

    path("menu-items/", MenuItemView.as_view(), name="menu-items"),
    path(
        "menu-items/<int:pk>/",
        SingleMenuItemView.as_view(),
        name="single-menu-item"
    ),

    path(
        "groups/<str:group_name>/users",
        GroupUsersView.as_view(),
        name="group-users"
    ),

    path(
        "featured-items/",
        FeaturedMenuItemView.as_view(),
        name="featured-items"
    ),

    path("cart/menu-items/", CartView.as_view(), name="cart"),

    path("orders/", OrderView.as_view(), name="orders"),
    path(
        "orders/<int:order_id>/",
        SingleOrderView.as_view(),
        name="single-order"
    ),
]
