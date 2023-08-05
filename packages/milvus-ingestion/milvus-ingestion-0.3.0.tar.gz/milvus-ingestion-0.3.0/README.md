# milvus-ingestion
A tool to help data ingestion for Milvus

## From source code
```commandline
git clone git@github.com:yhmo/milvus-ingestion.git
cd milvus-ingestion
pip3 install -r ./requirements.txt
```

## Installation
```commandline
pip3 install milvus-ingestion
```

## Requirement
python >= 3.7

## Usage
Assume you have created a collection in Milvus
```commandline
field1 = FieldSchema(name="book_id", dtype=DataType.INT64, is_primary=True, auto_id=False)
field2 = FieldSchema(name="book_intro", dtype=DataType.FLOAT_VECTOR, dim=_128)
field3 = FieldSchema(name="book_name", dtype=DataType.VARCHAR, max_length=64)
schema = CollectionSchema(fields=[field1, field2, field3])
collection = Collection(name="demo", schema=schema)
```

Use milvus_ingestion tool to help ingestion
```commandline
from milvus_ingestion import (
    IngestionType,
    DataBuffer,
)

data_buf = DataBuffer(ingestion_type=IngestionType.COLUMN_BASED)
data_buf.set_target_collection(collection_name="demo")

data_buf.append_row({
    "book_id": 1,
    "book_intro": [random.random() for _ in range(_128)],
    "book_name": "this is my first book",
})

data_buf.append_row({
    "book_id": 2,
    "book_intro": [random.random() for _ in range(_128)],
    "book_name": "this is my second book",
})

data_buf.persist()
task_id = data_buf.upload(clean=True)
```
