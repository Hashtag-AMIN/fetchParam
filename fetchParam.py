#!/usr/bin/env python3

import re ,requests, urllib3 ,random, validators, json
import os, time, sys, queue, argparse, concurrent.futures, warnings
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

banner = """

         ________        _          __      _______                                   
        |_   __  |      / |__       [  |    |_   __\                                  
        | |__\_|.---._| |-'.-| .-.| |--.__ | |  _)  |,--.__.--.  ,--. __ .--..--.--. 
          |  _|  /_/__\\| | / /'`\] | .-. |  |  ___/`'_\ :[ `/'`\]`'_\ :[ `.-. .-.  |  
         _| |_   | \__.,| |,| \__.  | | | | _| |_   // | |,| |    // | |,| | | | |  |______
        |_____|   '.__.'\__/'.___.'[___]|__]_____|  \'-;__[___]   \'-;__[___||__||__ ______]
        
                                                                             
                            
                                        ---------------------
                                        Fetch all Parameters from
                                        input, form ==> name & id
                                        a           ==> href parameter
                                        scripts     ==> var & let & const & Json_Keys
                                        ---------------------
                                             Hashtag_AMIN :)
                                        """

user_agent = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729;",
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
    "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Android; Tablet; rv:40.0) Gecko/40.0 Firefox/40.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508",
    "Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; Android 4.4.2; SM-T320 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Linux; Android 5.0.2; SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84",
    "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",
    "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143",
    "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0)",
]

def read_urls():
    url = all_args.url
    urls = all_args.urls
    read_urls_list = list()
    if url is not None:
        url = url.strip()
        read_urls_list.append(url)
        return read_urls_list
    if urls is not None:
        with open(urls ,"r") as f:
            for url in f.readlines():
                url = url.strip()
                if validators.url(url):
                    read_urls_list.append(url)
        return read_urls_list

def send_request(url):
    try:
        headers = {"User-Agent" : random.choice(user_agent), "X-Forwarded-For": "127.0.0.1"}
        response = requests.get(url=url, headers=headers , verify=False,timeout=5)#, proxies=proxies)
        if response.status_code in [200,401,403,500]:
            res_text = response.text
            return res_text
    except:
        raise ConnectionError("Can Not Connet Server")

def souping(request_text):
        soup = BeautifulSoup(request_text, 'html.parser')
        return soup

def extract_form_tag(soup):
    results = list()
    params = list()
    forms = soup.find_all("form")
    if forms != None:
        for form in forms:
            if "name" in form.attrs.keys():
                name_id = [form.attrs["name"]]
                results.append(name_id)
            if "id" in form.attrs.keys():
                var_id = [form.attrs["id"]]
                results.append(var_id)
        if len(results[0][0]) > 0:
            params.append(results[0][0])
    return params
    
def extract_input_tag(soup):
    result = list()
    params = list()
    inputs = soup.find_all("input")
    if inputs != None:
        for input in inputs:
            if "name" in input.attrs.keys():
                result.append([input.attrs["name"]][0])
            if "id" in input.attrs.keys():
                result.append([input.attrs["id"]][0])
            for result_input in result:
                params.append(result_input)
        return params

def extract_script_tag(soup):
    result = list()
    params = list()
    scripts = soup.find_all("script")
    if scripts != None:
        for script in scripts:
            vars_script = re.findall('var (\w+|\d+)', script.text)
            if len(vars_script) != 0:
                for variable in vars_script:
                    result.append(variable)
        for script in scripts:
            let_script = re.findall('let (\w+|\d+)', script.text)
            if len(let_script) != 0:
                for variable in let_script:
                    result.append(variable)
        for script in scripts:
            let_script = re.findall('const (\w+|\d+)', script.text)
            if len(let_script) != 0:
                for variable in let_script:
                    result.append(variable)
        for result_script in result:
            params.append(result_script)
        params = list(set(params))
    return params
    
def extract_a_tag(soup):
    result = list()
    a_tags = soup.find_all("a")
    if a_tags != None:
        for a in a_tags:
            link = a["href"]
            if link != "#" and "?" in link:
                keys = parse_qs(urlparse(link).query).keys()
                for key in keys:
                    result.append(key)
    return result

