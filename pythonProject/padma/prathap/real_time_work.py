#  # Service Name                     Status                      Type
#  # system                           OK                          System
#  # omd                              OK                          Process
#  # adhd                             OK                          Process
#  # postgres                         OK                          Process
#  # psrv                             OK                          Process
#  # tomcat                           OK                          Process
#  # udppm                            OK                          Process
#  # streamsnapd                      OK                          Process
#  # fusededup                        OK                          Process
# reddy = open("real_time","r")
# service = reddy.read()
# c = service.splitlines()
# print("print c::;",c)
# h = []
# for pro in c:
#     if "Process" in pro:
#         # v = pro.split()
#         # print("pro v  :",v)
#         d = pro.split()[1]
#         m = pro.split()[0]
#         h.append((m,d))
#         print("print h:",h)
#
#
# #processes = [(line.split()[0],line.split()[1]) for line in c if 'Process' in line]
# print("processes:::::::::::::::", h)
#
# #print('Output: ' + o.decode('ascii'))
# #print('Error: '  + e.decode('ascii'))
# #print('code: ' + str(proc.returncode))
# omd = False
# psrv = False
# adhd = False
# state = "OK"
# for line in h:
#     # print(line)
#     if line[0] == 'psrv'and line[1] == state:
#         print("it is running")
#         psrv = True
#     if line[0] == 'adhd' and line[1] == state:
#         print("it is running")
#         adhd = True
#     if line[0] == 'omd' and line[1] == state:
#         print("it is running")
#         omd = True
# if psrv and adhd and omd:
#     print("it is ruNNING")
# else:
#     raise AssertionError

#we need to get the  hostName and nicType from the below data
rk = {
    'memberOrderIndex': 1,
	'delay': 10,
	'vmMembers': [{
		'memberUuId': '5028d3cd-103b-454a-ec49-4381d44ac995',
		'memberName': 'auto-rd-vm2',
		'vm': True,
		'executionStatus': '',
		'cdsAppId': '5848',
		'cdsClusterId': '145313127218',
		'targetClusterId': '0',
		'validForAppGroup': True,
		'displayAppName': 'auto-rd-vm2',
		'displayAppType': 'VM',
		'apptype': 'VM',
		'recoveryType': {
			'recoveryTypeId': 1,
			'name': 'Recover VM From VMWare VM Backup',
			'recoveryTypeOrder': '1',
			'description': 'Add VMs you wish to recover at the DR site. Each VM may be recovered only once and will retain its original host name.'
		},
		'infoRequired': False,
		'policyOpCode': 0,
		'id': 0,
		'vappName': '',
		'numberOfCpus': 2,
		'actualNumberOfNics': 1,
		'testNumberOfNics': 1,
		'testMemoryInMbs': 2048,
		'actualMemoryInMbs': 2048,
		'storageLocation': '[Branch6_DS] auto-rd-vm2/auto-rd-vm2.vmx',
		'shutdownOrder': 0,
		'keyValue': 'vm-85109',
		'numberOfVirtualDisks': 3,
		'hddInGbs': 50.0,
		'hostName': 'auto-rd-vm2',
		'reasonForInvalidVM': '',
		'cupResourceAllocation': {
			'reservation': 0,
			'limit': -1,
			'shares': 2000,
			'sharesLevel': 1,
			'numberOfCpus': 0,
			'corePerSocket': 0
		},
		'memoryResourceAllocation': {
			'reservation': 0,
			'limit': -1,
			'shares': 20480,
			'sharesLevel': 1,
			'numberOfCpus': 0,
			'corePerSocket': 0
		},
		'testCPUAllocation': 0,
		'actualCPUAllocation': 0,
		'prescript': '',
		'postscript': '',
		'username': '',
		'passwd': '',
		'nicNames': [{
			'deviceConfigId': 4000,
			'macAddress': '00:50:56:a8:72:6c',
			'nicType': 'VirtualVmxnet3',
			'interfaceLabel': 'Network adapter 1',
			'pciSlotNumber': 192
		}],
		'vmAllNicDataList': [{
			'interfaceLabel': 'Network adapter 1',
			'enforcedStaticIp': False,
			'enforcedStaticDnsIp': False,
			'gateway': '',
			'macAddress': '00:50:56:a8:72:6c',
			'nicType': 'VirtualVmxnet3',
			'pciSlotNumber': 192
		}],
		'sourceIp': '172.27.64.195',
		'sourceSubnet': '',
		'sourceGateway': '172.27.64.1',
		'osName': 'linux',
		'appliancegroupid': 0,
		'coresPerSocket': 1,
		'testCoresPerSocket': 1,
		'virtualSocket': 2,
		'testVirtualSocket': 2,
		'sequenceNumber': 0,
		'bootdisksize': 0,
		'originalBootdisksize': 0,
		'critical': False,
		'vappStartupOrder': 0,
		'vmalreadyPresentInRecPlan': False
	}],
	'appMembers': []}
print(rk.values())
print(rk.keys())
cv = rk["vmMembers"]
print("print(cv)  =",cv)

print(type(cv))
for b in cv:
	print(b)
	bn = b["hostName"]
	print("print hostname   :::",bn)
	df = b["nicNames"]#[0]["nicType"]
	print(df[0]["nicType"])

