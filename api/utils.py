

def all_videos(videos):
    my_videos = [{
        "id": video.id, 
        "title": video.title,
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
        "published": video.published
    } for video in videos]

    return my_videos

