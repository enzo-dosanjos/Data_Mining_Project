import folium
from folium.plugins import MarkerCluster

m = folium.Map(location=(45.754858, 4.821710))

def add_point_all_info(carte, photo_id, user_id, lat, long, tags, title, dateTmi, dateTh, dateTd, dateTmo, dateTy, dateUmi, dateUh, dateUd, dateUmo, dateUy):
    folium.Marker(
        location=[lat, long],
        tooltip=title,
        popup=f"""
            ID:{photo_id}<br>
            User ID:{user_id}<br>
            Name:{title}<br>
            Tags:{tags}<br>
            Taken:{dateTd:.0f}/{dateTmo:.0f}/{dateTy:.0f} at {dateTh:.0f}:{dateTmi:.0f}<br>
            Uploaded:{dateUd:.0f}/{dateUmo:.0f}/{dateUy:.0f} at {dateUh:.0f}:{dateUmi:.0f}<br>""",
        icon=folium.Icon(color="red"),
    ).add_to(carte)

def add_point_to_group(group, color_group, photo_id, user_id, lat, long, tags, title, dateTmi, dateTh, dateTd, dateTmo, dateTy, dateUmi, dateUh, dateUd, dateUmo, dateUy):
    folium.Marker(
        location=[lat, long],
        tooltip=title,
        popup=f"ID:{photo_id}"
              f"User ID:{user_id}"
              f"Name:{title}"
              f"Tags:{tags}"
              f"Taken:{dateTd}/{dateTmo}/{dateTy} at {dateTh}:{dateTmi}"
              f"Uploaded:{dateUd}/{dateUmo}/{dateUy} at {dateUh}:{dateUmi}",
        icon=folium.Icon(color=color_group),
    ).add_to(group)

group_1 = folium.FeatureGroup("first group").add_to(m)
group_2 = folium.FeatureGroup("second group").add_to(m)
folium.LayerControl().add_to(m)

def add_dataframe_without_cluster(carte, dataframe):
    for _, row in dataframe.iterrows():
        add_point_all_info(carte, row["id"], row["user"], row["lat"], row["long"], row["tags"], row["title"], row["date_taken_minute"], row["date_taken_hour"], row["date_taken_day"], row["date_taken_month"], row["date_taken_year"], row["date_upload_minute"], row["date_upload_hour"], row["date_upload_day"], row["date_upload_month"], row["date_upload_year"])

#marker_cluster = MarkerCluster().add_to(m)
#add_dataframe_without_cluster(marker_cluster, df_modified.head(50000))

m.save("index_t.html")

def add_dataframe_with_cluster():
    print("da")


m.save("index.html")


"""
from folium.plugins import HeatMap

m2 = folium.Map(location=(45.754858, 4.821710))

data_HMap = df_modified[["lat","long"]].values.tolist()
HeatMap(data_HMap).add_to(m2)

m2.save("HMap.html")

m2
"""


"""
from folium.plugins import HeatMapWithTime
m3 = folium.Map(location=(45.754858, 4.821710))

data_HMapWTime = [
    df_annee[["lat", "long"]].values.tolist()
    for _, df_annee in df_modified.sort_values("date_taken_year").groupby("date_taken_year")
]
annees = [
    str(annee)
    for annee in sorted(df_modified["date_taken_year"].unique())
]

HeatMapWithTime(
    data_HMapWTime,
    index=annees,
    radius=15,
    auto_play=False,
    max_opacity=0.8
).add_to(m3)

m3.save("HMapWTime.html")

m3
"""

"""
#Ancienne version
m3 = folium.Map(location=(45.754858, 4.821710))

data_HMapWTime = [[]]
for _, row in df_modified.iterrows():
    myrow = [row["lat"], row["long"], row["date_taken_month"] + 100* row["date_taken_year"]]
    list.append(data_HMapWTime, myrow)

hm = folium.plugins.HeatMapWithTime(data_HMapWTime)
hm.add_to(m3)

m3.save("HMapWTime.html")

m3
"""