from location import get_loc


def info1(param, js):
    """
    (str, json) -> list
    function works with a json searching for a special type of info

    param param: string that means type of info
    here is the list of all the possible parameters: "name", "screen_name",
    "location","description","followers_count", "friends_count"
    "listed_count","created_at","favourites_count", "utc_offset", "time_zone"
    "url", "status", "statuses_count", "profile_background_image_url"
    "profile_image_url", "profile_banner_url"

    param js: json with full information about user
    return: list of tuples that contain username and info of special parameter
    """

    info_list = []
    for user in js['users']:
        # next part is commented because this program
        # uses only correct parameters
        # if param not in user:
        #     print("No {} found".format(param))
        if param == "location":
            info_list.append((get_loc(user[param]), user["name"],
                              user["profile_image_url"]))
        elif param == "status":
            info_list.append((user["name"], user[param]["text"]))
        else:
            info_list.append((user["name"], user[param]))
    return info_list
