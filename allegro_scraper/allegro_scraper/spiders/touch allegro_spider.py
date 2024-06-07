import scrapy
import json

class AllegroSpider(scrapy.Spider):
    name = "allegro"
    allowed_domains = ["allegro.pl"]
    start_urls = ["https://allegro.pl/kategoria/zabawki-11818"]
    # allowed_domains = ["youtube.com"]
    # start_urls = ["https://www.youtube.com/"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'RETRY_TIMES': 5,  # Retry requests if they fail
        'RETRY_HTTP_CODES': [403, 500, 502, 503, 504],  # Retry on these HTTP codes
        'COOKIES_ENABLED': True,
        'ROTATING_PROXY_LIST': [
            '45.77.56.114:31802',
            '108.61.175.7:31802',
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


        # # Extract the script tags that contain JSON data
        script_tags = response.css("script[type='application/json']")
        # print(script_tags)

        mylist = []
        
        for script in script_tags:
            # print(script)
            try:
                # Extract the JSON content
                json_data = script.css("::text").get()
                
                # Parse the JSON content
                data = json.loads(json_data.strip())
                
                # Pretty-print the JSON data
                pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
                # print(pretty_json)
                mylist.append(pretty_json)

                
                # Check for specific key to determine if this is the desired data
                if 'baseUrl' in data:
                    self.log("Found the target JSON data!")
                    break

            except json.JSONDecodeError as e:
                self.log(f"Failed to parse JSON: {e}")
            except Exception as e:
                self.log(f"An error occurred: {e}")

        print(mylist)


# scrapy crawl allegro
