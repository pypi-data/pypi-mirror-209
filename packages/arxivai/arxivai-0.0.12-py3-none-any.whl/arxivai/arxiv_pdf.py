import json
import os
import re
from pathlib import Path

import fitz
import tiktoken
from google.cloud import storage
from langchain.text_splitter import RecursiveCharacterTextSplitter

file = os.path.join(os.path.expanduser('~'), '.config/my_settings.json')
with open(file, "r") as jsonfile:
    settings = json.load(jsonfile)
os.environ["OPENAI_API_KEY"] = settings['OPENAI_API_KEY']


def download(arxiv_id) -> Path:
    os.makedirs(Path("dataset/tmp"), exist_ok=True)
    file_name = Path(f"dataset/tmp/{arxiv_id}.pdf")
    if not os.path.exists(file_name):
        bucket_name = "arxiv-dataset"
        blob_name = f"arxiv/arxiv/pdf/{arxiv_id.split('.')[0]}/{arxiv_id}.pdf"

        storage_client = storage.Client.create_anonymous_client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(file_name)

    return file_name


def pdf_context(arxiv_id: str) -> dict:
    context = {
        'subtitles': [],
        'fulltext': [],
    }
    pdf_file = download(arxiv_id)

    with fitz.open(pdf_file) as doc:
        toc = doc.get_toc(simple=True)
        for entry in toc:
            context['subtitles'].append(entry[1])

        for page in doc:
            text = page.get_text().encode("utf-8")
            # data['fulltext'].append(extract_sentences(text.decode("utf-8")))
            context['fulltext'].append(text.decode("utf-8"))

    return context


def tiktoken_len(text: str) -> int:
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)


def text_chunks(text: str) -> list:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
        length_function=tiktoken_len,
    )
    chunks = text_splitter.split_text(text)

    return chunks


def delete(file_name: str):
    if os.path.exists(file_name):
        os.remove(file_name)


if __name__ == '__main__':
    arxiv_id = '2106.12423v4'
    data = pdf_context(arxiv_id)

    filename = Path(f"dataset/tmp/{arxiv_id}.txt")
    with open(filename, 'w', encoding='utf-8') as f:
        fulltext = re.sub(r'\n+', ' ', '\n'.join(data['fulltext']))

        content = fulltext.split(data['subtitles'][0])[1]
        for i in range(1, len(data['subtitles'])):
            try:
                split_before = fulltext.split(data['subtitles'][i])[0]
                split_after = fulltext.split(data['subtitles'][i])[1]
                if i == len(data['subtitles'])-1:
                    chunks = text_chunks(split_after)
                    for chunk in chunks:
                        f.write(f"{data['subtitles'][i]}: {chunk}\n")
                else:
                    chunks = text_chunks(split_before)
                    for chunk in chunks:
                        f.write(f"{data['subtitles'][i-1]}: {chunk}\n")
            except:
                pass
