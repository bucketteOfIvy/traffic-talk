### Author: Ashlynn Wimer
### Date: 5/6/2024
### About: This script is used to pull traffic data from Chicago Public Data
###        portal in preparation for a lightning talk on the afterlife of 
###        redlining.
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

URL = 'https://data.cityofchicago.org/resource/85ca-t3if.csv?$query=SELECT%0A%20%20%60crash_record_id%60%2C%0A%20%20%60crash_date%60%2C%0A%20%20%60posted_speed_limit%60%2C%0A%20%20%60traffic_control_device%60%2C%0A%20%20%60device_condition%60%2C%0A%20%20%60weather_condition%60%2C%0A%20%20%60lighting_condition%60%2C%0A%20%20%60first_crash_type%60%2C%0A%20%20%60trafficway_type%60%2C%0A%20%20%60lane_cnt%60%2C%0A%20%20%60alignment%60%2C%0A%20%20%60roadway_surface_cond%60%2C%0A%20%20%60road_defect%60%2C%0A%20%20%60report_type%60%2C%0A%20%20%60crash_type%60%2C%0A%20%20%60intersection_related_i%60%2C%0A%20%20%60private_property_i%60%2C%0A%20%20%60hit_and_run_i%60%2C%0A%20%20%60damage%60%2C%0A%20%20%60date_police_notified%60%2C%0A%20%20%60prim_contributory_cause%60%2C%0A%20%20%60sec_contributory_cause%60%2C%0A%20%20%60street_no%60%2C%0A%20%20%60street_direction%60%2C%0A%20%20%60street_name%60%2C%0A%20%20%60beat_of_occurrence%60%2C%0A%20%20%60photos_taken_i%60%2C%0A%20%20%60statements_taken_i%60%2C%0A%20%20%60dooring_i%60%2C%0A%20%20%60work_zone_i%60%2C%0A%20%20%60work_zone_type%60%2C%0A%20%20%60workers_present_i%60%2C%0A%20%20%60num_units%60%2C%0A%20%20%60most_severe_injury%60%2C%0A%20%20%60injuries_total%60%2C%0A%20%20%60injuries_fatal%60%2C%0A%20%20%60injuries_incapacitating%60%2C%0A%20%20%60injuries_non_incapacitating%60%2C%0A%20%20%60injuries_reported_not_evident%60%2C%0A%20%20%60injuries_no_indication%60%2C%0A%20%20%60injuries_unknown%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60%0AORDER%20BY%20%60crash_date%60%20DESC%20NULL%20FIRST%2C%20%60crash_record_id%60%20ASC%20NULL%20LAST'

def pull_batch(lst, batch_num, batch_size=50000):
    '''
    Pull bunch of data and append it to a list of pds.
    '''
    df = pd.read_csv(f'{URL}%20LIMIT%20{batch_size}%20OFFSET%20{batch_num*batch_size}')
    lst.append(df)

pds = []
with ThreadPoolExecutor(7) as executor:
    for i in range(17):
        executor.submit(pull_batch, pds, i)    

df = pd.concat(pds, ignore_index=True).drop_duplicates()

df.to_csv('../../data/crash_data.csv')