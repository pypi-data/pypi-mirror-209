import os
from pathlib import Path

import fitz
from google.cloud import storage
import re


def download(arxiv_id):
    os.makedirs(Path("dataset/tmp"), exist_ok=True)
    file_name = Path(f"dataset/tmp/{arxiv_id}.pdf")
    if not os.path.exists(file_name):
        bucket_name = "arxiv-dataset"
        blob_name = f"arxiv/arxiv/pdf/{arxiv_id.split('.')[0]}/{arxiv_id}.pdf"

        storage_client = storage.Client.create_anonymous_client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(file_name)

        print(
            f"Downloaded {arxiv_id}.pdf from gs://{bucket_name}:{blob_name} successfully.")


def context(arxiv_id) -> dict:
    file_name = Path(f"dataset/tmp/{arxiv_id}.pdf")

    context = {
        'paper_id': arxiv_id,
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


def remove(arxiv_id: str):
    file_name = Path(f"dataset/tmp/{arxiv_id}.pdf")

    if os.path.exists(file_name):
        os.remove(file_name)

        print(f"Removed {arxiv_id}.pdf successfully.")
