import folium
from params import info1
from twitter2 import make_js
from folium.plugins import MarkerCluster


def cr_map(acct):
    """
    function creates a web map where the locations
    of the users are presented
    :param acct: twitter username that is entered by user
    :return: html code with web map
    """
    map = folium.Map(location=[20, -3], zoom_start=2.52)
    marker_cluster = MarkerCluster().add_to(map)

    fg = folium.FeatureGroup(name="​Twitter")
    # get json
    js = make_js(acct)
    data = info1("location", js)

    for i in data:
        if not i[0]:
            continue
        icon_user = folium.features.CustomIcon(i[2], icon_size=(40, 40))
        folium.Marker(location=i[0], popup=str(i[1]), icon=icon_user).add_to(
            marker_cluster)

    map.add_child(folium.LayerControl())
    return map.save("/home/yarka/PycharmProjects/lab2(twitter)"
                    "/templates/rybka_twitter3.html")
