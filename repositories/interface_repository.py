import json
import certifi
import pymongo
from bson import ObjectId, DBRef

from typing import Generic, TypeVar, get_args


T = TypeVar('T')

# TODO add dta validations and error control


class InterfaceRepository(Generic[T]):
    def __init__(self):
        #connect db

        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            data_config.get("db_connection"),
            tlsCAFile=ca
        )
        self.data_base = client[data_config.get("db_name")]
        model_class = get_args(self.__orig__bases__[0])
        self.collection = model_class[0].__name__.lower()

    def load_file_config(self):
        with open("config.json", "r") as config:
            data = json.load(config)
        return data

    def find_all(self) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find({}):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def find_by_id(self, id_:str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        document = current_collection.find_one({'_id':_id})
        document = self.get_values.db_ref(document)
        if document:
            document['_id']=document['id'].__str__()
        else:
            document = {}

    def save(self, item:T) -> T:
        current_collection = self.data_base[self.collection]
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            id_ = item._id
            _id = ObjectId(id_)
            delattr(item, '_id')
            item = item.__dict__
            updated_item = {"$set":item}
            current_collection.update_one({'_id': _id}, updated_item)
        else:
            #insert
            _id = current_collection.insert_one(item.__dict__)
            id_ = _id.inserted_id.__str__()
        return self.find_by_id(id_)

    # TODO check if this function could be replaced by save

    def update(self, id_:str, item:T) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        item = item.__dict__
        updated_item = {"$set":item}
        document = current_collection.update_one({'_id':_id}, updated_item)
        return{ "updated_count": document.matched_count}

    def delete(self, id_:str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        result = current_collection.delete_one({'_id':_id})
        return {"delete_count": result.deleted_count}

    # TODO check if this could replace  by find_all
    def query(self, query:dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find(query): #igual que el find all, pero le pasamos el query que es un diccionario de un campo y un valor
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    #TODO add to function to process result list and use here and in find
    def query_aggregation(self, query:dict)-> dict:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.aggregate(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def get_values_db_ref(self, document: dict)->dict:
        for key in document.keys():
            #value = document.get.(key)
            if isinstance(document.get(key), DBRef):
                collection_ref = self.data_base[(document.get(key)).collection]

                document_ref = collection_ref.find_one({'_id' : ObjectId(document.get(key)).id})
                document_ref['_id'] = document_ref['_id'].__str__()
                document[key]=document_ref
                document[key]=self.get_values_db_ref(document[key])
            elif isinstance(document.get(key), list) and len(document.get(key))>0:
                document[key] = self.get_values_db_ref_list(document.get(key))
            elif isinstance(document.get(key), dict):
                document[key]= self.get_values_db_ref(document.get(key))
        return document

    def get_values_db_ref_from_list(self, list_:list)-> list:
        processed_list = []
        collection_ref = self.data_base[list_[0]._id.collection]
        for item in list_:
            _id = ObjectId(item._id)
            document_ref = collection_ref.find_one({'_id':_id})
            document_ref['_id']= document_ref['_id'].__str__()
            # TODO check if in this point each document:ref needs to call get_values_db_ref
            processed_list.append(document_ref)
        return processed_list

    def transform_object_ids(self, document:dict) ->dict:
        for key in document.keys():
            value =document.get(key)
            if isinstance(value, ObjectId):
                document[key]= document[key].__str__()
            elif isinstance(value, list) and len(value) >0:
                document[key]= self.format_list(value)
            elif isinstance(value, dict):
                document[key]=self.transform_object_ids(value)
        return document


    def format_list(self, list_:list)->list:
        processed_list =[]
        for item in list_:
            if isinstance(item, ObjectId):
                temp=item.__str__()
                processed_list.append(temp)
        if len(processed_list)==0:
            #if not processed_list, es otra forma de decir
            processed_list=list_
        return processed_list


    def transform_refs(self, item:T)->T:
        item_dict = item.__dict__
        for key in item_dict.keys():
            if item.dict.get(key).__str__().count("object")==1:
                object_=self.object_to_db_ref(getattr(item, key))
        return item


    def object_to_db_ref(self, item_ref:T)->DBRef:
        collection_ref = item_ref.__class__.__name.lower()
        return DBRef(collection_ref,ObjectId(item_ref._id))