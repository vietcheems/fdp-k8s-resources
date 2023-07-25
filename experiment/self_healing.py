import subprocess, time, datetime


DURATION = 600


with open('result.csv', 'w') as f:
        f.write('timestamp,node_count,pod_count\n')

for step in range(DURATION):
    print(f'Step: {step}')
    nodes = subprocess.run(['kubectl', 'get', 'node'], stdout=subprocess.PIPE)
    nodes = nodes.stdout.decode('utf-8').split('\n')
    nodes = nodes[1:-1]
    node_count = 0
    for node in nodes:
        if node.split()[1] == 'Ready':
        # if 'Ready' in node:
            node_count += 1

    pods = subprocess.run(['kubectl', 'get', 'pod', '-l' ,'app=superset'], stdout=subprocess.PIPE)
    pods = pods.stdout.decode('utf-8').split('\n')
    pods = pods[1:-1]
    pod_count = 0
    for pod in pods:
        if pod.split()[1] == '1/1' and pod.split()[2] == 'Running':
            pod_count += 1

    with open('result.csv', 'a') as f:
        f.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},{node_count},{pod_count}\n')
    time.sleep(1)
