from sqlalchemy import MetaData, Table, Integer, String, Column, TIMESTAMP

metadata = MetaData()
subscriptionModel = Table(
    'subscriptions', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String),
    Column('created_at', TIMESTAMP),
    Column('updated_at', TIMESTAMP)
    
)