import json

from src.services.rabbit_service import RabbitService
from src.services.subscriptionService import SubscriptionService

class SubscriptionQueuingPipeline:
    @staticmethod
    def handle_subscriptions_stage():
        return SubscriptionService.get_subscriptions()

    @staticmethod
    def send_rabbit_message_stage(subscriptions):
        for subscription in subscriptions:
            rabbitMessage = json.dumps(subscription)

            print(f'>>> Send subscription email to rabbit: {subscription['to']}')
            RabbitService.send(rabbitMessage)

    @staticmethod
    def run():
        print('>>> Run handle_subscriptions_stage')
        subscriptions = SubscriptionQueuingPipeline.handle_subscriptions_stage()

        print('>>> Run send_rabbit_message_stage', subscriptions)
        SubscriptionQueuingPipeline.send_rabbit_message_stage(subscriptions)
