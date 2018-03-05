import psycopg2


def popular_article(query1):
    conn = psycopg2.connect(database="news", host="localhost", user="vagrant")
    cur = conn.cursor()
    print("POPULAR ARTICLES ARE: \n")
    cur.execute(query1)
    result_set = cur.fetchall()
    for i in range(len(result_set)):
        title = result_set[i][0]
        views = result_set[i][1]
        print("%s--%d" % (title, views))
        cur.close()


def popular_author(query2):
    conn = psycopg2.connect(database="news", host="localhost", user="vagrant")
    cur = conn.cursor()
    print("\n")
    print("POPULAR AUTHORD ARE:\n")
    cur.execute(query2)
    result_set = cur.fetchall()
    for i in range(len(result_set)):
        author_name = result_set[i][0]
        views = result_set[i][1]
        print("%s--%d" % (author_name, views))
        cur.close()


def error(query3):
    conn = psycopg2.connect(database="news", host="localhost", user="vagrant")
    cur = conn.cursor()
    print("\n")
    print("DAYS ON WHICH THERE IS MORE THAN 1% ERROR:\n")
    cur.execute(query3)
    result_set = cur.fetchall()
    for i in range(len(result_set)):
        date = result_set[i][0]
        err = result_set[i][1]
        print("%s--%.1f %%" % (date, err))
        cur.close()


if __name__ == '__main__':
    query1 = "SELECT a.title,views \
              FROM articles a,article_view av \
              WHERE concat('/article/',a.slug)=av.article\
              ORDER BY views desc"
    query2 = "SELECT name,sum(tot) \
              FROM total_view \
              GROUP BY name ORDER BY sum desc"
    query3 = "SELECT * \
              FROM error_percentage \
              WHERE error>1"
    popular_article(query1)
    popular_author(query2)
    error(query3)
