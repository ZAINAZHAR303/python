import pymongo
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin  


requests.packages.urllib3.disable_warnings()


client = pymongo.MongoClient("mongodb+srv://zain:n8fvmhudsxtHKhVC@cluster0.r1g32.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
db = client['loan_data_db']  
collection = db['agriculture_loans']  


html_text = requests.get('https://ztbl.com.pk/', verify=False).text
soup = BeautifulSoup(html_text, 'lxml')


list_items = soup.find_all('li', class_='li-dropdown')
if len(list_items) >= 3:
    agriculture_loans_li = list_items[2]  

    
    nested_list_items = agriculture_loans_li.find_all('li')

    
    for nested_item in nested_list_items:
        
        link = nested_item.find('a')
        if link and link.get('href'):
            name = link.text.strip()
            url = urljoin('https://ztbl.com.pk', link['href'])

            try:
                
                response = requests.get(url, verify=False)
                response.raise_for_status()
                print(f"Successfully fetched {url}")

                
                page_soup = BeautifulSoup(response.text, 'lxml')

                
                h2_tag = page_soup.find('h2')
                h2_content = h2_tag.get_text(strip=True) if h2_tag else None

                
                p_tags = page_soup.find_all('p')
                paragraphs = [p.get_text(strip=True) for p in p_tags]

                
                table = page_soup.find('table')
                table_content = []
                if table:
                    headers = table.find_all('strong')  
                    rows = table.find_all('tr')
                    
                    
                    table_headers = [header.get_text(strip=True) for header in headers]
                    for row in rows:
                        columns = row.find_all(['td', 'th'])
                        row_data = [column.get_text(strip=True) for column in columns]
                        if row_data:
                            table_content.append(dict(zip(table_headers, row_data)))

                
                loan_data = {
                    'name': name,
                    'url': url,
                    'h2': h2_content,
                    'paragraphs': paragraphs,
                    'table': table_content
                }

                
                collection.insert_one(loan_data)
                print(f"Data for '{name}' stored in MongoDB.")

            except requests.exceptions.RequestException as e:
                print(f"Failed to fetch {url}: {e}")
else:
    print("The third <li> (Agriculture Loans) was not found.")


client.close()
