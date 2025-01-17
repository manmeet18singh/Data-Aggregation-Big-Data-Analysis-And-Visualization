import requests
import json
import io
import gzip
import s3fs
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

stop_words = set(stopwords.words('english'))

# Domains to search through
domains = ['espn.com', 'foxsports.com', 'cbssports.com', 'sportingnews.com', 'bleacherreport.com']

# Months to search through. March 2019
index_list = ["2019-13"]

fs = s3fs.S3FileSystem(anon=True)

def get_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    print(soup.text)
    return soup.get_text()

def search_domain(domain):
 
    record_list = []
    
    print("Trying target domain: " + domain)
    
    for index in index_list:
        
        print("Trying index " + str(index))
        
        cc_url  = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
        cc_url += "url=%s&matchType=domain&output=json" % domain
        
        response = requests.get(cc_url)
        
        if response.status_code == 200:
            records = response.text.splitlines()
            
            for record in records:
                record_list.append(json.loads(record))
    
    print("Found a total of " + str(len(record_list)) + " hits.")
    
    return record_list  

def download_page(record):
 
    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1
 
    prefix = 'https://commoncrawl.s3.amazonaws.com/'
    
    resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
    
    raw_data = io.BytesIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)
    
    data = f.read()
    
    return data

def check_word(word):
    bad = ["<", "=", "\\", ":", "_", ".", "#", "@", "(", ")", "{", "}", ";", "[", "]", "\"", 
           "?", ">", ",", "/", "--", "*", "+", "||", "&&", "|"]
    for char in bad:
        if char in word:
            return False
    if word in stop_words:
        return False

    return True
    

def main():

    ### PROCESSING STEP 1 - Grab 100 articles from each domain ###

    for domain in domains:
        results = search_domain(domain)
        # for i in range(100):
        #     file = str(domain) + ".txt"
        #     f = open(file, "a")
        #     f.write(str(download_page(results[i])))
        #     f.write("\n\n\n")
        #     f.close()
        #     print("Wrote " + domain + " article " + str(i))

    ### PROCESSING STEP 2 - Drop header, turn into valid HTML, and snag text from beautiful soup ###

    # ps = PorterStemmer()

    # all_words = []

    # with open('sportingnews.com.txt', "r") as f:
    #     for line in f:
    #         what = line.strip('b\'')
    #         huh = what.strip()
    #         doc_pos = huh.find('<!DOC')
    #         # -1 because of the two newlines in txt file to seperate stuff
    #         if doc_pos != -1:
    #             html = huh[doc_pos:len(huh)]
    #             html = html.replace('\n','')
    #             html.strip(" ")
    #             html.strip("\t")

    #             # stem words
    #             words = html.split()
    #             for word in words:
    #                 ps.stem(word)
    #                 all_words.append(word)
     
    #     f.close()
    
    # good_words = []
    # # Filter/write out words to file
    # for word in all_words:
    #     if check_word(word):
    #         good_words.append(word)

    # good = " ".join(good_words)
    # f = open("sportingnews_words.txt", "w+")
    # f.write(good)
    f.close()
    
                
if __name__== "__main__":
  main()