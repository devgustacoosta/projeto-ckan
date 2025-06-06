import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def almavivasolutions_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "almavivasolutions_get_sum": almavivasolutions_get_sum,
    }
