import boto3
sqs = boto3.client("sqs")

# connect to dynamoDB table outside handler


def handler(event, context):

    # get sqs adif message, parse and insert into dynamoDB table
    try:
        data = sqs.receive_message(
            QueueUrl="https://sqs.{}.amazonaws.com/{}/sqs-rms-adif".format(environ["AWS_REGION"], environ["SIGMA_AWS_ACC_ID"]),
            MaxNumberOfMessages=1,
            VisibilityTimeout=30,
            WaitTimeSeconds=0,
            AttributeNames=["All"],
            MessageAttributeNames=["rmsadifmessage"]
        )
    except BaseException as e:
        print(e)
        raise(e)
    
        
    return {"message": "Successfully executed"}
