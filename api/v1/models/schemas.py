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