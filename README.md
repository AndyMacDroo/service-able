# service-able

A very simple health check framework for applications, written in python.

### Defining Services

An simple example `services.yml` service definition file can be found below:

```yaml

---
service_health:

  google:
    check_me:
      every:
        seconds: 1
    available_at:
      url: https://www.google.co.uk
    expect:
      a_http_response:
        code: 200
        
  mock_service:
    check_me:
      every:
        seconds: 10
    available_at:
      url: https://jsonplaceholder.typicode.com/todos/1
    expect:
      a_http_response:
        code: 200
        json: '{ "userId": 1, "id" : 1, "title": "delectus aut autem", "completed": false }'

```

## Installation and Usage

Install python dependencies:
```
pip install -r requirements.txt
```

Get usage notes:
```
python main.py -h
```

## Daemon

The health check daemon will log out when services become unhealthy based on their config in the following format:

```
 ____  ____  ____  _  _  __  ___  ____       __   ____  __    ____
/ ___)(  __)(  _ \/ )( \(  )/ __)(  __)___  / _\ (  _ \(  )  (  __)
\___ \ ) _)  )   /\ \/ / )(( (__  ) _)(___)/    \ ) _ (/ (_/\ ) _)
(____/(____)(__\_) \__/ (__)\___)(____)    \_/\_/(____/\____/(____)
Starting service health checks...
2019-01-05 23:13:37.135614 - [service-able/image_service] - the service is UNHEALTHY - expected:{'a_http_response': {'code': 200}}.
2019-01-05 23:13:38.136978 - [service-able/image_service] - the service is UNHEALTHY - expected:{'a_http_response': {'code': 200}}.
2019-01-05 23:13:39.138299 - [service-able/image_service] - the service is UNHEALTHY - expected:{'a_http_response': {'code': 200}}.
```
