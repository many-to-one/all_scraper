import html
from bs4 import BeautifulSoup
import scrapy
import json

# scrapy crawl allegro

class AllegroSpider(scrapy.Spider):
    name = "allegro"
    # allowed_domains = ["allegro.pl"]
    # start_urls = ["https://allegro.pl/kategoria/zabawki-edukacyjne-11821"]
    # allowed_domains = ["youtube.com"]
    # allowed_domains = ["pracuj.pl"]
    # start_urls = ["https://www.pracuj.pl/praca/badania%20i%20rozw%C3%B3j;cc,5002"] 
    # allowed_domains = ["olx.pl"]
    # start_urls = ["https://www.olx.pl/praca/administracja-biurowa/"]
    # allowed_domains = ["otomoto.pl"]
    # start_urls = ["https://www.otomoto.pl/osobowe"] 
    allowed_domains = ["amazon.pl"]
    start_urls = ["https://www.amazon.pl/gp/browse.html?node=20861470031&ref_=nav_em_toys_blocks_0_2_8_4"]


    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'RETRY_TIMES': 5,  # Retry requests if they fail
        'RETRY_HTTP_CODES': [403, 500, 502, 503, 504],  # Retry on these HTTP codes
        'COOKIES_ENABLED': True,
        'ROTATING_PROXY_LIST': [
            '50.168.72.119:80',
            '50.217.226.44:80',
            '5.189.184.6:80',
            '195.23.57.78:80',
            '89.22.120.116:80',
            '50.223.239.183:80',
            '34.122.187.196:80',
            '50.174.145.12:80',
            '50.207.199.87:80',
            '50.169.135.10:80',
            '50.174.7.158:80',
            '50.168.72.118:80',
            '104.225.220.233:80',
            '23.254.231.55:80',
            '116.203.28.43:80',
            '51.254.69.243:3128',
            '81.171.24.199:3128',
        ],
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
        #     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        #     'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        }
    }


    # ____________________________# allegro.pl # ____________________________#
    # def parse(self, response):
    #     if response.status == 403:
    #         self.log("Access forbidden - 403 error.")
    #         return

    #     product_info = {}

    #     # Extracting image source
    #     product_info['image_src'] = response.css('img::attr(src)').get()

    #     # Extracting product name
    #     product_info['product_name'] = response.css('h2::text').get().strip()

    #     # Extracting price
    #     product_info['price'] = response.css('span._6a66d_0FiDs::text').get().strip()

    #     # Extracting delivery price
    #     product_info['delivery_price'] = response.css('div.mqu1_g3::text').get().strip()

    #     # Extracting number of buyers
    #     product_info['buyers'] = response.css('div.munh_56_l::text').get().strip()

    #     yield product_info
        # ____________________________# end of allegro.pl # ____________________________#



    # ____________________________# allegro.pl new # ____________________________#
    def parse(self, response):
        if response.status == 403:
            self.log("Access forbidden - 403 error.")
            return

        # Debugging: Print the page URL
        # self.log(f'Scraping BODY ###############: {response.body}')

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', {'class': '_octopus-search-result-card_style_apbSearchResultItem__2-mx4'})
        # print('############ TITLES #############', quotes)
        for quote in quotes:
            for i in quote:

                yield {
                    '############ TITLE #############': i.find_all('span')
                }




    # ____________________________# olx.pl # ____________________________#
    # def parse(self, response):
    #     if response.status == 403:
    #         self.log("Access forbidden - 403 error.")
    #         return

    #     for job in response.css('div.jobs-ad-card'):
    #         job_title = job.css('a h6::text').get()
    #         job_link = job.css('a::attr(href)').get()
            
    #         # Drukowanie wyników
    #         self.log(f'Title: {job_title}')
    #         self.log(f'Link: {job_link}')
            
    #         # Można tutaj dodać logikę, która będzie zapisywała dane do pliku lub przekazywała je dalej
    #         yield {
    #             'title': job_title,
    #             'link': response.urljoin(job_link)  # Tworzy pełny URL do oferty pracy
    #         }

        # Find the link to the next page
        # next_page = response.css('a[data-testid="pagination-forward"]::attr(href)').get()
        
        # if next_page:
        #     # Construct the full URL and request the next page
        #     next_page_url = response.urljoin(next_page)
        #     print(' @#@#@#@#@#@ NEXT PAGE @#@#@#@#@#@ ')
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)
    # ____________________________# end of olx.pl # ____________________________#




    # ____________________________# pracuj.pl # ____________________________#

    # def parse(self, response):
    #     if response.status == 403:
    #         self.log("Access forbidden - 403 error.")
    #         return

    #     for job in response.css('div[data-test="section-offers"] > div'):
    #         job_title = job.css('h2 a::text').get()
    #         job_url = job.css('a[data-test="link-offer"]::attr(href)').get()
    #         publication_date = job.css('p[data-test="text-added"]::text').get()
    #         location = job.css('h4::text').get()

    #         # Print the extracted information (for debugging)
    #         # self.log(f'Title: {job_title}')
    #         # self.log(f'URL: {job_url}')
    #         # self.log(f'Publication Date: {publication_date}')
    #         # self.log(f'Location: {location}')

    #         yield {
    #             'title': job_title,
    #             'url': response.urljoin(job_url),  # Form the full URL
    #             'publication_date': publication_date,
    #             'location': location
    #         }

    #     import re
    #     # Find the link to the next page
    #     next_page_button = response.css('button[data-test="bottom-pagination-button-next"]')
        
    #     if next_page_button:
    #         # Assume URL changes predictably for next page, e.g., "?page=2", "?page=3", etc.
    #         # Extract current page number from URL
    #         current_page = response.url.split('pn=')[-1] if 'pn=' in response.url else '1'
    #         try:
    #             next_page_number = int(current_page) + 1
    #         except ValueError:
    #             next_page_number = 2
            
    #         # Create next page URL
    #         if 'pn=' in response.url:
    #             next_page_url = re.sub(r'pn=\d+', f'pn={next_page_number}', response.url)
    #         else:
    #             # If there's no page parameter, add one
    #             next_page_url = f"{response.url}?pn={next_page_number}"
            
    #         self.log(f'Navigating to next page: {next_page_url}')
            
    #         # Request the next page
    #         yield scrapy.Request(url=next_page_url, callback=self.parse)

    #     else:
    #         self.log("No next page button found or last page reached.")
    # ____________________________# end of pracuj.pl # ____________________________#





    # ____________________________# otomoto.pl # ____________________________#

    # def parse(self, response):
    #     if response.status == 403:
    #         self.log("Access forbidden - 403 error.")
    #         return

    #     for job in response.css('div[data-testid="search-results"] > div'):
    #         job_title = job.css('h1 a::text').get()
    #         # job_url = job.css('a[data-test="link-offer"]::attr(href)').get()
    #         # publication_date = job.css('p[data-test="text-added"]::text').get()
    #         # location = job.css('h4::text').get()

    #         # Print the extracted information (for debugging)
    #         # self.log(f'Title: {job_title}')
    #         # self.log(f'URL: {job_url}')
    #         # self.log(f'Publication Date: {publication_date}')
    #         # self.log(f'Location: {location}')

    #         yield {
    #             'title': job_title,
    #             # 'url': response.urljoin(job_url),  # Form the full URL
    #             # 'publication_date': publication_date,
    #             # 'location': location
    #         }
        
        # ____________________________# end of otomoto.pl # ____________________________#





    # ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    # def parse(self, response):
    #     if response.status == 403:
    #         self.log("Access forbidden - 403 error.")
    #         return
   
        # print(response)
        # print(response.body.decode('utf-8'))

        # data = response.body.decode('utf-8'
        # print('################## DATA ##################', data[120000:140000])
        # print('################## TOTAL LENGTH OF DATA ##################')
        # print(len(data))


        # # ____________________________# olx.pl # ____________________________#
        # script_tags = response.css("script[type='application/ld+json']")
        # print("################### script_tags ##################", script_tags)
        # # ____________________________# end of olx.pl # ____________________________#



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
        #                 # for dt in pretty_json:
        #                 print("################### pretty_json ##################", pretty_json["groupedOffers"])
        #             else:
        #                 print("No JSON content in the '__NEXT_DATA__' script tag.")
        #         except json.JSONDecodeError as e:
        #             self.log(f"Failed to parse JSON: {e}")
        #         except Exception as e:
        #             self.log(f"An error occurred: {e}")
        #     else:
        #         print("The '__NEXT_DATA__' script tag was not found.")

        
        # ____________________________## ____________________________## ____________________________#


        # # Extract the script tags that contain JSON data
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



