import boto3

def lambda_handler(event, context):
    client = boto3.client('cognito-idp', region_name='us-east-1')  # change region if needed

    response = client.admin_create_user(
        UserPoolId='us-east-1_ntg4MuBtW',
        Username=event['email'],
        UserAttributes=[
            {'Name': 'email', 'Value': event['email']},
            {'Name': 'email_verified', 'Value': 'true'}
        ],
        TemporaryPassword='TempPass123!',
        MessageAction='SUPPRESS'
    )
    
    client.admin_set_user_password(
        UserPoolId='us-east-1_ntg4MuBtW',
        Username=event['email'],
        Password=event['password'],
        Permanent=True
    )

    return {
        'statusCode': 200,
        'body': 'User created successfully!'
    }

