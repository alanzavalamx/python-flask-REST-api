
from settings import user, pwd

print( 'postgresql+psycopg2://admin:%(pwd)s@192.6.9.154:5432/dbtest'.format(user=user, pwd=pwd,))