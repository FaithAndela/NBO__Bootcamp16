import query

def query_hokoasavings():
    client = bigquery.Client()
    query_results = client.run_sync_query("""
        SELECT
            APPROX_TOP_COUNT(corpus, 10) as title,
            COUNT(*) as unique_words
        FROM `publicdata.samples.hokoasavings`;""")

    
    query_results.use_legacy_sql = False

    query_results.run()

    
    page_token = None

    while True:
        rows, total_rows, page_token = query_results.fetch_data(
            max_results=10,
            page_token=page_token)

        for row in rows:
            print(row)

        if not page_token:
            break


if __name__ == '__main__':
    query_hokoasavings()