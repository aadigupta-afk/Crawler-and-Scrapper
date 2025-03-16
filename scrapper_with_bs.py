from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import Html2TextTransformer
from bs4 import BeautifulSoup
import json

urlss = [""]


def extract_tag_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    header_id_content = soup.find('div', id='ssr-main').find('div', class_='App ThemeContext ThemeContext_dark ThemeContext_line').find('main', class_='rm-Guides').find('div', class_='rm-Container rm-Container_flex').find('article', class_='rm-Article', id = 'content').find('header', id='content-head')
    soup = BeautifulSoup(html_content, 'html.parser')
    section_content = soup.find('div', id='ssr-main').find('div', class_='App ThemeContext ThemeContext_dark ThemeContext_line').find('main', class_='rm-Guides').find('div', class_='rm-Container rm-Container_flex').find('article', class_= 'rm-Article', id = 'content').find('div', class_='grid-container-fluid', id='content-container').find('section', class_='content-body grid-100').find('div')

    return header_id_content,section_content

all_data= []
output_file_path = "data.json"

for url in urlss:
    loader = AsyncChromiumLoader(urls=[url], headless=True, user_agent="USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    
    html_documents = loader.load() 

    for html_doc in html_documents:
        html_content = html_doc.page_content
        

        data = extract_tag_content(html_content)
        new_page_content = ''.join(str(data))

        
    for doc in html_documents:
        doc.page_content = new_page_content
    

    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(html_documents)

    content = docs_transformed[0].page_content[0: ]  
    md = docs_transformed[0].metadata
    all_data.append({"page_content": content, "url": md})
    print(url)

with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=4, ensure_ascii=False)
