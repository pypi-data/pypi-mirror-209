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


# if __name__ == '__main__':
#     file = os.path.join(os.path.expanduser('~'), '.config/my_settings.json')
#     with open(file, "r") as jsonfile:
#         settings = json.load(jsonfile)
#     os.environ["OPENAI_API_KEY"] = settings['OPENAI_API_KEY']

#     arxiv_id = '2303.11032v1'  # No TOC

#     context = context(arxiv_id)
#     print(context['subtitles'])
#     print('-------------------')

#     filename = Path(f"dataset/tmp/{arxiv_id}.txt")
#     with open(filename, 'w', encoding='utf-8') as f:
#         fulltext = re.sub(r'\n+', ' ', '\n'.join(context['fulltext']))

#         content = fulltext.split(context['subtitles'][0])[1]
#         for i in range(1, len(context['subtitles'])):
#             try:
#                 split_before = fulltext.split(context['subtitles'][i])[0]
#                 split_after = fulltext.split(context['subtitles'][i])[1]
#                 if i == len(context['subtitles'])-1:
#                     chunks = text_chunks(split_after)
#                     for chunk in chunks:
#                         f.write(f"{context['subtitles'][i]}: {chunk}\n")
#                 else:
#                     chunks = text_chunks(split_before)
#                     for chunk in chunks:
#                         f.write(f"{context['subtitles'][i-1]}: {chunk}\n")
#             except:
#                 pass
