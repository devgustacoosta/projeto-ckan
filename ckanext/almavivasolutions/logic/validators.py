import ckan.plugins.toolkit as tk


def almavivasolutions_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "almavivasolutions_required": almavivasolutions_required,
    }
