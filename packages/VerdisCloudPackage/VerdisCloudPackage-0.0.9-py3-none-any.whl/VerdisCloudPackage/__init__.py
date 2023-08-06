import os
from VerdisCloudPackage import AWS
def cloud_choice(config):
    cloud_ch=os.environ.get('PYTHON_CLOUD', "AWS")
    if cloud_ch=="AWS":
        return AWS.getParams(config)
    else:
        return AWS.getParams(config)


    

