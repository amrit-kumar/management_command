from django.core.management.base import BaseCommand, CommandError
from cilent_app.models import Api
import requests



class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('filingDatetimeFrom', nargs='?',default='2014-01-01')
        parser.add_argument('filingDatetimeTo', nargs='?')



    def handle(self, *args, **options):
        from_date=''
        to_date=''
        my_argument = options['filingDatetimeFrom']
        my_argument2 = options['filingDatetimeTo']

        try:
            if my_argument=='filingDatetimeFrom':
                from_date='2014-01-01'
            if my_argument2 == 'filingDatetimeTo':
                to_date='2017-01-01'
        except :
            raise CommandError('Date does not exist' )

        url = 'https://ptabdata.uspto.gov/ptab-api/documents/?filingDatetimeFrom=' + from_date +'&filingDatetimeTo='+to_date
        response = requests.get(url,timeout=5, verify=False)
        filename='response.txt '
        with open(filename,'w') as f:
            f.write(response.text)

