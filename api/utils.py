

# def all_videos(videos):
#     my_videos = [{
#         "id": video.id, 
#         "title": video.title,
#         "video_link": video.video_link,
#         "category": video.category.name,
#         "age_rating": video.rating,
#         "desktop_thumbnail": video.desktop_thumbnail.url,
#         "desktop_banner": video.desktop_banner.url,
#         "mobile_thumbnail": video.mobile_thumbnail.url,
#         "mobile_banner": video.mobile_banner.url,
#         "genres": video.genres,
#         "mood": video.mood,
#         "actors": video.actors,
#         "likes": video.likes,  
#         "category": video._category,
#         "date_uploaded": video.date_uploaded,
#         "last_modified": video.last_modified,
#         "published": video.published
#     } for video in videos]

#     return my_videos


# def all_videos(videos):
#     my_videos = [{
#         "id": video.id, 
#         "title": video.title,
#         "description": video.description,
#         "video_link": video.video_link,
#         "category": video.category.name,
#         "_category": {
#             "id": video.category.id,
#             "name": video.category.name
#         },
#         "director": {
#             "name":video._director.name,
            
#         },
#         "playlist": video.playlist.title,
#         "more_like_this": video.more_like_this,
#         "age_rating": video.rating,
#         "rating": video.rating,
#         "desktop_thumbnail": video.desktop_thumbnail.url,
#         "desktop_banner": video.desktop_banner.url,
#         "mobile_thumbnail": video.mobile_thumbnail.url,
#         "mobile_banner": video.mobile_banner.url,
#         "genres": video.genres,
#         "mood": video.mood,
#         "actors": video.actors,
#         "likes": video.likes,
#         "category": video._category,
#         "has_manual_views": video.has_manual_views,
#         "date_uploaded": video.date_uploaded,
#         "last_modified": video.last_modified,
#         "manual_views": video.manual_views,
#         "release_date": video.release_date,
#         "published": video.published
#     } for video in videos]

#     return my_videos

def all_videos(videos):
    my_videos = [{
        "id": video.id, 
        "title": video.title,
        "description": video.description,
        "director": {
            "id": video._director.id,
            "name":video._director.name,
            "bio": video._director.bio,
            "image": video._director.image.url
        },
        "video_link": video.video_link,
        "category": video.category.name,
        "age_rating": video.rating,
        "desktop_thumbnail": video.desktop_thumbnail.url,
        "desktop_banner": video.desktop_banner.url,
        "mobile_thumbnail": video.mobile_thumbnail.url,
        "mobile_banner": video.mobile_banner.url,
        "genres": video.genres,
        "mood": video.mood,
        "actors": video.actors,
        "likes": video.likes,  
        "category": video._category,
        "date_uploaded": video.date_uploaded,
        "last_modified": video.last_modified,
        "published": video.published,
        "more_like_this": video.more_like_this
    } for video in videos]

    return my_videos

