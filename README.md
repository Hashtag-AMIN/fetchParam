

# ⚡️ fetchParam

<h3> 👨‍💻 This tool can extract : </h3>

   * name & id from a & input tags 
   * var & let & const variable from scripts tags 
   * Json keys from scripts tags 
   * href parameter from a tags


## 🖥 &nbsp; Installation

&nbsp;&nbsp;<img src="https://img.shields.io/badge/Python-informational?style=flat&logo=python&logoColor=white&color=blue">

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Dependency.

```bash
git clone https://github.com/Hashtag-AMIN/fetchParam
python3 -m pip install -r requirement.txt
cp fetchParam.py /usr/local/sbin
fetchParam.py -h
```


## 💻🌐&nbsp;Usage

<h3>&nbsp;&nbsp; This tool can create custom wordlist for Arjun, x8 or Mass Assignment attacks  </h3>

```text


         ________        _          __      _______
        |_   __  |      / |__       [  |    |_   __\
        | |__\_|.---._| |-'.-| .-.| |--.__ | |  _)  |,--.__.--.  ,--. __ .--..--.--.
          |  _|  /_/__\| | / /'`\] | .-. |  |  ___/`'_\ :[ `/'`\]`'_\ :[ `.-. .-.  |
         _| |_   | \__.,| |,| \__.  | | | | _| |_   // | |,| |    // | |,| | | | |  |______
        |_____|   '.__.'\__/'.___.'[___]|__]_____|  '-;__[___]   '-;__[___||__||__ ______]



                                        ---------------------
                                        Fetch all Parameters from
                                        input, form ==> name & id
                                        a           ==> href parameter
                                        scripts     ==> var & let & const & Json_Keys
                                        ---------------------
                                             Hashtag_AMIN :)

usage:

    Example:
            python3 fetchParam.py [options] file [ output ]
            python3 fetchParam.py --url http://example.com
            python3 fetchParam.py --urls urls.txt
            python3 fetchParam.py --urls urls.txt --threads 100 --silent
            python3 fetchParam.py --urls urls.txt --threads 100 --output Params.txt

    Send Request & fetch [a, input, form & variable in JSfile] Parameters

    options:
    -h, --help            show this help message and exit
    -u URL, --url URL     Enter a url to fetch the parameters
    -U URLS, --urls URLS  Enter a urls file to fetch the parameters
    -t THREADS, --threads THREADS
                            Enter threads to send parallel request: default: 5
    -o OUTPUT, --output OUTPUT
                            Write result output file, Not in terminal
    -s, --silent          Skip banner & logs
```

<h4> This tool give url or urls file: </h4>

```bash
python3 fetchParam.py --url http://example.com
```

```bash
python3 fetchParam.py --urls urls.txt
```

<h4> You can handle threads: </h4>

```bash
python3 fetchParam.py --urls urls.txt --threads 100
```

<h4> So you can handle output and logs & banner too: </h4>

```bash
python3 fetchParam.py --urls urls.txt --threads 100 --silent --output param.txt
```

## 🔧⚙️&nbsp; Features

<h3> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  This tool works without headless Chromium browser or Chromium Drive  </h3>

<br>

<h5> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Happy Learning  </h5>
<h5> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Enjoy Hunting  </h5>
