from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def college_head_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='college-head-login'):
    '''
    Decorator for views that checks that the logged in user is a college head,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_college_head,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
