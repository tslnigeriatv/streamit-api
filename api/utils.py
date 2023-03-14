

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
        # Added new attributes here...
        "published": video.published,
        "manual_views": video.manual_views,
        "has_manual_views": video.has_manual_views,
        "release_date": video.release_date,
        
    } for video in videos]

    return my_videos

