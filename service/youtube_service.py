from googleapiclient.discovery import build
from model.video import Video


class YoutubeService:

    def __init__(self, api_key):
        self.youtube = build(serviceName='youtube', version='v3', developerKey=api_key)

    def obter_id_videos_playlist(self, playlist_id):
        page_token = None
        playlist_videos = []
        while True:
            response = self.youtube.playlistItems().list(part='snippet',
                                                         playlistId=playlist_id,
                                                         maxResults=50,
                                                         pageToken=page_token).execute()
            playlist_videos += response['items']
            if not response.get('nextPageToken'):
                break

        return list(map(lambda x: x['snippet']['resourceId']['videoId'], playlist_videos))

    def obter_dados_video(self, id_video_list):
        video_list = []
        for id_video in id_video_list:
            snippet = self.youtube.videos().list(part='snippet', id=id_video).execute()
            content_details = self.youtube.videos().list(part='contentDetails', id=id_video).execute()
            statistics = self.youtube.videos().list(part='statistics', id=id_video).execute()

            if snippet['items'] and content_details['items'] and statistics['items']:
                video_list.append(Video(snippet['items'][0]['snippet'],
                                        statistics['items'][0]['statistics'],
                                        content_details['items'][0]['contentDetails']))
        return video_list
