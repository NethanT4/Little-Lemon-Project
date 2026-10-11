from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny, IsAdminUser, IsAuthenticated
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied

from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer, MenuItemSerializer,
    CartSerializer, OrderSerializer
)

class IsManager(IsAuthenticated):
    def has_permission(self, request, view):
        return (
            super().has_permission(request, view)
            and request.user.groups.filter(name="Manager").exists()
        )

class IsDeliveryCrew(IsAuthenticated):
    def has_permission(self, request, view):
        return (
            super().has_permission(request, view)
            and request.user.groups.filter(name="Delivery crew").exists()
        )

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related("category").all()
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category_id=category)

        ordering = self.request.query_params.get("ordering")
        if ordering in ["price", "-price"]:
            queryset = queryset.order_by(ordering)

        return queryset

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method in ["PUT","PATCH","DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]

class GroupUsersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, group_name):
        group = get_object_or_404(Group, name=group_name)
        users = group.user_set.all().values("id","username")
        return Response(list(users))

    def post(self, request, group_name):
        username = request.data.get("username")
        if not username:
            return Response(
                {"error": "username is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = get_object_or_404(User, username=username)
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        return Response(
            {"message" : f"{username} added to {group_name} group"}
        )

    def delete(self, request, group_name):
        username = request.data.get("username")
        user = get_object_or_404(User, username=username)
        group = get_object_or_404(Group, name=group_name)
        user.groups.remove(group)
        return Response(status=status.HTTP_200_OK)

class FeaturedMenuItemView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        return MenuItem.objects.filter(featured = True)

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Cart.objects.filter(user=request.user)
        return Response(CartSerializer(items, many=True).data)

    def post(self, request):
        menuitem_id = request.data.get("menuitem")
        quantity = int(request.data.get("quantity", 1))

        if quantity < 1:
            return Response(
                {"error": "Quantity must be positive"},
                status=status.HTTP_400_BAD_REQUEST
            )

        menuitem = get_object_or_404(MenuItem, id=menuitem_id)
        cart, created = Cart.objects.get_or_create(
            user=request.user,
            menuitem=menuitem,
            defaults={
                "quantity": quantity,
                "unit_price": menuitem.price,
                "price": menuitem.price * quantity
            }
        )

        if not created:
            cart.quantity += quantity
            cart.price = cart.unit_price * cart.quantity
            cart.save()

        return Response(CartSerializer(cart).data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request):
        Cart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.groups.filter(name="Manager").exists():
            orders = Order.objects.all()
        elif request.user.groups.filter(name="Delivery crew").exists():
            orders = Order.objects.filter(delivery_crew=request.user)
        else:
            orders = Order.objects.filter(user=request.user)

        return Response(OrderSerializer(orders, many=True).data)

    def post(self, request):
        cart_items = Cart.objects.filter(user=request.user)

        if not cart_items.exists():
            return Response(
                {"error": "Your cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        total = sum(item.price for item in cart_items)
        order = Order.objects.create(user=request.user, total=total)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                menuitem=item.menuitem,
                quantity=item.quantity,
                unit_price=item.unit_price,
                price=item.price
            )

        cart_items.delete()
        return Response(
            OrderSerializer(order).data,
            status=status.HTTP_201_CREATED
        )


class SingleOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)

        if request.user.groups.filter(name="Manager").exists():
            if "delivery_crew" in request.data:
                crew_id = request.data["delivery_crew"]
                order.delivery_crew = get_object_or_404(
                    User, id=crew_id
                )
            if "status" in request.data:
                order.status = request.data["status"]
            order.save()
            return Response(OrderSerializer(order).data)

        if request.user.groups.filter(name="Delivery crew").exists():
            if order.delivery_crew_id != request.user.id:
                raise PermissionDenied(
                    "This order is not assigned to you"
                )
            if "status" in request.data:
                order.status = request.data["status"]
                order.save()
                return Response(OrderSerializer(order).data)

        raise PermissionDenied("You cannot update this order")

    def delete(self, request, order_id):
        if not request.user.groups.filter(name="Manager").exists():
            raise PermissionDenied("Managers only")

        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


       