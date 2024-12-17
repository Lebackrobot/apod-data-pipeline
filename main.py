import schedule
import time

from src.configs.logging_config import logging
from src.subscription_queuing_pipeline import SubscriptionQueuingPipeline
from src.setup_cache_pipeline import SetupCachePipeline


if __name__ == '__main__':
    log = logging.getLogger(__name__)

    log.info('🚀 Start pipeline service')

    log.info('📅 Scheduler SetupCachePipeline.run 07:00')
    schedule.every().day.at('07:00', 'America/Sao_Paulo').do(SetupCachePipeline.run)

    log.info('📅 Scheduler SubscriptionQueuingPipeline.run 10:00')
    schedule.every().day.at('10:00', 'America/Sao_Paulo').do(SubscriptionQueuingPipeline.run)

    while True:
        schedule.run_pending()
        time.sleep(1)
