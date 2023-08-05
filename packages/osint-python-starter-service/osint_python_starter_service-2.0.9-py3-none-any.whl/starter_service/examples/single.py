import os

from starter_service.examples.app.classes.config import Config

os.environ['CONSUME'] = 'config'
os.environ['PRODUCE'] = 'config'

from starter_service.base_service import StarterService
from starter_service.api import API


class SingleRoute(StarterService):
    name = "single_route"
    path = "app"

    def health(self):
        return "OK"

    def ready(self):
        return True

    def kafka_callback(self):
        """Kafka callback"""
        self.logger.info("Kafka callback")

    def api_callback(self):
        """API callback"""
        self.logger.info("API callback")

    @API.post(consumer="config", producer="config", doc="Process raw article and return metadata")
    def handle_message(self, config: dict):
        config['languages'] = ['ru', 'ru']
        config['translations'][0]['from_'] = "def"
        config['translations'][0]['from'] = "def"
        return config

        # return {
        #     "articleId": message['id'],
        #     "origin": "string",
        #     "data": [
        #         {
        #             "type": "string",
        #             "value": "string",
        #             "confidence": 0,
        #             "metadata": {
        #                 "string": "string"
        #             }
        #         }
        #     ]
        # }


if __name__ == '__main__':
    SingleRoute()
