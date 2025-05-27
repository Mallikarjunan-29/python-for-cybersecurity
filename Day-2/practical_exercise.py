import os
# source_address=[]
# dest_address=[]
# action=[]
# port=[]
# connection_type=[]
# event_date=[]
# event_time=[]
file_path=os.path.join("Day-2/logs/log.txt")
with open(file_path) as f:
    logs =f.readlines()
for log in logs:
    # event_date.append(log.split(" ")[0])
    # event_time.append(log.split(" ")[1])
    # action.append(log.split(" ")[2])
    # source_address.append(log.split(" ")[3])
    # dest_address.append(log.split(" ")[5])
    # connection_type.append(log.split(" ")[6])
    # port.append(log.split(" ")[7])
    if log.find("DENY")>0:
        print(log)

