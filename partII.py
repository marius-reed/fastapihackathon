"""import psycopg2
from fastapi import FastAPI, status
import os
import urllib
import json


host_server = os.environ.get('HOST_SERVER', 'pssql-fastapihackatahon01.postgres.database.azure.com')
db_name = os.environ.get('DB_NAME', 'postgres')
db_username = os.environ.get('DB_USERNAME', 'pssqlfastapihackathonadmin')
db_password = os.environ.get('DB_PASSWORD', '')
ssl_mode = os.environ.get('SSL_MODE','require')

app = FastAPI()

@app.get("/v1/Customer/ChurnScore/{customer_id}")
async def get_customer_churn_score(customer_id:int):
    conn = psycopg2.connect(
    host=host_server,
    database=db_name,
    user=db_username,
    password=db_password)

    cur = conn.cursor()

    query = "Select * from fastapihackathon.CustomerScore where model_name = 'churn_30d' and customer_id = %s and not has_churned "

    records = cur.execute(query,(customer_id,))
    
    records = cur.fetchall()
     
    record = [dict((cur.description[i][0],value) for i, value in enumerate(row)) for row in records]
    return record


@app.post("/v1/Customer/HasChurned/{customer_id}")
async def post_has_churned(customer_id:int):

    conn = psycopg2.connect(
    host=host_server,
    database=db_name,
    user=db_username,
    password=db_password)

    cur = conn.cursor()

    query = "UPDATE fastapihackathon.CustomerScore SET has_churned = True where customer_id = %s"

    cur.execute(query,(customer_id,))

    conn.commit()

    return []

@app.get("/v1/Customer/HighestPrediction/{customer_id}")
async def get_customer_highest_prediction(customer_id:int):

    conn = psycopg2.connect(
    host=host_server,
    database=db_name,
    user=db_username,
    password=db_password)

    cur = conn.cursor()

    query = "Select * from fastapihackathon.CustomerScore where customer_id = %s ORDER BY score DESC LIMIT 1"

    records = cur.execute(query,(customer_id,))
    
    records = cur.fetchall()
     
    record = [dict((cur.description[i][0],value) for i, value in enumerate(row)) for row in records]
    return record"""