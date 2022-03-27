from pickle import dumps, loads
from datetime import datetime
from tagcounter.db import cursor, con
from urllib.parse import urlparse


def create(url, tags_dictionary):
    parsed_url = urlparse(url)
    cursor.execute(f"INSERT INTO tags_info VALUES (?, ?, ?, ?);", (parsed_url.netloc, url, datetime.now().isoformat(), dumps(tags_dictionary)))
    con.commit()


def get_by_url(url):
    found_entity = cursor.execute("SELECT * FROM tags_info WHERE url=?;", [url]).fetchone()
    if found_entity is None:
        return
    url_dict = loads(found_entity[3])

    return found_entity[:-1] + (url_dict,)

