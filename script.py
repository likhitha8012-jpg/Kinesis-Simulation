import boto3
import json
import time
import random

stream_name = 'SwipeData'
region_name = 'eu-north-1'

kinesi_client = boto3.client('kinesis', region_name=region_name)

def generate_random_data():
    return {
        'sensor_id': random.randint(1, 10),
        'temperature': round(random.uniform(20.0, 30.0), 2),
        'humidity': round(random.uniform(30.0, 60.0), 2),
        'timestamp': time.time()
    }
def send_data_to_kinesis():
    while True:
        data = generate_random_data()
        partition_key = str(data['sensor_id'])
        print(f"Sending data: {data}")
        kinesi_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=str(data['sensor_id'])
        )
        time.sleep(1)

if __name__ == "__main__":
    print("Starting to send data to Kinesis stream...")
    send_data_to_kinesis()
