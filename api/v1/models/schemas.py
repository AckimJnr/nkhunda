"""
schemas module

This module contains the schemas for the API
"""

#user schema
def single_user_data(user):
    """
    Returns a dictionary of a single user
    """
    return {
        "user_id": str(user["_id"]),
        "org_id": user["org_id"],
        "app_id": user["app_id"],
        "full_name": user["full_name"],
        "created_at": int(user["created_at"]),
        "updated_at": int(user["updated_at"])
    }

def all_users_data(users):
    """
    Returns a list of dictionaries of all users
    """
    return [single_user_data(user) for user in users]

#app schema
def single_app_data(app):
    """
    Returns a dictionary of a single app
    """
    return {
        "app_id": str(app["_id"]),
        "org_id": app["org_id"],
        "users": app["users"],
        "app_name": app["app_name"],
        "app_type": app["app_type"],
        "app_description": app["app_description"],
        "groups": app["groups"],
        "created_at": int(app["created_at"]),
        "updated_at": int(app["updated_at"])
    }

def all_apps_data(apps):
    """
    Returns a list of dictionaries of all apps
    """
    return [single_app_data(app) for app in apps]

#organisation schema
def single_org_data(org):
    """
    Returns a dictionary of a single organisation
    """
    return {
        "org_id": str(org["_id"]),
        "name": org["name"],
        "apps": org["apps"],
        "created_at": int(org["created_at"]),
        "updated_at": int(org["updated_at"])
    }

def all_orgs_data(orgs):
    """
    Returns a list of dictionaries of all organisations
    """
    return [single_org_data(org) for org in orgs]