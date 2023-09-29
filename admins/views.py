from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from users.models import User
from products.models import Product, ProductCategory
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, ProductAdminCreateForm, \
    ProductCategoryAdminCreateForm


class AdminsIndexView(TemplateView):
    template_name = 'admins/index.html'

    def get_context_data(self, **kwargs):
        context = super(AdminsIndexView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ Панель'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminsIndexView, self).dispatch(request, *args, **kwargs)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-update-delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.safe_delete()
        return HttpResponseRedirect(success_url)

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Продукты'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products')
    template_name = 'admins/admin-products-create.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Добавление продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products')
    template_name = 'admins/admin-products-update-delete.html'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('admins:admin_products')
    template_name = 'admins/admin-products-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryAdminCreateForm
    success_url = reverse_lazy('admins:admin_categories')
    template_name = 'admins/admin-categories-create.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Добавление категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryAdminCreateForm
    success_url = reverse_lazy('admins:admin_categories')
    template_name = 'admins/admin-categories-update-delete.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('admins:admin_categories')
    template_name = 'admins/admin-categories-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def index(request):
#     context = {'title': 'GeekShop - Админ Панель'}
#     return render(request, 'admins/index.html', context)


# Create
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Пользователь успешно создан')
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'GeekShop - Создание пользователя', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


# Read
# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {
#         'title': 'GeekShop - Пользователи',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)


# Update
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Данные пользователя {selected_user.username} успешно обновлены')
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#
#     context = {
#         'title': 'GeekShop - Обновление пользователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


# Delete
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.safe_delete()
#     return HttpResponseRedirect(reverse('admins:admin_users'))


# Create product
# @user_passes_test(lambda u: u.is_staff)
# def admin_products_create(request):
#     if request.method == 'POST':
#         form = ProductAdminCreateForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Продукт успешно добавлен')
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductAdminCreateForm()
#     context = {'title': 'GeekShop - Добавление продукта', 'form': form}
#     return render(request, 'admins/admin-products-create.html', context)


# Read products
# @user_passes_test(lambda u: u.is_staff)
# def admin_products(request):
#     context = {
#         'title': 'GeekShop - Продукты',
#         'products': Product.objects.all(),
#     }
#     return render(request, 'admins/admin-products-read.html', context)


# Update product
# @user_passes_test(lambda u: u.is_staff)
# def admin_products_update(request, id):
#     selected_product = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductAdminCreateForm(instance=selected_product, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Данные продукта {selected_product.name} успешно обновлены')
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductAdminCreateForm(instance=selected_product)
#
#     context = {
#         'title': 'GeekShop - Редактирование продукта',
#         'form': form,
#         'selected_product': selected_product,
#     }
#     return render(request, 'admins/admin-products-update-delete.html', context)


# Delete product
# @user_passes_test(lambda u: u.is_staff)
# def admin_products_delete(request, id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return HttpResponseRedirect(reverse('admins:admin_products'))


# Create category
# @user_passes_test(lambda u: u.is_staff)
# def admin_categories_create(request):
#     if request.method == 'POST':
#         form = ProductCategoryAdminCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Категория успешно добавлена')
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = ProductCategoryAdminCreateForm()
#     context = {'title': 'GeekShop - Добавление категории', 'form': form}
#     return render(request, 'admins/admin-categories-create.html', context)


# Read categories
# @user_passes_test(lambda u: u.is_staff)
# def admin_categories(request):
#     context = {
#         'title': 'GeekShop - Категории',
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'admins/admin-categories-read.html', context)


# Update category
# @user_passes_test(lambda u: u.is_staff)
# def admin_categories_update(request, id):
#     selected_category = ProductCategory.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductCategoryAdminCreateForm(instance=selected_category, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Данные категории {selected_category.name} успешно обновлены')
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = ProductCategoryAdminCreateForm(instance=selected_category)
#
#     context = {
#         'title': 'GeekShop - Редактирование категории',
#         'form': form,
#         'selected_category': selected_category,
#     }
#     return render(request, 'admins/admin-categories-update-delete.html', context)


# Delete category
# @user_passes_test(lambda u: u.is_staff)
# def admin_categories_delete(request, id):
#     category = ProductCategory.objects.get(id=id)
#     category.delete()
#     return HttpResponseRedirect(reverse('admins:admin_categories'))
