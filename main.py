from elasticsearch import Elasticsearch

client = Elasticsearch(
    "https://6cbcff10791f4ba69c2f72585fae4aaa.us-central1.gcp.cloud.es.io:443",
    api_key="SXQ1ZVFwSUJ4NTRHRWE2TDZBdmM6ZERGOWJZWVZTRHl0TDFpNU9xWTNiZw==",
)

# client.indices.create(index="my_index")

client.index(
    index="film_index",
    id="1",
    document={
        "name": "toy story",
        "descriprion": "В спальне Энди его игрушки начинают жить своей жизнью, как только он выходит из комнаты. В день рождения мальчика царит паника — все боятся появления новой игрушки, которая перетянет внимание на себя. И только любимчик Эдди, ковбой Вуди, ни о чем не переживает. Однако, когда мальчик получает в подарок фигурку астронавта Базза Лайтера, Вуди очень быстро оказывается забыт. И тогда ковбой решает вернуть себе первое место в сердце Энди.",
    }
)

# ans = client.get(index="my_index", id="my_document_id1")

res = client.search(index="film_index", query={
    "match": {
        "name" : "story"
    }
})

# client.delete(index="my_index", id="my_document_id")

print(res)