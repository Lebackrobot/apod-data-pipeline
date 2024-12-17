import schedule
import time

from src.configs.logging_config import logging
from src.subscription_queuing_pipeline import SubscriptionQueuingPipeline
from src.setup_cache_pipeline import SetupCachePipeline


if __name__ == '__main__':
    log = logging.getLogger(__name__)

    log.info('🚀 Start pipeline service')
    schedule.every().day.at('08:00', 'America/Sao_Paulo').do(SetupCachePipeline.run)
    schedule.every().day.at('20:45', 'America/Sao_Paulo').do(SubscriptionQueuingPipeline.run)

    while True:
        schedule.run_pending()
        time.sleep(1)
