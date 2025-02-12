from langchain.document_loaders import youtube
import io
url = "https://www.youtube.com/watch?v=6fM70wVT0zg"
loader = youtube.YoutubeLoader.from_youtube_url(url)
docs = loader.load()


with io.open(file="youtube_transcript.txt",mode="w",encoding="utf-8") as file:
    file.write(docs[0].page_content)
    file.close()