def extract_json_key(soup):
    result = list()
    params = list()
    scripts = soup.find_all("script", type="application/ld+json")
    if scripts != None:
        for script in scripts:
            json_keys = json.loads(script.text).keys()
            for json_key in json_keys:
                result.append(json_key)
        for result_script in result:
            params.append(result_script)
        params = list(set(params))
    return params

def fetch_param(soup):  # :)
    if soup != None:
        result_all = list()
        # form tag 
        results_form = extract_form_tag(soup=soup)
        
        for result_form in results_form:
            if len(result_form) > 2:
                result_all.append(result_form)
                
        # input tag
        results_input = extract_input_tag(soup=soup)

        for result_input in results_input:
            if len(result_input) > 2:
                result_all.append(result_input)
        # script tag:
        results_scripts = extract_script_tag(soup=soup)
        
        for result_scripts in results_scripts:
            if len(result_scripts) > 2:
                result_all.append(result_scripts)
        # a tag
        results_a = extract_a_tag(soup=soup)
        
        for result_a in results_a:
            if len(result_a) > 2:
                result_all.append(result_a)
        # Json Keys
        results_scripts = extract_json_key(soup=soup)

        for result_script in results_scripts:
                if "@" in result_script:
                    if len(result_script) > 3:
                        result_all.append(result_script[1:])
                        result_all.append(result_script)
                elif len(result_script) > 3:
                        result_all.append(result_script)
    
        #add result
        if result_all != None:
            return result_all
        return False
    return False

finall_result = list()
def collect_param(url):
    result_all = list()
    result_uniq = list()
    responeTXT = send_request(url)
    soup = souping(responeTXT)
    
    fetch_param_result = fetch_param(soup=soup)
    
    if fetch_param_result != False and  len(fetch_param_result) > 0:
        for param in fetch_param_result:
            result_all.append(param)
                
    result_uniq = list(set(result_all))
    if len(result_uniq) > 0 :
        for param in result_uniq:
            finall_result.append(param)
        
def main():
    uniq_param = list()
    all_urls = read_urls()

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_num) as executor:
        future_to_url = {executor.submit(collect_param, url): url for url in all_urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                if not silent:
                    print(f"[+] [Done] Request Send to: {url}")
            except:
                if not silent:
                    print(f"[-] [feild] Request Send to: {url}    ")
    
    uniq_param = list(set(finall_result))
    if output is not None:
        with open( output , "w") as f:
                for param in uniq_param:
                    f.write(param+"\n")
    else:
        for result in uniq_param:
            print(result)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(prog='fetchParam.py',
    description="""Send Request & fetch [a, input, form & variable in JSfile] Parameters""",
    usage="""

    Example:
            python3 fetchParam.py [options] file [ output ]
            python3 fetchParam.py --url http://example.com
            python3 fetchParam.py --urls urls.txt
            python3 fetchParam.py --urls urls.txt --threads 100 --silent
            python3 fetchParam.py --urls urls.txt --threads 100 --output Params.txt
            
            """)
    parser.add_argument('-u','--url', type=str, default=None, help='Enter a url to fetch the parameters')
    parser.add_argument('-U','--urls', type=str, default=None, help='Enter a urls file to fetch the parameters')
    parser.add_argument('-t','--threads', type=int, default=5, help='Enter threads to send parallel request: default: 5')
    parser.add_argument('-o','--output', type=str, default=None, help='Write result output file, Not in terminal')
    parser.add_argument('-s','--silent', action="store_true", help='Skip banner & logs')

    all_args = parser.parse_args()
    url = all_args.url
    urls = all_args.urls
    thread_num = all_args.threads
    silent = all_args.silent
    output = all_args.output

    if not silent:
        print(banner)
        
    if url == None and urls == None:
        parser.print_usage()
        sys.exit(-1)
    elif url != None and urls == None:
        if validators.url(url) != True:
            parser.print_usage()
            sys.exit(-1)
    elif url == None and urls != None:
        if os.path.isfile(urls) != True:
            parser.print_usage()
            sys.exit(-1)

    main()