from datetime import date

from src.configs.db_connect import db_connection
from sqlalchemy import select, cast, Date
from src.models.subscriptionModel import subscriptionModel

class SubscriptionService:
    @staticmethod
    def get_subscriptions():
        query = select(subscriptionModel).where(
            cast(subscriptionModel.c.created_at, Date) < date.today()
        )
        results = db_connection.execute(query)

        return [{
            "username": result[1],
            "to": result[2],
            "token": None,
            "type": "subscription",

         } for result in results]