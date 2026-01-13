import folium

m = folium.Map(location=(45.754858, 4.821710))

def add_point_all_info(map, id, user_id, lat, long, tags, title, dateTmi, dateTh, dateTd, dateTmo, dateTy, dateUmi, dateUh, dateUd, dateUmo, dateUy):
    folium.Marker(
        location=[lat, long],
        tooltip=title,
        popup=f"""ID:{id}<br>
            User ID:{user_id}<br>
            Name:{title}<br>
            Tags:{tags}<br>
            Taken:{dateTd:.0f}/{dateTmo:.0f}/{dateTy:.0f} at {dateTh:.0f}:{dateTmi:.0f}<br>
            Uploaded:{dateUd:.0f}/{dateUmo:.0f}/{dateUy:.0f} at {dateUh:.0f}:{dateUmi:.0f}<br>""",
        icon=folium.Icon(color="red"),
    ).add_to(map)

def add_point_to_group(group, color_group, id, user_id, lat, long, tags, title, dateTmi, dateTh, dateTd, dateTmo, dateTy, dateUmi, dateUh, dateUd, dateUmo, dateUy):
    folium.Marker(
        location=[lat, long],
        tooltip=title,
        popup=f"ID:{id}"
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

def add_dataframe_without_cluster(map, dataframe):
    for _, row in dataframe.iterrows():
        add_point_all_info(map, row["lat"], row["long"], row["tags"], row["title"], row["date_taken_minute"], row["date_taken_hour"], row["date_taken_day"], row["date_taken_month"], row["date_taken_year"], row["date_upload_minute"], row["date_upload_hour"], row["date_upload_day"], row["date_upload_month"], row["date_upload_year"])


def add_dataframe_with_cluster():
    print("da")


m.save("index.html")