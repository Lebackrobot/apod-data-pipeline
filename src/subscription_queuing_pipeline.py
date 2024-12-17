import json

from src.services.rabbit_service import RabbitService
from src.services.subscriptionService import SubscriptionService
from src.configs.logging_config import logging

log = logging.getLogger(__name__)

class SubscriptionQueuingPipeline:
    @staticmethod
    def handle_subscriptions_stage():
        return SubscriptionService.get_subscriptions()

    @staticmethod
    def send_rabbit_message_stage(subscriptions):
        for subscription in subscriptions:
            rabbitMessage = json.dumps(subscription)

            log.info(f'Send subscription email to rabbit: {subscription['to']}')
            RabbitService.send(rabbitMessage)

    @staticmethod
    def run():
        log.info('Run handle_subscriptions_stage')
        subscriptions = SubscriptionQueuingPipeline.handle_subscriptions_stage()

        log.info('Run send_rabbit_message_stage', subscriptions)
        SubscriptionQueuingPipeline.send_rabbit_message_stage(subscriptions)
