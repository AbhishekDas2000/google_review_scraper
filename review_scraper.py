# import json
import pandas as pd
from tqdm import tqdm

# from pygments import highlight
# from pygments.lexers import JsonLexer
# from pygments.formatters import TerminalFormatter

from google_play_scraper import Sort, reviews, app

app_packages = ['com.saveo.saveomedical','com.ionicframework.mobilemfp973648','com.medikabazaar.app','wholesalemedical.in','com.growthaccel.pharmarack_retailer','com.retailio.retailerapp']
app_reviews = []

for ap in tqdm(app_packages):
    for score in list(range(1, 6)):
        for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
            rvs, _ = reviews(
                ap,
                lang='en',
                country='us',
                sort=sort_order,
                # count=200 if score == 3 else 100,
                count=400,
                filter_score_with=score
            )
            for r in rvs:
                rem_list = ['reviewId','userName','userImage','reviewCreatedVersion','at','replyContent','repliedAt']
                r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
                r['appId'] = ap
                [r.pop(key) for key in rem_list]
            app_reviews.extend(rvs)


# def print_json(json_object):
#     json_str = json.dumps(
#         json_object,
#         indent=2,
#         sort_keys=True,
#         default=str
#     )
#     print(highlight(json_str, JsonLexer(), TerminalFormatter()))


# print_json(app_infos[0])

# app_infos_df = pd.DataFrame(app_infos)
# app_infos_df.to_csv('apps.csv', index=None, header=True)

app_reviews_df = pd.DataFrame(app_reviews)
app_reviews_df.to_excel('reviews.xlsx', index=None, header=True)
