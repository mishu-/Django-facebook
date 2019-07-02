"""
URL patterns for the views included in ``django.contrib.auth``.

Including these URLs (via the ``include()`` directive) will set up the
following patterns based at whatever URL prefix they are included
under:

* User login at ``login/``.

* User logout at ``logout/``.

* The two-step password change at ``password/change/`` and
  ``password/change/done/``.

* The four-step password reset at ``password/reset/``,
  ``password/reset/confirm/``, ``password/reset/complete/`` and
  ``password/reset/done/``.

The default registration backend already has an ``include()`` for
these URLs, so under the default setup it is not necessary to manually
include these views. Other backends may or may not include them;
consult a specific backend's documentation for details.

"""

from django.conf.urls import url
from django.contrib.auth.views import *
from django_facebook import registration_views
from django_facebook.utils import replication_safe

urlpatterns = [
    url(
        r'^login/$',
        replication_safe(LoginView.as_view(template_name='users/login.html')),
        name='auth_login'
    ),
    url(
        r'^logout/$',
        replication_safe(LogoutView.as_view(template_name='users/logout.html')),
        name='auth_logout'
    ),
    url(
        r'^password/change/$',
        PasswordChangeView.as_view(),
        name='auth_password_change'
    ),
    url(
        r'^password/change/done/$',
        PasswordChangeDoneView.as_view(),
        name='auth_password_change_done'
    ),
    url(
        r'^password/reset/$',
        PasswordResetView.as_view(),
        name='auth_password_reset'
    ),
    url(
        r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(),
        name='auth_password_reset_confirm'
    ),
    url(
        r'^password/reset/complete/$',
        PasswordResetCompleteView.as_view(),
        name='auth_password_reset_complete'
    ),
    url(
        r'^password/reset/done/$',
        PasswordResetDoneView.as_view(),
        name='auth_password_reset_done'
    ),
    url(
        r'^register/$',
        registration_views.register,
        name='registration_register'
    ),
]
