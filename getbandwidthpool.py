#"""
#This script retrive all baremetal's public outbound bandwidth under account.
#"""
import SoftLayer

#USERNAME = 'TEN1409073'
#API_KEY = 'b6e527173d31073f16bec8b4c13236e54af6577533b1eb0bf2e40a0dd7a76922'

#USERNAME = 'TEN1803999'
#API_KEY = 'e6e15c1db0c79dd61eadd61d419ff06716e7b1987ff40533d499b27c0103fdd2'

#USERNAME = 'mikefitzgerald'
#API_KEY = '9905caafc1e80d2d0e7e0f17be8a206af2c4a283c654aea03b60e1e7b46f36f0'

USERNAME = 'TEN2119708'
API_KEY = '6637ed6ef4587e14a12b6607fa9728e50372d1db7a546488ffc55f651b37b08e'

# client = SoftLayer.create_client_from_env()
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

#"""
#Declare these to keep line lengths minimal
#"""
accountClient = client['SoftLayer_Account']
# hardwareService = client['SoftLayer_Hardware']

#"""
#Add an object mask to retrieve our billing items related to the servers
#http://softlayer.github.io/reference/datatypes/SoftLayer_Hardware_Server
#for a list of the relational properties you can retrieve along with hardware.
#"""
#objectMask = 'mask[primaryIpAddress]'

#get bandwidthpool list
bandwidthpools = accountClient.getVirtualDedicatedRacks()

# We are looking for the bandwidth pool
for item in bandwidthpools:
    try:
        print("Bandwidth Pool Name:")
        print(item["name"])
        print("Allocated Bandwidth GB:")
        print(client['SoftLayer_Network_Bandwidth_Version1_Allotment'].getTotalBandwidthAllocated(id=item['id']))
        print("Current used outbound bandwidth:")
        print(client['SoftLayer_Network_Bandwidth_Version1_Allotment'].getOutboundPublicBandwidthUsage(id=item['id']))
        print("Projected outbound bandwidth at the end of the billing cycle:")
        print(client['SoftLayer_Network_Bandwidth_Version1_Allotment'].getProjectedPublicBandwidthUsage(id=item['id']))
        print("Will the outbandwidth usage overload:")
        print(client['SoftLayer_Network_Bandwidth_Version1_Allotment'].getProjectedOverBandwidthAllocationFlag(id=item['id']))
    except SoftLayer.SoftLayerAPIError as e:
        """
#        If there was an error returned from the SoftLayer API then bomb out with the
#        error message.
        """
        print("Unable to get bandwidth pool:  \nfaultCode= %s, \nfaultString= %s" % (e.faultCode, e.faultString))
print("Done")
