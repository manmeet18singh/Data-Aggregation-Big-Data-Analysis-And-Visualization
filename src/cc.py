import requests
import json
from io import StringIO
import gzip
import s3fs
from bs4 import BeautifulSoup

# Domains to search through
domains = ['espn.com', 'cnn.com', 'foxnews.com', 'cbssports.com', 'cbsnews.com', 'bleacherreport.com']

# Months to search through. February + March 2019
index_list = ["2019-09","2019-13"]

fs = s3fs.S3FileSystem(anon=True)

def get_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

def search_domain(domain):
 
    record_list = []
    
    print("[*] Trying target domain: " + domain)
    
    for index in index_list:
        
        print("[*] Trying index %s" % index)
        
        cc_url  = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
        cc_url += "url=%s&matchType=domain&output=json" % domain
        
        response = requests.get(cc_url)
        
        if response.status_code == 200:
            records = response.text.splitlines()
            
            for record in records:
                record_list.append(json.loads(record))
            
            print("[*] Added %d results." % len(records))
            
    
    print("[*] Found a total of %d hits." % len(record_list))
    
    print(record_list[1])
    return record_list  

def download_page(record):
 
    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1
 
    prefix = 'https://commoncrawl.s3.amazonaws.com/'
    
    resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
    # print(prefix + record['filename'])
    # resp = requests.get(prefix + record['filename'])
    
    # The page is stored compressed (gzip) to save space
    # We can extract it using the GZIP library
    raw_data = StringIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)
    
    # What we have now is just the WARC response, formatted:
    data = f.read()
    
    response = ""
    
    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass
            
    return response

def main():
    # for domain in domains:
    #     search_domain(domain)
    test = search_domain(domains[1])
    test2 = download_page(test[1])
    print(test2)

if __name__== "__main__":
  main()