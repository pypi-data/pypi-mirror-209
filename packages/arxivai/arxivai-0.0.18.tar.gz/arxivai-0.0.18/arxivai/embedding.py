import openai
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter


def token_len(text: str) -> int:
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)


def chunks(text: str) -> list:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
        length_function=token_len,
    )
    chunks = text_splitter.split_text(text)

    return chunks


def encode(chunks: list) -> list:
    embeddings = []
    for chunk in chunks:
        response = openai.Embedding.create(
            input=chunk,
            model="text-embedding-ada-002",
        )
        embedding = response['data'][0]['embedding']
        embeddings.append(embedding)

    return embeddings
