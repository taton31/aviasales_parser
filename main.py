import requests
import datetime
import time
import telebot
from notifiers import get_notifier

token = '7062094367:AAGwm9ThvvtISXa7iTNYWN-cYyehh-Z7RHM'
chatId = 603616360
chatId2 = 1723464345
bot = telebot.TeleBot(token)

def send_message(message):
    telegram = get_notifier('telegram')
    try:
        telegram.notify(token=token, chat_id=chatId, message=message)
        telegram.notify(token=token, chat_id=chatId2, message=message)
    except:
        print('Could not send message')
        
def req(date):
    aaa = ['16m9g', '48n5d', '1k7fo', '1q1xf', '1zkas', '498fl', '2zok6', '36k57']
    def get_timestamp():
        ct = datetime.datetime.now()
        return int(ct.timestamp())

    session = requests.Session()

    cookies = {
        'auid': 'bkhwMmbDISZINmhoeHItAg==',
        '_sp_ses.dc27': '*',
        'marker': 'google',
        'currency': 'RUB',
        'nuid': '78a9daaa-9164-4421-8f60-224839602e7b',
        '_gcl_au': '1.1.1920805983.1724064045',
        '_gid': 'GA1.2.1724581604.1724064046',
        'tmr_lvid': '828ea448193311091dd7bef35a5dcb39',
        'tmr_lvidTS': '1724064045758',
        '_ym_uid': '1724064046473175310',
        '_ym_d': '1724064046',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'uncheck_hotel_cookie': 'true',
        '_clck': 'ojpt8q%7C2%7Cfog%7C0%7C1692',
        'uxs_uid': 'a5874860-5e17-11ef-b036-a5aae06eefbf',
        '_dc_gtm_UA-1481416-4': '1',
        '_clsk': '1fcxab8%7C1724064892740%7C3%7C0%7Cp.clarity.ms%2Fcollect',
        '_ga': 'GA1.2.547603777.1724064046',
        '_ga_KD6Y7CZ85S': 'GS1.2.1724064046.1.1.1724064900.29.0.0',
        '_ga_EVCZWTNN22': 'GS1.1.1724064045.1.1.1724064912.0.0.0',
        '_ga_GCLPS5EN9Q': 'GS1.1.1724064046.1.1.1724064912.17.0.0',
        'search_init_stamp': '1724064917286',
        '_sp_id.dc27': 'dc29294f-9ccb-4274-b5d1-c41b6cc3b0d8.1724064043.1.1724064920..915ef53a-07fe-49c8-a748-410d8eaf0546..aa94bf0a-28bd-48f8-a998-6d4c40f1bc17.1724064043495.133',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9',
        'authorization': '',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'auid=bkhwMmbDISZINmhoeHItAg==; _sp_ses.dc27=*; marker=google; currency=RUB; nuid=78a9daaa-9164-4421-8f60-224839602e7b; _gcl_au=1.1.1920805983.1724064045; _gid=GA1.2.1724581604.1724064046; tmr_lvid=828ea448193311091dd7bef35a5dcb39; tmr_lvidTS=1724064045758; _ym_uid=1724064046473175310; _ym_d=1724064046; _ym_isad=2; _ym_visorc=b; uncheck_hotel_cookie=true; _clck=ojpt8q%7C2%7Cfog%7C0%7C1692; uxs_uid=a5874860-5e17-11ef-b036-a5aae06eefbf; _dc_gtm_UA-1481416-4=1; _clsk=1fcxab8%7C1724064892740%7C3%7C0%7Cp.clarity.ms%2Fcollect; _ga=GA1.2.547603777.1724064046; _ga_KD6Y7CZ85S=GS1.2.1724064046.1.1.1724064900.29.0.0; _ga_EVCZWTNN22=GS1.1.1724064045.1.1.1724064912.0.0.0; _ga_GCLPS5EN9Q=GS1.1.1724064046.1.1.1724064912.17.0.0; search_init_stamp=1724064917286; _sp_id.dc27=dc29294f-9ccb-4274-b5d1-c41b6cc3b0d8.1724064043.1.1724064920..915ef53a-07fe-49c8-a748-410d8eaf0546..aa94bf0a-28bd-48f8-a998-6d4c40f1bc17.1724064043495.133',
        'origin': 'https://www.aviasales.ru',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.aviasales.ru/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-aws-waf-token': '3ae8a26c-1852-4620-99c9-fa3668aa7e08:DQoAYVBMcJISAQAA:CliMtRQJOsfQ6wjBuxIILn3P3FVzK9n1SXdStx2vMbthjlUPvahDD52FmhtWCujCLfUGuWuiRYnm4/UcVmiQmJLNOtw2uO0EK2ZcDgeEMDagduep3CMoJKFvse8m0zQ9gIgDa3RB3b0cQXwKfOGrV/ecL0Pm/bmc2jIlwlzHOIg2DsfX0oOgvaW7r5YxDI70iGvJPJd/dRqoqkdRUu7mQu2vWY+lGSTAZIA9kWWYeeoC+QJo0/GK0qGLSFccPb314ROZgIZ/DQ==',
        'x-client-type': 'web',
        'x-origin-cookie': 'auid=bkhwMmbDISZINmhoeHItAg==; _sp_ses.dc27=*; marker=google; currency=RUB; nuid=78a9daaa-9164-4421-8f60-224839602e7b; _awt=463612396843306624f936336e2365393667ab33632e3934-62f68623f5d9330557b33b623dc03e17; _gcl_au=1.1.1920805983.1724064045; _gid=GA1.2.1724581604.1724064046; tmr_lvid=828ea448193311091dd7bef35a5dcb39; tmr_lvidTS=1724064045758; _ym_uid=1724064046473175310; _ym_d=1724064046; _ym_isad=2; _ym_visorc=b; domain_sid=rxjqUesfZij85ADwtkWcG%3A1724064047093; uncheck_hotel_cookie=true; currency=rub; _clck=ojpt8q%7C2%7Cfog%7C0%7C1692; _yoid=de9b6f19-25f0-4dbd-9ee3-00a8e2af96e9; _yosid=d936e9bc-76b8-4bc9-9750-a607e777eed8; uxs_uid=a5874860-5e17-11ef-b036-a5aae06eefbf; _dc_gtm_UA-1481416-4=1; _clsk=1fcxab8%7C1724064892740%7C3%7C0%7Cp.clarity.ms%2Fcollect; tmr_detect=0%7C1724064893619; _ga=GA1.2.547603777.1724064046; _ga_KD6Y7CZ85S=GS1.2.1724064046.1.1.1724064900.29.0.0; aws-waf-token=3ae8a26c-1852-4620-99c9-fa3668aa7e08:DQoAYVBMcJISAQAA:CliMtRQJOsfQ6wjBuxIILn3P3FVzK9n1SXdStx2vMbthjlUPvahDD52FmhtWCujCLfUGuWuiRYnm4/UcVmiQmJLNOtw2uO0EK2ZcDgeEMDagduep3CMoJKFvse8m0zQ9gIgDa3RB3b0cQXwKfOGrV/ecL0Pm/bmc2jIlwlzHOIg2DsfX0oOgvaW7r5YxDI70iGvJPJd/dRqoqkdRUu7mQu2vWY+lGSTAZIA9kWWYeeoC+QJo0/GK0qGLSFccPb314ROZgIZ/DQ==; _ga_EVCZWTNN22=GS1.1.1724064045.1.1.1724064912.0.0.0; _ga_GCLPS5EN9Q=GS1.1.1724064046.1.1.1724064912.17.0.0; search_init_stamp=1724064917286; _sp_id.dc27=dc29294f-9ccb-4274-b5d1-c41b6cc3b0d8.1724064043.1.1724064919..915ef53a-07fe-49c8-a748-410d8eaf0546..aa94bf0a-28bd-48f8-a998-6d4c40f1bc17.1724064043495.132',
    }

    json_data = {
        'search_params': {
            'directions': [
                {
                    'origin': 'MOW',
                    'destination': 'HKT',
                    'date': date,
                    'is_origin_airport': False,
                    'is_destination_airport': False,
                },
            ],
            'passengers': {
                'adults': 1,
                'children': 0,
                'infants': 0,
            },
            'trip_class': 'Y',
        },
        'client_features': {
            'direct_flights': True,
            'brand_ticket': False,
            'top_filters': True,
            'badges': False,
            'tour_tickets': True,
            'assisted': True,
        },
        'market_code': 'ru',
        'marker': 'google',
        'citizenship': 'RU',
        'currency_code': 'rub',
        'languages': {
            'ru': 1,
        },
        'debug': {
            'experiment_groups': {
                'usc-exp-marketChangeOfferForeigners': 'treatment',
                'usc-exp-authByPhone': 'off',
                'ex-exp-webTabbar': 'form',
                'asb-exp-biletixSearchEngine': 'off',
                'asb-exp-flexibleBookingPricing': 'off',
                'serp-exp-nativeSharing': 'on',
                'serp-exp-bletFlightInfo': 'on',
                'serp-exp-bletInformers': 'on',
                'serp-exp-bletItinerary': 'on',
                'avs-exp-downgradedGates': 'on',
                'serp-exp-hotelsSearchAutostart': 'on_without_tooltip',
                'asb-exp-biletix-sbp': 'on',
                'usc-exp-subscriptionLoginFlowWeb': 'treatment',
                'serp-exp-aa3': 'off',
                'serp-exp-hotelsMainAdPlacement': 'on',
                'avs-exp-foreignCards': 'on',
                'serp-exp-bletProposalsModal': 'on',
                'serp-exp-savedFilters': 'on',
                'usc-exp-showSupportLinkNavbar': 'enabled',
                'usc-exp-priceAlertSubscriptionOnExplore': 'treatment',
                'serp-exp-aa2': 'off',
                'avs-exp-comparisonWidget': 'on',
                'avs-exp-directTicketsScheduleV3': 'on',
                'usc-exp-faqSearch': 'off',
                'guides-exp-feed': 'on',
                'serp-exp-disableSeatsAmenitiesFlightInfo': 'on',
                'asb-exp-additionalServicesOnContactForm': 'control',
                'serp-exp-faresV2': 'on',
                'asb-exp-smsPricing': 'off',
                'serp-exp-hotelPreviewV2': 'on',
                'guides-exp-newPinSizes': 'on',
                'serp-exp-predictionSearch': 'on',
                'usc-exp-menuSupportSection': 'on',
                'guides-exp-trapHeader': 'expanded_top',
                'serp-exp-ticketProductBanner': 'on',
                'serp-exp-hotelsResults': 'native.test',
                'serp-exp-aws-waf': 'active_with_async_loading_enabled_v2',
                'asb-exp-migrateAssistedToSelene': 'enabled',
                'usc-exp-marketChangeOfferWidget': 'on',
                'avs-exp-aa': 'on',
                'ex-exp-newWebAutocomplete': 'iteration-1',
                'serp-exp-hotelsTooltipMention': 'on',
                'serp-exp-uxFeedback': 'on',
                'serp-exp-faresFilters': 'on',
                'asb-exp-refund90Pricing': 'off',
                'usc-exp-emailSubscriptionForm': 'footer_form',
                'usc-exp-ssrInstructions': 'on',
                'prem-exp-newMarketsMain': 'off',
                'ex-exp-directionScreenWithTickets': 'it4-poi-uber-psgr',
                'serp-exp-hotelsAutocomplete': 'on_new_backend',
                'serp-exp-modalDirectFlights': 'off',
                'asb-exp-servicesInFares': 'off',
                'serp-exp-sessionStartUxFeedback': 'on_desktop',
                'serp-exp-ticketPreviewV3': 'on',
                'ex-exp-mainCityVideo': 'several_videos',
                'serp-exp-hotels': 'on_prod_with_trap_entry_point',
            },
        },
        'brand': 'AS',
        'search_source': 'search_form',
    }

    response = session.post('https://tickets-api.aviasales.ru/search/v2/start', cookies=cookies, headers=headers, json=json_data)
    try:
        search_id = response.json()['search_id']
    except:
        print(response.text)
        exit()
    print (search_id)
    # print (response.json()['search_id'])

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"search_params":{"directions":[{"origin":"MOW","destination":"HKT","date":"2024-12-23","is_origin_airport":false,"is_destination_airport":false}],"passengers":{"adults":1,"children":0,"infants":0},"trip_class":"Y"},"client_features":{"direct_flights":true,"brand_ticket":false,"top_filters":true,"badges":false,"tour_tickets":true,"assisted":true},"market_code":"ru","marker":"google","citizenship":"RU","currency_code":"rub","languages":{"ru":1},"debug":{"experiment_groups":{"usc-exp-marketChangeOfferForeigners":"treatment","usc-exp-authByPhone":"off","ex-exp-webTabbar":"form","asb-exp-biletixSearchEngine":"off","asb-exp-flexibleBookingPricing":"off","serp-exp-nativeSharing":"on","serp-exp-bletFlightInfo":"on","serp-exp-bletInformers":"on","serp-exp-bletItinerary":"on","avs-exp-downgradedGates":"on","serp-exp-hotelsSearchAutostart":"on_without_tooltip","asb-exp-biletix-sbp":"on","usc-exp-subscriptionLoginFlowWeb":"treatment","serp-exp-aa3":"off","serp-exp-hotelsMainAdPlacement":"on","avs-exp-foreignCards":"on","serp-exp-bletProposalsModal":"on","serp-exp-savedFilters":"on","usc-exp-showSupportLinkNavbar":"enabled","usc-exp-priceAlertSubscriptionOnExplore":"treatment","serp-exp-aa2":"off","avs-exp-comparisonWidget":"on","avs-exp-directTicketsScheduleV3":"on","usc-exp-faqSearch":"off","guides-exp-feed":"on","serp-exp-disableSeatsAmenitiesFlightInfo":"on","asb-exp-additionalServicesOnContactForm":"control","serp-exp-faresV2":"on","asb-exp-smsPricing":"off","serp-exp-hotelPreviewV2":"on","guides-exp-newPinSizes":"on","serp-exp-predictionSearch":"on","usc-exp-menuSupportSection":"on","guides-exp-trapHeader":"expanded_top","serp-exp-ticketProductBanner":"on","serp-exp-hotelsResults":"native.test","serp-exp-aws-waf":"active_with_async_loading_enabled_v2","asb-exp-migrateAssistedToSelene":"enabled","usc-exp-marketChangeOfferWidget":"on","avs-exp-aa":"on","ex-exp-newWebAutocomplete":"iteration-1","serp-exp-hotelsTooltipMention":"on","serp-exp-uxFeedback":"on","serp-exp-faresFilters":"on","asb-exp-refund90Pricing":"off","usc-exp-emailSubscriptionForm":"footer_form","usc-exp-ssrInstructions":"on","prem-exp-newMarketsMain":"off","ex-exp-directionScreenWithTickets":"it4-poi-uber-psgr","serp-exp-hotelsAutocomplete":"on_new_backend","serp-exp-modalDirectFlights":"off","asb-exp-servicesInFares":"off","serp-exp-sessionStartUxFeedback":"on_desktop","serp-exp-ticketPreviewV3":"on","ex-exp-mainCityVideo":"several_videos","serp-exp-hotels":"on_prod_with_trap_entry_point"}},"brand":"AS","search_source":"show_all_tickets"}'
    #response = requests.post('https://tickets-api.aviasales.ru/search/v2/start', cookies=cookies, headers=headers, data=data)




    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.aviasales.ru',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.aviasales.ru/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-client-type': 'web',
    }


    from random import sample, shuffle

    rr = '1234567890qwertyuiopasdfghjklzxcvbnm'
    i=0

    while True:
        i += 1
        shuffle(aaa)
        json_data = {
            'search_id': search_id,
            'rnd': aaa[0],
            # 'rnd': ''.join(sample(rr,len(rr)))[0:5],
            'last_update_timestamp': get_timestamp(),
            'order': 'best',
            'limit': 10,
            'price_per_person': False,
            'search_by_airport': False,
            'filters': {},
            'prechecked_filters': {},
        }

        response = session.post('https://tickets-api.eu-central-1.aviasales.ru/search/v3/results', headers=headers, json=json_data)
        
        mina = 9999999
        if response.text:
            js = response.json()[0]
            for ticket in js['tickets']:
                mina = min(mina, int(ticket['proposals'][0]['price']['value']))
            print(mina)
        else:
            print('oooops')

        
        time.sleep(5)

        if i > 5:
            return mina

while True:
    dates = ['2024-12-23', '2024-12-24', '2024-12-25', '2024-12-26', '2024-12-27', '2024-12-28', '2024-12-29']
    dic = {}
    for i in dates:
        z = req(i)
        if dic.get(i, 9999999) > z:
            if dic.get(i, 9999999) != 9999999:
                send_message(f'обновилась минимальная цена на {i}:{z}')
            dic[i] = z
        time.sleep(30)

    print(dic)
    with open('res.txt', 'w') as f:
        f.write(str(dic))

    time.sleep(5*60)
    