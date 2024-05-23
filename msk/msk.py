import boto3

client = boto3.client('kafka')

list_nodes_response = client.list_nodes(
    ClusterArn='arn:aws:kafka:ap-southeast-1:314402748588:configuration/meeyland-test/f60bf186-7cea-4732-8ec6-90476a68cd29-3',
    MaxResults=1
)

print('\n')
print('Here is the first node in the list:')
print('\n')
print(list_nodes_response['NodeInfoList'])

next_token = list_nodes_response['NextToken']

list_nodes_response = client.list_nodes(
    ClusterArn='arn:aws:kafka:ap-southeast-1:314402748588:configuration/meeyland-test/f60bf186-7cea-4732-8ec6-90476a68cd29-3',
    NextToken=next_token
)

print('\n')
print('Here are the remaining nodes in the list:')
print('\n')
print(list_nodes_response['NodeInfoList'])