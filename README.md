# SIMPLE VULNERABILITY CHECKER API

## Preposition ##
There are a lot of issues from vulnerable libs on  Linux boxes. Therefore, this is  a service that can generate a list from a database of package(library) versions, that have open vulnerabilities. 
This way is possible to identify which versions we have to avoid. 
#### Request format ####
`http://127.0.0.1:80/versions?name=xz-utils`
#### Response format ####
- name: name of the package that is equal to the query param value
- versions: list of affected versions of the package
- timestamp: timestamp of the request

Example: 
`{
    "name": "xz-utils",
    "versions": [
        "5.2.2-1.3ubuntu0.1",
        "5.2.4-1ubuntu1.1",
        "5.1.1alpha+20120614-2ubuntu2.14.04.1+esm1",
        "5.1.1alpha+20120614-2ubuntu2.16.04.1+esm1"
    ],
    "timestamp": "2024-05-10 22:13:18"
}`

### Datasource ###
The service rely on the osv.dev database to check for vulnerabilities.
The following ecosystems should be used: 'Debian', 'Ubuntu'. 

### Tests ###
There is no test coverage requirement for this service on this level. 
