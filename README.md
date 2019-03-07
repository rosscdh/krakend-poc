# KrakenD POC

kraken for assembling preexisting services into unified endpoints


## Usage

### Raw Backend Call

Call the backend directly to see the "actual data"
```
# call the backend services directly
http http://192.168.8.165:8001/hello/bob/ 

HTTP/1.1 200 OK
Connection: close
Date: Thu, 07 Mar 2019 10:32:10 GMT
Server: gunicorn/19.9.0
content-length: 62
content-type: application/json; charset=utf-8

{
    "is_superuser": true,
    "message": "Hello bob!",
    "name": "bob"
}

http http://192.168.8.165:8001/test/data/
http http://192.168.8.165:8001/test/list_data/

```

### Kraken Call

Call the kraken frontend to get the whitelist,blacklist combined results and combined list data result set

```
# kraken combined route
http http://localhost:8080/hellow/monkey/
HTTP/1.1 200 OK
Cache-Control: public, max-age=3600
Content-Length: 176
Content-Type: application/json; charset=utf-8
Date: Thu, 07 Mar 2019 10:34:00 GMT
X-Krakend: Version 0.7.1
X-Krakend-Completed: true

{
    "is_superuser": true,
    "list_results": [
        {
            "list_data": 0
        },
        {
            "list_data": 1
        },
        {
            "list_data": 2
        },
        {
            "list_data": 3
        },
        {
            "list_data": 4
        }
    ],
    "name": "monkey",
    "results": [
        {
            "num": 0
        },
        {
            "num": 1
        },
        {
            "num": 2
        }
    ]
}
```