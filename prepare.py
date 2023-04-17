import numpy as np
import pandas as pd

def explore_df():
    '''
    This function will import the games.csv made during the acquire phase and prepare it for exploration
    '''
    df=pd.read_csv('games.csv')
    df.drop(columns=['url', 'bga_edit_url', 'template_url', 'discount', 'thumb_url', 'image_url',
                    'official_url', 'historical_low_prices', 'is_historical_low', 'skus', 'edit_url',
                    'images', 'msrps', 'sku_objects', 'tags', 'msrp_text', 'price_text', 'trending_rank',
                    'price_ca', 'price_uk', 'price_au', 'player_counts', 'players', 'playtime',
                    'visits', 'lists', 'mentions', 'links', 'plays', 'developers', 'related_to',
                    'related_as', 'names', 'comment_count', 'description', 'specs', 'handle', 'active',
                    'listing_clicks', 'size_width', 'store_images_url', 'sell_sheet_url', 'cs_rating', 'availability_status',
                    'video_links', 'isbn', 'upc', 'sku', 'size_units', 'size_depth', 'size_height',
                    'weight_units', 'weight_amount', 'rules_url', 'matches_specs', 'faq', 'commentary',
                    'mechanics', 'categories', 'publishers', 'designers', 'primary_publisher', 'primary_designer',
                    'artists', 'description_preview','amazon_rank'], inplace=True)
    df['msrp']= df['msrp'].fillna(47.43)
    df=df.drop([597, 631, 901, 558, 977])
    years=[2013, 2009, 2018, 2013, 2012, 2010, 2007, 2017, 2012, 2012, 1981, 2010, 2015]
    for y in years:
        df['year_published'].fillna(y, limit=1, inplace=True)
    ages= [12, 12, 13]
    for y in ages:
        df['min_age'].fillna(y, limit=1, inplace=True)
    for i, row in df.iterrows():
        if row['price'] == 0:
            new_price = row['msrp'] * 1.0956
            df.at[i, 'price'] = new_price 
    return df