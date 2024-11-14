from langchain_community.document_loaders import YoutubeLoader


loader=YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=5qtC-tsQ-wE&t=321s", add_video_info=False, language=["en"], translation="en")

data=loader.load()

print(data)