# <div class="mpof_ki mp7g_oh mg9e_8 mj7a_8 m7er_k4 mjyo_6x mgmw_3z _6a66d_i2yJ- mx7m_1 mnyp_co mlkp_ag mwdn_1 mh36_24 mvrt_24 _6a66d_u7-8J">
#     <div>
#         <div class="mpof_ki myre_zn m389_6m mse2_56 _6a66d_vtb7E">
#             <div class="mpof_ki mp7g_oh">
#                 <a href="https://allegro.pl/events/clicks?emission_unit_id=fec18f08-c04a-4f3a-8b61-65edcbeec588&amp;emission_id=1cb37584-ccd0-440c-b294-d4d4b1ff829c&amp;type=OFFER&amp;ts=1718095910237&amp;redirect=https%3A%2F%2Fallegro.pl%2Foferta%2Fklocki-magnetyczne-konstrukcyjne-swiecacy-tor-110el-3d-magnetic-edukacyjne-14518133089%3Fbi_s%3Dads%26bi_m%3Dlisting%253Adesktop%253Acategory%26bi_c%3DNTBmYmIzNTItZDU3Mi00ZTViLTk2ZjEtYjFlMjAyOWZjZGE1AA%26bi_t%3Dape&amp;placement=listing:desktop:category&amp;sig=503aa7d27ccdd54c997078cfdd137b6c" 
#                     class="msts_9u mg9e_0 mvrt_0 mj7a_0 mh36_0 mpof_ki m389_6m mx4z_6m m7f5_6m mse2_k4 m7er_k4 _6a66d_fmANP  " rel="nofollow" aria-hidden="true" tabindex="-1">
#                     <img alt="KLOCKI MAGNETYCZNE KONSTRUKCYJNE ŚWIECĄCY TOR 110el 3D MAGNETIC EDUKACYJNE" 
#                         src="https://a.allegroimg.com/s180/1191e3/c3f6c7e043eea2960b6f065d538a/KLOCKI-MAGNETYCZNE-KONSTRUKCYJNE-SWIECACY-TOR-110el-3D-MAGNETIC-EDUKACYJNE" 
#                         data-src="https://a.allegroimg.com/s180/1191e3/c3f6c7e043eea2960b6f065d538a/KLOCKI-MAGNETYCZNE-KONSTRUKCYJNE-SWIECACY-TOR-110el-3D-MAGNETIC-EDUKACYJNE">
#                 </a>
#             </div>
#             <div class="mg9e_8 mpof_5r mpof_z0_x mzmg_6m">
#                 <span class="mgn2_12 mpof_vs mgmw_3z _6a66d_xn36M">dostępne warianty</span>
#             </div>
#         </div>
#     </div>
#     <div class="mpof_ki myre_zn mh36_8 mjyo_6x _6a66d_5o-oq">
#         <div class="m7er_k4">
#             <div class="m0t1_f9 mpof_ki myre_zn m389_0a">
#                 <div class="mg9e_8 _6a66d_-55wz">
#                     <div class="mpof_ki m7f5_6m" data-test-tag="observed-holder">
#                         <button aria-label="POLUB" title="POLUB" 
#                             class="mgn2_14 mp0t_0a mgmw_wo mqu1_21 mj9z_5r mli8_k4 mqen_m6 l1fas mg9e_0 mvrt_0 mj7a_0 mh36_0 m911_5r mefy_5r mnyp_5r mdwl_5r msa3_z4 m0qj_5r msts_n7 l1v1s mpof_ki m389_6m mp7g_oh mp4t_0 m3h2_0 mryx_0 munh_0 _6a66d_wB9fd _6a66d_x8XXl" data-test-tag="observed-link">
#                         </button>
#                     </div>
#                 </div>
#                 <div class="mqu1_g3 mzmg_f9 _6a66d_Gz-kx mzmg_f9 mpof_5r mpof_z0_s">
#                     <span class="mpof_z0 mgmw_3z mgn2_12 _6a66d_gjNQR ">Firma</span>
#                 </div>
#             </div>
#             <div class="mj7a_4 m3h2_56 mpof_ki">
#                 <div data-test-tag="dsa">
#                     <span class="mp0t_0a mgn2_12 mqu1_16 mli8_k4 mgmw_3z mp4t_4 mryx_0 mqen_32">Sponsorowane</span>
#                         <button class="m911_5r mefy_5r mnyp_5r mdwl_5r msts_n7 mupj_mm mqen_m6" data-test-tag="dsa-button">
#                             <img class="m7er_k4 _6a66d_a8tj- " 
#                                 src="https://a.allegroimg.com/original/34a646/639f929246af8f23da49cf64e9d7/action-common-information-33306995c6" alt="pokaż podpowiedź">
#                         </button>
#                     </div>
#                 </div>
#                 <h2 class="mgn2_14 m9qz_yp meqh_en mpof_z0 mqu1_16 m6ax_n4 mp4t_0 m3h2_0 mryx_0 munh_0 mj7a_4">
#                     <a 
#                         class="mgn2_14 mp0t_0a mgmw_wo mj9z_5r mli8_k4 mqen_m6 l1fas l1igl meqh_en mpof_z0 mqu1_16 m6ax_n4 _6a66d_LPwkT  " 
#                         href="https://allegro.pl/events/clicks?emission_unit_id=fec18f08-c04a-4f3a-8b61-65edcbeec588&amp;emission_id=1cb37584-ccd0-440c-b294-d4d4b1ff829c&amp;type=OFFER&amp;ts=1718095910237&amp;redirect=https%3A%2F%2Fallegro.pl%2Foferta%2Fklocki-magnetyczne-konstrukcyjne-swiecacy-tor-110el-3d-magnetic-edukacyjne-14518133089%3Fbi_s%3Dads%26bi_m%3Dlisting%253Adesktop%253Acategory%26bi_c%3DNTBmYmIzNTItZDU3Mi00ZTViLTk2ZjEtYjFlMjAyOWZjZGE1AA%26bi_t%3Dape&amp;placement=listing:desktop:category&amp;sig=503aa7d27ccdd54c997078cfdd137b6c" title="" rel="nofollow">
#                             KLOCKI MAGNETYCZNE KONSTRUKCYJNE ŚWIECĄCY TOR 110el 3D MAGNETIC EDUKACYJNE
#                     </a>
#                 </h2>
#                 <div class="mpof_ki m389_6m msa3_z4 mj7a_4 mgn2_12" aria-label="od Super Sprzedawcy">od<!-- --> 
#                     <div class="mpof_ki mp7g_oh _6a66d_jQ1a4">
#                         <div class="mpof_vs mp7g_oh">
#                             <picture class="">
#                                 <source media="(prefers-color-scheme: dark)" 
#                                     srcset="https://a.allegroimg.com/original/34e1bf/82d1aebc4a9db9bef96345fd1e99/dark-information-common-super-seller-236577cfa7">
#                                     <img class="m7er_k4 _6a66d_a8tj-" 
#                                     src="https://a.allegroimg.com/original/34dd95/40d81c26458ca692070c8ed7eae5/information-common-super-seller-236577cfa7" alt="">
#                             </picture>
#                             <div data-test-tag="hover-message-wrapper" class="mjyo_6x mp7g_f6 mjb5_w6 msbw_2 mldj_2 mtag_2 mm2b_2 mgmw_wo msts_n6 m7er_k4 tify42 tidkhk _6a66d_pgnfd ti11a2 m9vn_gl m9vn_d2_l mpof_5r">
#                         </div>
#                     </div>
#                 </div> 
#                 <!-- -->Super Sprzedawcy
#             </div>
#             <div class="m7er_k4 mpof_5r mpof_z0_s">
#                 <div class="mgn2_12 mj7a_2 " aria-label="Parametry oferty">
#                     <dl class="mp4t_0 m3h2_0 mryx_0 munh_0 mg9e_0 mvrt_0 mj7a_0 mh36_0 meqh_en msa3_z4 m6ax_n4">
#                         <dt class="mpof_uk mgmw_3z mp4t_0 m3h2_0 mryx_0 munh_0 mg9e_0 mvrt_0 mj7a_0 mh36_0 _6a66d_r2-gF">Stan</dt>
#                         <dd class="mpof_uk mp4t_0 m3h2_0 mryx_0 munh_0 mgmw_wo mg9e_0 mj7a_0 mh36_0 mvrt_8 _6a66d_9KC9A ">Nowy</dd>
#                         <dt class="mpof_uk mgmw_3z mp4t_0 m3h2_0 mryx_0 munh_0 mg9e_0 mvrt_0 mj7a_0 mh36_0 _6a66d_r2-gF">Wiek dziecka</dt>
#                         <dd class="mpof_uk mp4t_0 m3h2_0 mryx_0 munh_0 mgmw_wo mg9e_0 mj7a_0 mh36_0 mvrt_8 _6a66d_9KC9A ">3 lata +</dd>
#                         <dt class="mpof_uk mgmw_3z mp4t_0 m3h2_0 mryx_0 munh_0 mg9e_0 mvrt_0 mj7a_0 mh36_0 _6a66d_r2-gF">Liczba elementów</dt>
#                         <dd class="mpof_uk mp4t_0 m3h2_0 mryx_0 munh_0 mgmw_wo mg9e_0 mj7a_0 mh36_0 mvrt_8 _6a66d_9KC9A ">110 szt.</dd>
#                     </dl>
#                 </div>
#             </div>
#             <div class="mg9e_4">
#                 <div class="mj7a_4">
#                     <div class="mpof_92 myre_zn">
#                         <div class="msa3_z4 mpof_ki m389_0a _6a66d_gAhFO">
#                             <span class="mli8_k4 msa3_z4 mqu1_1 mgmw_qw mp0t_ji m9qz_yo mgn2_27 mgn2_30_s" aria-label="aktualna cena 129,00&nbsp;zł" data-test-tag="price-container">
#                                 <div class="mli8_k4 msa3_z4 mqu1_1 mp0t_ji m9qz_yo mgn2_27 mgn2_30_s mgmw_g5">129,<span class="mgn2_19 mgn2_21_s m9qz_yq">00</span>&nbsp;
#                                     <span class="mgn2_19 mgn2_21_s m9qz_yq">zł</span>
#                                 </div>
#                             </span>
#                         </div>
#                     </div>
#                     <span class="_6a66d_0FiDs"> 
#                         <div class="mpof_vs mp7g_oh">
#                             <span class="_6a66d_40QIU">
#                                 <div class="mgn2_12 mpof_ki m389_6m mwdn_1 " aria-label=" Smart!">
#                                     <div class="_6a66d_lw2XW mpof_ki mwdn_1 m389_6m _6a66d_N6HYD">
#                                         <picture class="mpof_z0 _6a66d_3US8T mli2_0">
#                                             <source 
#                                                 media="(prefers-color-scheme: dark)" 
#                                                 srcset="https://a.allegroimg.com/original/34611c/c433ab0c4bf9a76e4f1f15b5dd1f/dark-brand-subbrand-smart-2ecf1fa38c.svg">
#                                                 <img class="mpof_z0 _6a66d_uVDCA  " src="https://a.allegroimg.com/original/343b4d/ed3f5c04412ab7bd70dd0a34f0cd/brand-subbrand-smart-d8bfa93f10.svg" alt="Smart!">
#                                         </picture>
#                                     </div>
#                                 </div>
#                             </span>
#                             <div data-test-tag="hover-message-wrapper" 
#                                 class="mjyo_6x mp7g_f6 mjb5_w6 msbw_2 mldj_2 mtag_2 mm2b_2 mgmw_wo msts_n6 m7er_k4 tify42 tidkhk _6a66d_pgnfd ti11a2 m9vn_gl m9vn_d2_l mpof_5r">
#                             </div>
#                         </div>
#                     </span>
#                     <div class="mgn2_14 msa3_z4 mp4t_4 mgmw_g5" data-test-tag="netPrice">
#                         <span class="m9qz_yr mpof_vs">104,88&nbsp;zł</span> <!-- -->netto
#                     </div>
#                 </div>
#                 <div data-onboarding-hook="bpg">
#                     <div class="mgn2_12 mpof_ki m389_6m mwdn_1 mj7a_4" aria-label="  Gwarancja najniższej ceny">
#                         <div style="font-weight:normal;text-decoration:none" class="_6a66d_lw2XW mpof_ki mwdn_1 m389_6m _6a66d_N6HYD">
#                             <picture class="mpof_z0 _6a66d_3US8T mli2_0">
#                                 <source media="(prefers-color-scheme: dark)" 
#                                 srcset="https://a.allegroimg.com/original/349f4b/d6b5d489425a84e359ef29fe6358/dark-information-benefits-badge-check-solid-5fba5fae0e">
#                                 <img class="mpof_z0 _6a66d_uVDCA  " src="https://a.allegroimg.com/original/34027e/82300c8b45e28642166596e878cb/information-benefits-badge-check-solid-10f517f89a" alt="">
#                             </picture>
#                             <span class="mj7a_2 mg9e_2 mli2_0" style="color:var(--m-color-price-bargain, #107b1e);font-weight:normal;text-decoration:none"> Gwarancja najniższej ceny</span>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="mgn2_12 mpof_ki m389_6m mwdn_1 mj7a_4" aria-label=" 60 dni na spłatę">
#                     <div style="color:#ffffff;background-color:#144393" class="_6a66d_lw2XW msbw_2 mldj_2 mtag_2 mm2b_2 mgmw_3z mh36_4 mvrt_4 mj7a_2 mg9e_2 mwdn_0">
#                         <span class="mj7a_2 mg9e_2 mli2_0">60 dni na spłatę</span>
#                 </div>
#             </div>
#         </div>
#         <div class="mj7a_4">
#             <div class="mqu1_g3 mgn2_12">138,99&nbsp;zł z dostawą</div>
#         </div>
#     </div>
#     <div class="mpof_ki m389_6m m7er_k4 m7f5_sf mp4t_56 mwdn_1">
#         <div class="mgn2_12 mpof_ki m389_6m mwdn_1 mj7a_4" aria-label=" kup do 13:00 -  dostawa jutro">
#             <div class="_6a66d_lw2XW mpof_ki mwdn_1 m389_6m _6a66d_N6HYD">
#                 <span class="mj7a_2 mg9e_2 mli2_0" style="color:var(--m-color-text-secondary, #656565);font-weight:bold;text-decoration:none">kup do 13:00 - </span>
#                 <span class="mj7a_2 mg9e_2 mli2_0" style="color:var(--m-color-green, #1bb826);font-weight:bold;text-decoration:none">dostawa jutro</span>
#                 <div class="mpof_vs mp7g_oh">
#                 <picture class="mpof_z0 _6a66d_3US8T mli2_0">
#                     <source media="(prefers-color-scheme: dark)" srcset="https://assets.allegrostatic.com/fast-delivery-icons/information-dark.svg">
#                     <img class="mpof_z0 _6a66d_uVDCA  " src="https://assets.allegrostatic.com/fast-delivery-icons/information.svg" alt="">
#                 </picture>
#                 <div data-test-tag="hover-message-wrapper" 
#                     class="mjyo_6x mp7g_f6 mjb5_w6 msbw_2 mldj_2 mtag_2 mm2b_2 mgmw_wo msts_n6 m7er_k4 tify42 tidkhk _6a66d_pgnfd ti11a2 mpof_5r">
#                 </div>
#             </div>
#         </div>
#     </div>
#     <div class="mpof_ki m389_a6 munh_56_l mj7a_4">
#         <span class="msa3_z4 mgn2_12">237 osób kupiło tę ofertę</span>
#     </div>
# </div>
# <div class="mpof_5r_x m7er_k4 _6a66d_-dvfo">
#     <button class="mgn2_14 mp0t_0a m9qz_yp mp7g_oh mqu1_24 mtsp_ib mli8_k4 m3h2_0 munh_0 m911_5r mefy_5r mnyp_5r mdwl_5r msbw_rf mldj_rf mtag_rf mm2b_rf mqvr_2 mqen_m6 meqh_en m0qj_5r msts_n7 mh36_16 mvrt_16 mg9e_8 mj7a_8 mjir_sv m2ha_2 m8qd_vz mjt1_n2 b19b6 mryx_8 mp4t_8 mse2_40 msa3_z4 mgmw_u5g mrmn_qo mrhf_u8 m31c_kb m0ux_fp b1xwt b1fea">
#         <span class="mpof_z0 _6a66d_mO-AV">do koszyka</span>
#         <span class="mpof_5r _6a66d_adCmP">dodaj do koszyka</span>
#     </button>
# </div></div></div>