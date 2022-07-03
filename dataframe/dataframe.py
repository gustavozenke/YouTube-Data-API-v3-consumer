import pandas as pd

from typing import List
from model.video import Video


def convert_list_videos_to_dataframe(video_list: List[Video]):
    return pd.DataFrame({'title': list(map(lambda video: video.title, video_list)),
                         'publishedAt': list(map(lambda video: video.published_at, video_list)),
                         'channelId': list(map(lambda video: video.channel_id, video_list)),
                         'description': list(map(lambda video: video.description, video_list)),
                         'channelTitle': list(map(lambda video: video.channel_title, video_list)),
                         'categoryId': list(map(lambda video: video.category_id, video_list)),
                         'viewCount': list(map(lambda video: video.view_count, video_list)),
                         'likeCount': list(map(lambda video: video.like_count, video_list)),
                         'favoriteCount': list(map(lambda video: video.favorite_count, video_list)),
                         'commentCount': list(map(lambda video: video.comment_count, video_list)),
                         'duration': list(map(lambda video: video.duration, video_list)),
                         'dimension': list(map(lambda video: video.dimension, video_list)),
                         'definition': list(map(lambda video: video.definition, video_list)),
                         'caption': list(map(lambda video: video.caption, video_list)),
                         'licensed_content': list(map(lambda video: video.licensed_content, video_list))})


def salvar_dataframe_csv(dataframe, path, file_name):
    dataframe.to_csv(path+"/"+file_name+".csv", sep='\t', indevideo=False)
