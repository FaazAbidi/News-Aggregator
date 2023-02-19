import datetime
from enum import Enum

class ApiSource(Enum):
    '''
    This is an enum for the api sources
    '''
    NEWSAPI = 'newsapi'
    REDDIT = 'reddit'

class HelperService:
    
    @staticmethod
    def convertDateTimeStringToDatetime(datetime_string: str, api_source: ApiSource):
        '''
        This method converts a datetime string from reddit to a datetime object
        '''
        try:
            if api_source == ApiSource.REDDIT:
                return datetime.datetime.strptime(datetime_string ,'%Y-%m-%d %H:%M:%S').replace(tzinfo=datetime.timezone.utc)
            elif api_source == ApiSource.NEWSAPI:
                return datetime.datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
            else:
                print("Invalid api source")
                return None
        except ValueError as e:
            print("Error converting datetime string to datetime object: ", e)
            return None