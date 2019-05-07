import json
from unittest import TestCase

import requests
from osbot_aws.apis.Secrets import Secrets
from pbx_gs_python_utils.utils import Http
from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Elastic_Search import Elastic_Search

from oss_bot.helpers.Test_Helper import Test_Helper


class Load_Data_Elk:

    def __init__(self):
        self.oss_server     = 'https://open-security-summit.org'
        self.aws_secret_id  = 'elk-oss-data'
        self.index_id       = 'oss-metadata'
        self._elastic       = None

    def elastic(self):
        if self._elastic is None:
            self._elastic = Elastic_Search(index=self.index_id, aws_secret_id = self.aws_secret_id)

    def get_data(self,path):
        url = "{0}{1}".format(self.oss_server, path)
        return requests.get(url).json()

    def send_data_to_elk(self, data, delete_index=False):
        if delete_index:
            self.elastic().delete_index().create_index()
        try:
            records_added = self.elastic().add_bulk(data)
            return { 'status':'ok','data': records_added }
        except Exception as error:
            return {'status': 'error', 'data': '{0}'.format(error) }



class test_Load_Data_Elk(Test_Helper):
    def setUp(self):
        super().setUp()
        self.load_data_elk = Load_Data_Elk()

    def test_data(self):
        data = self.load_data_elk.get_data('/api/index.json')
        assert len(data) > 100

    def test_send_data_to_elk(self):
        data = self.load_data_elk.get_data('/api/index.json')
        self.result = self.load_data_elk.send_data_to_elk(data, delete_index=True)

    def test_data_participants(self):
        path = '/participant/api/index.json'
        data = self.load_data_elk.get_data(path)
        self.result = len(data)


    def test_load_local_data(self):
        data = requests.get('http://localhost:1313/participant/json/').json()
        for item in data:
            print(item.get('title'),item.get('word_count'))

    def test_find_problematic_record(self):
        data = self.load_data_elk.get_data('/api/index.json')
        self.load_data_elk.elastic()
        for item in data:
            Dev.pprint(item)
            break




