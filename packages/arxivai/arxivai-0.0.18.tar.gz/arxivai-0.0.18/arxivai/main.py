import pdf
import embedding
import os
import json
import openai

if __name__ == '__main__':
    file = os.path.join(os.path.expanduser('~'), '.config/my_settings.json')
    with open(file, "r") as jsonfile:
        settings = json.load(jsonfile)

    openai.api_key = settings['OPENAI_API_KEY']
    arxiv_id = '2108.02216v2'
    pdf.download(arxiv_id)
    pdf.remove(arxiv_id)
    context = pdf.context(arxiv_id)
    chunks = embedding.chunks(context['fulltext'])
    print(len(chunks))

    embeddings = embedding.encode(chunks)
    print(len(embeddings))

    # data = response.json()
    # items = data.get("message", {}).get("items", [])
    # if items:
    #     first_item = items[0]
    #     doi = first_item.get("DOI")
    #     if doi:
    #         print(f'Found DOI: {doi}')
    #         doi_url = f"https://doi.org/{doi}"
    #         print(f"DOI URL: {doi_url}")



    # r = requests.get('http://api.crossref.org/works?query.bibliographic="Tyler B. Smith, Momentum-space Gravity from the Quantum Geometry and Entropy of Bloch Electrons"')
    # print(r.content)
