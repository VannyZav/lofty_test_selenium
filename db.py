import os

import psycopg2


password = os.getenv('DB_PASSWORD')
conn = psycopg2.connect(
    """dbname=lofty_parser
    user=postgres
    port=5433
    host=127.0.0.1
    password="""+password)

cur = conn.cursor()


def insert_data(channel_username, video_href, video_id):
    sql = """INSERT INTO youtube_channel_data (channel_username, 
    video_href, video_id) VALUES (%s, %s, %s) ON CONFLICT (video_href) DO NOTHING;"""
    cur.execute(sql, (channel_username, video_href, video_id))
    # conn.commit()


# cur.close()
# conn.close()
