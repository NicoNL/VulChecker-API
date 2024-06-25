from fastapi import APIRouter , HTTPException, Query
from .models import PackInfo
from typing import List
from datetime import datetime
import requests
import json

router = APIRouter()

@router.get("/versions", description="GET method to obtain the vulnerabilities of a package in Debian and Ubuntu")
async def versions(name: str = Query(..., description="Name of the package")):
    
    def getVuls(ecosystem):
        url = "https://api.osv.dev/v1/query"
        payload = {
            "package": {
                "name": name,
                "ecosystem": ecosystem
            }
        }
        response = requests.post(url, json=payload)
        data = response.json()
        return data

    def getVersions(vuls):
        result = []
        for vul in vuls:
            if 'affected' in vul:
                for affected_item in vul['affected']:
                    for r in affected_item['ranges']:
                        for event in r['events']:
                            if 'fixed' in event:
                                result.append(event['fixed'])

        result = list(set(result))
        return result

    try:
        ubuntu_vuls = getVuls("Ubuntu").get('vulns', [])
        debian_vuls = getVuls("Debian").get('vulns', [])
        
        if not debian_vuls and not ubuntu_vuls:
            raise HTTPException(status_code=404, detail="No vulnerabilities found for the given package or the package does not exist")
        
        vuls = getVersions(ubuntu_vuls) + getVersions(debian_vuls)
        
        result = {
            "package": name,
            "versions" : vuls,
            "timestamp" :datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
