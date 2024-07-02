import pandas as pd
import logging
import logging
import pandas as pd
import numpy as np
import datetime
from string_grouper import match_strings, match_most_similar, \
	group_similar_strings, compute_pairwise_similarities, \
	StringGrouper
from timeit import default_timer as timer
from soundshapecode import ssc
SSC_ENCODE_WAY = 'SHAPE'  # 'ALL','SOUND','SHAPE'
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)
logging.basicConfig(level=logging.DEBUG)

demo_file = 'C://git//ssc//corp.csv'
wc_sanction = pd.read_csv(demo_file, encoding='utf-8')
print("sanction with rows", len(wc_sanction))
wc_sanction['enterprise_name_code'] = wc_sanction['enterprise_name'].apply(lambda x: str(ssc.getSSC(x, SSC_ENCODE_WAY)))

wc_sanction.to_csv('C://git//ssc//wc_sanction-code.csv')

request_file= 'C://git//ssc//cn_request_corps.csv'
requests = pd.read_csv(request_file, encoding='utf-8')
print("request with rows", len(requests))
requests['RequestNameCode'] = requests['RequestName'].apply(lambda x: str(ssc.getSSC(x, SSC_ENCODE_WAY)))

requests.to_csv('C://git//ssc//requests-code.csv')


enterprise_matches = match_strings(wc_sanction['enterprise_name_code'], requests['RequestNameCode'],
							   master_id = wc_sanction['enterprise_id'] ,
							   duplicates_id = requests['RequestId'] ,
							   ignore_index=True, min_similarity = 0.6)

enterprise_matches.to_csv('C://git//ssc//enterprise_matches.csv')
