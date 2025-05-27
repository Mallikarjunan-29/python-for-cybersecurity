import os
source_address=[]
dest_address=[]
action=[]
port=[]
connection_type=[]
event_date=[]
event_time=[]
file_path=os.path.join("Day-2/logs/log.txt")
def parse_log(line):
    try:
        log=line.strip().split()
        timestamp=log[0]+" "+log[1]
        action=log[2]
        source_address=log[3]
        dest_address=log[5]
        connection_type=log[6]
        port=log[7]
        return{
            'timestamp':timestamp,
            'action':action,
            'src_IP':source_address,
            'dest_IP':dest_address,
            'port':port,
            'connection':connection_type,
        }
    except IndexError:
        return None
    
with open(file_path) as f:
    logs =f.readlines()
    for log in logs:
        event= parse_log(log)
        if event['action']=="DENY":
            print(f"{event['action']} connection from {event['src_IP']} to {event['dest_IP']} on port {event['port']}")


   
