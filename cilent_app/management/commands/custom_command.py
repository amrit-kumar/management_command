from django.core.management.base import BaseCommand, CommandError
from cilent_app.models import Api
import requests
from urllib.request import urlopen


class Command(BaseCommand):
    help = 'Downloads the specific pdf at given url'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('filingDatetimeFrom', nargs='?', default='2014-01-01')
        parser.add_argument('filingDatetimeTo', nargs='?')

    def handle(self, *args, **options):
        from_date = ''
        to_date = ''
        my_argument = options['filingDatetimeFrom']
        my_argument2 = options['filingDatetimeTo']

        try:
            if my_argument == 'filingDatetimeFrom':
                from_date = '2014-01-01'
            if my_argument2 == 'filingDatetimeTo':
                to_date = '2017-01-01'
        except:
            raise CommandError('Date does not exist')

        url = 'https://ptabdata.uspto.gov/ptab-api/documents/?filingDatetimeFrom=' + from_date + '&filingDatetimeTo=' + to_date
        response = requests.get(url, timeout=5, verify=False)
        for i in (response.json()['results']):
            for j in i['links']:
                if j['rel'] == 'download':
                    download_url = j['href']
                    download_response = requests.get(download_url, verify=False, stream=True)
                    print("download_response url", download_response.url)

                    filename = str(download_response.url).split('/')[4] + '_' + str(download_response.url).split('/')[
                        5] + '_' + str(download_response.url).split('/')[6] + '.pdf'
                    with open(filename, 'wb') as f:
                        f.write(download_response.content)

        filename = 'response.txt '
        with open(filename, 'w') as f:
            f.write(response.text)
