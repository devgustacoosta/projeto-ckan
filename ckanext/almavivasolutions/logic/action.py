import ckan.plugins.toolkit as tk
import ckanext.almavivasolutions.logic.schema as schema


@tk.side_effect_free
def almavivasolutions_get_sum(context, data_dict):
    tk.check_access(
        "almavivasolutions_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.almavivasolutions_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'almavivasolutions_get_sum': almavivasolutions_get_sum,
    }
