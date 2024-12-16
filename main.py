import schedule
import time

from src.subscription_queuing_pipeline import SubscriptionQueuingPipeline
from src.setup_cache_pipeline import SetupCachePipeline


if __name__ == '__main__':
    #schedule.every().day.at('08:00', 'America/Sao_Paulo').do(SetupCachePipeline.run)
    #schedule.every().day.at('20:45', 'America/Sao_Paulo').do(SubscriptionQueuingPipeline.run)

    print("Start pipeline service")
    #SubscriptionQueuingPipeline.run()
    SetupCachePipeline.run()

    while True:
        schedule.run_pending()
        time.sleep(1)
