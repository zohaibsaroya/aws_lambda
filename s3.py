def lambda_handler(event,context):
    bucket=event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'],encoding='utf-8' )
    try:
        response=s3.get_object(Bucket=bucket,Key=key)
        text=response["Body"].read().decode()
        data=json.loads(text)
        print(data)
        