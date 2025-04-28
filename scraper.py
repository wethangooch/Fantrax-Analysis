# This file holds all of the stat scraping code

from curl2pyreqs.ulti import parseCurlString
import requests
import re
import json


def parse_curl(curl_command):
    # Extract the URL from the cURL command
    url_pattern = re.compile(r"curl\s+'([^']+)'")
    url_match = url_pattern.search(curl_command)
    if not url_match:
        raise ValueError("URL not found in cURL command")
    url = url_match.group(1)
    
    # Extract headers from the cURL command
    headers_pattern = re.compile(r"-H '([^:]+):\s([^']+)'")
    headers = {}
    for match in headers_pattern.findall(curl_command):
        headers[match[0]] = match[1]
    
    # Extract the data from the cURL command
    data_pattern = re.compile(r"--data-raw '([^']+)'")
    data_match = data_pattern.search(curl_command)
    data = None
    if data_match:
        data = json.loads(data_match.group(1))
    
    return url, headers, data


def scrape_managers(league_id):
    # Scrape manager data from the website

    cookies = {
    '_gat': '1',
    'cf_clearance': '4h54jTil1v4eNWwetK8Upch6SWM5VOoYnAmCj5GKIC4-1745796927-1.2.1.1-MaXmf.GF7LjZmHz12olbdSdFUHHGOsQ_0WddxFzgbAyD_sy9FRa8L6BJ6mZ_o1luQfPhVe8w01EEqPLoi7_Zd0mX92uPTScTs3bz5QZX2838UJyaOIawOnCLyam05_44ecMulEgIVi0pOhBRTV6WZcpB15q.xIBMgOPK1mUSsehZmD7FYrqUNV6KJ8.uod0XZ9_miN0y7NsyrXOPajQHBg4Ep0KeuZGRJ1OA6uxIV4xxgxG81vHIb3xxUOndVy2Y5ax9BGKt507HCbEdnwWHgYmEeJDtCH8GuEMOe77QqqoXk6wBiT6q2QNV2KbG7C18TGuGtlCxNW7f.YHh6wu_A3_gxldvobrMpbbxer8K0bw',
    '_ga_DM2Q31JXYV': 'GS1.2.1745796928.1.1.1745796941.47.0.0',
    'ui': 'z3b5f9yima0aey8q',
    '_gid': 'GA1.2.1506288446.1745796928',
    '_ga': 'GA1.2.229536404.1745796928',
    'FX_RM': '_qpxzVA0FDwpVWQQPGQpdBkVRBBgAFwkWAB0fBxZVEwMAUUM=',
    '__cf_bm': 'jUo4roeM8y0cw4C4RPxSxYVBnOPfGfVeR80SDI_sqw0-1745796927-1.0.1.1-iAwT6DPKFelDXaogGuib738BF6tzmoCBnA0ERoCyDuWyD7RKe77ipyw8_w.AAM5_xRXgb7gCSyw3ljeMWRjIVHURbZ2BuL07Hy5Qqik.N_E',
    'JSESSIONID': 'node010t40pzwub0r1lpqx68bfr08l35006.node0',
    'uig': 'z3b5f9yima0aey8q',
    }

    # Create a session object
    session = requests.Session()

    # Add cookies to the session
    for cookie in cookies:
        session.cookies.set(cookie, cookies[cookie])

    curl_command = """curl 'https://www.fantrax.com/fxpa/req?leagueId=6xmefwzslywuomj4' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'Referer: https://www.fantrax.com/fantasy/league/6xmefwzslywuomj4/home' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
  -H 'Accept: application/json' \
  -H 'sec-ch-ua: "Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"' \
  -H 'Content-Type: text/plain' \
  -H 'sec-ch-ua-mobile: ?0' \
  --data-raw '{"msgs":[{"method":"chatAdmin","data":{"func":"getLeagueAndGuestUsers"}}],"uiv":3,"refUrl":"https://www.fantrax.com/fantasy/league/6xmefwzslywuomj4/home","dt":0,"at":0,"av":"0.0","tz":"America/New_York","v":"167.0.1"}'"""

    url, headers, data = parse_curl(curl_command)
    response = session.post(url, headers=headers, json=data)
    
    print(response.json())


    pass




    








def main():
    # Core logic goes here

    league_id = "6xmefwzslywuomj4"  # Example league ID
    scrape_managers(league_id)

    pass
    



if __name__ == "__main__":
    main()