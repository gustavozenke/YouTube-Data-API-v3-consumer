import isodate


class Video:

    def __init__(self, snippet_informations, statistics_information, content_details_information):
        self.title = snippet_informations['title']
        self.published_at = snippet_informations['publishedAt']
        self.channel_id = snippet_informations['channelId']
        self.description = snippet_informations['description']
        self.channel_title = snippet_informations['channelTitle']
        self.category_id = snippet_informations['categoryId']

        self.view_count = statistics_information['viewCount']
        self.like_count = statistics_information['likeCount']
        self.favorite_count = statistics_information['favoriteCount']
        self.comment_count = statistics_information['commentCount']

        self.duration = isodate.parse_duration(content_details_information['duration'])
        self.dimension = content_details_information['dimension']
        self.definition = content_details_information['definition']
        self.caption = content_details_information['caption']
        self.licensed_content = content_details_information['licensedContent']
