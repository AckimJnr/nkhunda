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

#message schema

def single_message_data(message):
    """
    retuns a single message
    """
    return {
        # "message_id": str(message["_id"]),
        "app_id": message["app_id"],
        "message_type": message["message_type"],
        "group_id": message["group_id"],
        "status": message["status"],
        "message_content": message["message_content"],
        "sender_id": message["sender_id"],
        "recipient_id": message["recipient_id"],
        "created_at": int(message["created_at"]),
        "updated_at": int(message["updated_at"])
    }

def all_messages_data(messages):
    """
    Returns a list of dictionaries of all messages
    """
    return [single_message_data(message.dict()) for message in messages]

#group schema
def single_group_data(group):
    """
    Returns a dictionary of a single group
    """
    return {
        "group_id": str(group["_id"]),
        "app_id": group["app_id"],
        "creator": group["creator"],
        "group_name": group["group_name"],
        "members": group["members"],
        "created_at": int(group["created_at"]),
        "updated_at": int(group["updated_at"])
    }

def all_groups_data(groups):
    """
    Returns a list of dictionaries of all groups
    """
    return [single_group_data(group) for group in groups]

#api_key schema
def single_api_key_data(api_key):
    """
    Returns a dictionary of a single api_key
    """
    return {
        "app_id": api_key["app_id"],
        "api_key": api_key["api_key"],
        "created_at": int(api_key["created_at"]),
        "updated_at": int(api_key["updated_at"]),
        "active": api_key["active"]
    }

def all_api_keys_data(api_keys):
    """
    Returns a list of dictionaries of all api_keys
    """
    return [single_api_key_data(api_key) for api_key in api_keys]