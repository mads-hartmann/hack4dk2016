class Picture(object):
    def __init__(self, picture_id):
        self.picture_id = picture_id

    @property
    def image_url(self):
        return '/static/images/{}.jpg'.format(str(self.picture_id).zfill(4))


class Person(object):
    def __init__(self, first_name, picture_id):
        self.first_name = first_name
        self.picture_id = picture_id
        self.image_url = '/static/images/{}.jpg'.format(str(picture_id).zfill(4))


def random_pictures(cnx, count):
    cursor = cnx.cursor(prepared=True)

    cursor.execute("""
        SELECT picture_id
        FROM hack4dk2016.person
        ORDER BY RAND()
        LIMIT %s
    """, (count, ))

    for row in cursor.fetchall():
        (picture_id,) = row
        yield Picture(picture_id)

    cursor.close()


def with_last_name(cnx, last_name):
    cursor = cnx.cursor(prepared=True)

    cursor.execute("""
        SELECT first_name, picture_id
        FROM hack4dk2016.person
        WHERE LOWER(last_name) = LOWER(%s)
    """, (last_name, ))

    for row in cursor.fetchall():
        (first_name, picture_id) = row
        yield Person(
            first_name.decode("utf-8"),
            picture_id)

    cursor.close()


def with_first_name(cnx, first_name):
    cursor = cnx.cursor(prepared=True)

    cursor.execute("""
        SELECT first_name, picture_id
        FROM hack4dk2016.person
        WHERE LOWER(first_name) = LOWER(%s)
    """, (first_name, ))

    for row in cursor.fetchall():
        (first_name, picture_id) = row
        yield Person(
            first_name.decode("utf-8"),
            picture_id)

    cursor.close()


def with_picture_id(cnx, picture_id):
    cursor = cnx.cursor(prepared=True)

    cursor.execute("""
        SELECT first_name, picture_id
        FROM hack4dk2016.person
        WHERE picture_id = %s
    """, (picture_id, ))

    for row in cursor.fetchall():
        (first_name, picture_id) = row
        yield Person(
            first_name.decode("utf-8"),
            picture_id)

    cursor.close()


def all_last_names(cnx):
    cursor = cnx.cursor(prepared=True)

    cursor.execute("""
         SELECT
            DISTINCT(last_name),
            COUNT(*) as count
        FROM hack4dk2016.person
        WHERE last_name <> ''
        GROUP BY last_name
        ORDER BY count desc, last_name desc;
    """)

    for row in cursor.fetchall():
        (last_name, count) = row
        yield (last_name.decode("utf-8"), count)

    cursor.close()


def all_first_names(cnx):
    cursor = cnx.cursor(prepared=True)

    cursor.execute("""
         SELECT
            DISTINCT(first_name),
            COUNT(*) as count
        FROM hack4dk2016.person
        WHERE first_name <> ''
        GROUP BY first_name
        ORDER BY count desc, first_name desc;
    """)

    for row in cursor.fetchall():
        (first_name, count) = row
        yield (first_name.decode("utf-8"), count)

    cursor.close()
