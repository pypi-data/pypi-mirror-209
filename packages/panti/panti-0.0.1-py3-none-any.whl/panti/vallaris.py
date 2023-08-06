import asyncio
import httpx
import os
from typing import List
from pandas import read_pickle
from dotenv import load_dotenv
from tqdm import tqdm
from uuid import uuid4
from furl import furl
import abc


class GeoJsonInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "get_geojson") and callable(subclass.get_geojson)


class Vallaris:
    base_url: str = "https://b-2.i-bitz.world/core/api/features/1.0-beta/collections"
    api_key: str
    collection_id: str

    def __init__(
        self, base_url: str, api_key: str, collection_id: str, auto_init_client=True
    ) -> None:
        self.api_key = api_key
        self.collection_id = collection_id

        if auto_init_client:
            self.create_client()

    def create_client(self, timeout=600.0):
        self.timeout = httpx.Timeout(timeout, connect=timeout)
        self.client = httpx.AsyncClient(timeout=self.timeout)

    async def _create(self, geojson: dict, collection_id=None) -> httpx.Response:
        if collection_id is None:
            collection_id = self.collection_id

        reqUrl = f"https://b-2.i-bitz.world/core/api/features/1.0-beta/collections/{collection_id}/items?api_key={self.api_key}"

        req_id = uuid4()

        print(
            f"{str(req_id)[-6:]}: Making POST request with {len(geojson['features'])} units"
        )
        data = await self.client.post(reqUrl, json=geojson)
        print(f"{str(req_id)[-6:]}: done")
        return data

    async def create(self, units: List[UnitData]):
        geojson = {
            "type": "FeatureCollection",
            "features": [unit.get_geojson() for unit in units],
        }

        response = await self._create(geojson)

        return response.json()

    async def _update(
        self, obj_id: str, geojson: dict, collection_id=None
    ) -> httpx.Response:
        if collection_id is None:
            collection_id = self.collection_id

        reqUrl = f"https://b-2.i-bitz.world/core/api/features/1.0-beta/collections/{collection_id}/items/{obj_id}?api_key={self.api_key}"

        req_id = uuid4()

        print(
            f"{str(req_id)[-6:]}: Making PUT request with {len(geojson['features'])} units"
        )
        data = await self.client.put(reqUrl, json=geojson)
        print(f"{str(req_id)[-6:]}: done")
        return data

    async def update(self, obj_id: str, units: List[UnitData]):
        geojson = {
            "type": "FeatureCollection",
            "features": [unit.get_geojson() for unit in units],
        }
        response = await self._update(obj_id, geojson)

        return response.json()

    async def _delete_all(self, collection_id=None) -> httpx.Response:
        if collection_id is None:
            collection_id = self.collection_id

        reqUrl = f"https://b-2.i-bitz.world/core/api/features/1.0-beta/collections/{collection_id}/items?api_key={self.api_key}"

        data = await self.client.delete(reqUrl)
        return data

    async def delete_all(self):
        response = await self._delete_all()
        return response

    async def _get_one(self, obj_id: str, collection_id=None) -> httpx.Response:
        if collection_id is None:
            collection_id = self.collection_id

        reqUrl = f"https://b-2.i-bitz.world/core/api/features/1.0-beta/collections/{collection_id}/items/{obj_id}?api_key={self.api_key}"

        data = await self.client.get(reqUrl)
        return data

    async def get_one(self, obj_id: str):
        response = await self._get_one(obj_id)
        return response.json()

    async def _get_many(
        self,
        properties: dict,
        collection_id=None,
    ) -> httpx.Response:
        if collection_id is None:
            collection_id = self.collection_id

        reqUrl = f"https://b-2.i-bitz.world/core/api/features/1.0/collections/{collection_id}/items?api_key={self.api_key}"
        reqUrl = furl(reqUrl).add(properties).url
        data = await self.client.get(reqUrl)
        return data

    async def get_many(self, properties: dict):
        response = await self._get_many(properties)
        return response.json()

    async def _edit_one(
        self, obj_id: str, geojson: dict, collection_id=None
    ) -> httpx.Response:
        if collection_id is None:
            collection_id = self.collection_id

        reqUrl = f"https://b-2.i-bitz.world/core/api/features/1.0-beta/collections/{collection_id}/items/{obj_id}?api_key={self.api_key}"

        data = await self.client.patch(reqUrl, json=geojson)
        return data

    async def edit_one(self, obj_id: str, unit: UnitData):
        response = await self._edit_one(obj_id, unit.get_geojson())
        return response.json()
