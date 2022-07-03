from googleapiclient.errors import HttpError
from dataframe.dataframe import salvar_dataframe_csv, convert_list_videos_to_dataframe
from service.youtube_service import YoutubeService


def main():
    api_key = ''  # Insira a apiKey para consumo da API aqui
    palylist_id = ''  # Insira o id da playlist aqui
    path = ''  # insira o caminho onde o CSV será salvo
    archive_name = ''  # Insira o nome do arquivo CSV

    youtube_service = YoutubeService(api_key)
    id_videos_playlist = youtube_service.obter_id_videos_playlist(palylist_id)
    list_videos = youtube_service.obter_dados_video(id_videos_playlist)

    salvar_dataframe_csv(convert_list_videos_to_dataframe(list_videos), path, archive_name)


if __name__ == '__main__':
    try:
        main()
    except HttpError as e:
        print('Erro HTTP %d ocorreu:\n%s' % (e.resp.status, e.reason))
    except Exception as e:
        print(f'{str(e)}')
