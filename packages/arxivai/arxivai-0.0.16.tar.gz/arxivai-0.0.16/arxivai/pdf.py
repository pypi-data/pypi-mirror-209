import os
from pathlib import Path

import fitz
from google.cloud import storage


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


def context(file_name) -> dict:
    context = {
        'subtitles': [],
        'fulltext': [],
    }

    with fitz.open(file_name) as doc:
        toc = doc.get_toc(simple=False)
        if len(toc) == 0:
            context['subtitles'].append('Table of Contents not found.')
        else:
            for entry in toc:
                context['subtitles'].append(entry[1])

        for page in doc:
            text = page.get_text().encode("utf-8")
            context['fulltext'].append(text.decode("utf-8"))

    return context


def remove(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
