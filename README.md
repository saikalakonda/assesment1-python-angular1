# Service mointoring for the services like httpd,rabbitmq, postgresql

## Usage

All responses will have the form

json
{
    "data": "response",
    "message": "Description"
}


Subsequent response definitions will only detail the expected value of the `data field`

### List all services

*Definition*

`GET /servicemonitoring`

*Response*

- `200 OK` on success

json
[
    { 
   "service_name":"httpd",
   "service_status":"UP",
   "host_name":"host1"
	},
    { 
   "service_name":"rabbitmq",
   "service_status":"UP",
   "host_name":"host2"
},
{ 
   "service_name":"postgresql",
   "service_status":"UP",
   "host_name":"host3"
}
]


### Registering a new servicemonitoring

*Definition*

`POST /servicemonitoring`

Creates a index in elasticsearch - store it whole the json 

*Arguments*

- `"service_name":string` define services
- `"service_status":string` service is up and running
- `"host_name":string` the IP address of the hostname

If a service is up and running, below json to be saved into a file.

*Response*

- `201 Created` on success

json
{ 
   "service_name":"httpd",
   "service_status":"UP or DOWN",
   "host_name":"host1"
}


## Lookup services mointoring  details

`GET /servicemonitoring/id?status

get the status of document search through json 

*Response*

- `404 Not Found` if the service does not exist
- `200 OK` on success

json
{
   "service_name":"httpd",
   "service_status":"UP",
   "host_name":"host1"
}
