import random

from pymilvus import connections, CollectionSchema, FieldSchema, DataType, Collection, utility

if __name__ == '__main__':
    connections.connect(
        alias="default",
        user='username',
        password='password',
        host='localhost',
        port='19530'
    )
    # book_id = FieldSchema(
    #     name="book_id",
    #     dtype=DataType.INT64,
    #     is_primary=True,
    # )
    # book_name = FieldSchema(
    #     name="book_name",
    #     dtype=DataType.VARCHAR,
    #     max_length=200,
    #     # The default value will be used if this field is left empty during data inserts or upserts.
    #     # The data type of `default_value` must be the same as that specified in `dtype`.
    #     default_value="Unknown"
    # )
    # word_count = FieldSchema(
    #     name="word_count",
    #     dtype=DataType.INT64,
    #     # The default value will be used if this field is left empty during data inserts or upserts.
    #     # The data type of `default_value` must be the same as that specified in `dtype`.
    #     default_value=9999
    # )
    # book_intro = FieldSchema(
    #     name="book_intro",
    #     dtype=DataType.FLOAT_VECTOR,
    #     dim=2
    # )
    # schema = CollectionSchema(
    #     fields=[book_id, book_name, word_count, book_intro],
    #     description="Test book search",
    #     enable_dynamic_field=True
    # )
    # collection_name = "book"
    # collection = Collection(
    #     name=collection_name,
    #     schema=schema,
    #     using='default',
    #     shards_num=2
    # )

    # data = [
    #     [i for i in range(2000)],
    #     [str(i) for i in range(2000)],
    #     [i for i in range(10000, 12000)],
    #     [[random.random() for _ in range(2)] for _ in range(2000)],
    #     # use `default_value` for a field
    #     # [],
    #     # or
    #     # None,
    #     # or just omit the field
    # ]

    # Once your collection is enabled with dynamic schema,
    # you can add non-existing field values.
    # data.append([str("dy" * i) for i in range(2000)])

    # Once your collection is enabled with dynamic schema,
    # you can add non-existing field values.

    # collection = Collection("book")  # Get an existing collection.
    # mr = collection.insert(data)

    # index_params = {
    #     "metric_type": "L2",
    #     "index_type": "IVF_FLAT",
    #     "params": {"nlist": 1024}
    # }
    # collection.create_index(
    #     field_name="book_intro",
    #     index_params=index_params
    # )

    # utility.index_building_progress("book")

    collection = Collection("book")  # Get an existing collection.
    collection.load()
    search_params = {
        "metric_type": "L2",
        "offset": 5,
        "ignore_growing": False,
        "params": {"nprobe": 10}
    }
    results = collection.search(
        data=[[0.1, 0.2]],
        anns_field="book_intro",
        # the sum of `offset` in `param` and `limit`
        # should be less than 16384.
        param=search_params,
        limit=10,
        expr=None,
        # set the names of the fields you want to
        # retrieve from the search result.
        output_fields=['book_name'],
        consistency_level="Strong"
    )

    # get the IDs of all returned hits
    results[0].ids

    # get the distances to the query vector from all returned hits
    results[0].distances

    # get the value of an output field specified in the search request.
    hit = results[0][0]
    hit.entity.get('book_name')
    results[0].ids
    results[0].distances
    collection.release()
    connections.disconnect("default")
