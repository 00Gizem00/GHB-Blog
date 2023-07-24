import sqlite3



def get_data_from_db(query, params = tuple()):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    return rows




def get_post_by_slug(slug):
    rows = get_data_from_db('SELECT id, title, subtitle, slug, content, created_on FROM blogs WHERE slug = ?',(slug,))

    if len(rows) == 0:
        return None
    
    post = {
        'id': rows[0][0],
        'title': rows[0][1],
        'subtitle': rows[0][2],
        'slug': rows[0][3],
        'content': rows[0][4],
        'created_on': rows[0][5]
    }

    return post


def get_all_posts():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, subtitle, slug, created_on FROM blogs')
    rows = cursor.fetchall()

    posts = []
    for row in rows:
        posts.append(
            {
                'id': row[0],
                'title': row[1],
                'subtitle': row[2],
                'slug': row[3],
                'created_on': row[4]
            }
        )
    conn.close()
    return posts