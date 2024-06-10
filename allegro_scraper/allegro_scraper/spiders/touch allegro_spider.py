import scrapy
import json

class AllegroSpider(scrapy.Spider):
    name = "allegro"
    # allowed_domains = ["allegro.pl"]
    # start_urls = ["https://allegro.pl/kategoria/zabawki-11818"]
    # allowed_domains = ["youtube.com"]
    # allowed_domains = ["pracuj.pl"]
    # start_urls = ["https://www.pracuj.pl/praca/administracja%20biurowa;cc,5001"] 
    allowed_domains = ["olx.pl"]
    start_urls = ["https://www.olx.pl/praca/administracja-biurowa/"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'RETRY_TIMES': 5,  # Retry requests if they fail
        'RETRY_HTTP_CODES': [403, 500, 502, 503, 504],  # Retry on these HTTP codes
        'COOKIES_ENABLED': True,
        'ROTATING_PROXY_LIST': [
            '51.254.69.243:3128',
            '81.171.24.199:3128',
        ],
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
        }
    }

    def parse(self, response):
        if response.status == 403:
            self.log("Access forbidden - 403 error.")
            return
        
        # print(response)
        # print(response.body.decode('utf-8'))

        data = response.body.decode('utf-8')
        print('################## DATA ##################', data[120000:140000])
        print('################## TOTAL LENGTH OF DATA ##################')
        print(len(data))


        # ____________________________# olx.pl # ____________________________#
        script_tags = response.css("script[type='application/ld+json']")
        print("################### script_tags ##################", script_tags)
        # ____________________________# end of olx.pl # ____________________________#



        # ____________________________# pracuj.pl # ____________________________#
        # Check if the response body is in JSON format
        # content_type = response.headers.get('Content-Type', '').decode('utf-8')
        # print("################### content_type ##################", content_type)
        
        # if 'application/json' in content_type:
        #     # Direct JSON response
        #     data = json.loads(response.body)
        #     pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
        #     print(pretty_json)
        # else:
        #     script_tag = response.css("script#__NEXT_DATA__")

        #     if script_tag:
        #         try:
        #             # Extract the JSON content from the <script> tag
        #             json_data = script_tag.css("::text").get()
                    
        #             if json_data:
        #                 # Parse and pretty-print the JSON content
        #                 data = json.loads(json_data.strip())
        #                 pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
        #                 print("################### pretty_json ##################", pretty_json)
        #             else:
        #                 print("No JSON content in the '__NEXT_DATA__' script tag.")
        #         except json.JSONDecodeError as e:
        #             self.log(f"Failed to parse JSON: {e}")
        #         except Exception as e:
        #             self.log(f"An error occurred: {e}")
        #     else:
        #         print("The '__NEXT_DATA__' script tag was not found.")

        
        # ____________________________## ____________________________## ____________________________#


        # # # Extract the script tags that contain JSON data
        # script_tags = response.css("script[type='application/json']")
        # # print(script_tags)

        # mylist = []
        
        # for script in script_tags:
        #     # print(script)
        #     try:
        #         # Extract the JSON content
        #         json_data = script.css("::text").get()
                
        #         # Parse the JSON content
        #         data = json.loads(json_data.strip())
                
        #         # Pretty-print the JSON data
        #         pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
        #         print(pretty_json)
        #         # mylist.append(pretty_json)

                
        #         # Check for specific key to determine if this is the desired data
        #         if 'baseUrl' in data:
        #             self.log("Found the target JSON data!")
        #             break

        #     except json.JSONDecodeError as e:
        #         self.log(f"Failed to parse JSON: {e}")
        #     except Exception as e:
        #         self.log(f"An error occurred: {e}")

        # print(mylist)


# scrapy crawl allegro
