# State Registry Service

## Usage

All responses will have the form

```json
{
  "data": "Mixed type holding the content of the response",
  "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of teh `data field`

## List all devices

### Definition
`GET/devices`

### Response
* `200 OK` on success

```json
[
  {
    "identifier": 1,
    "name": "Alabama",
    "forecasts": "total open, status",
  },
  {
    "identifier": 2,
    "name": "Alaska",
    "forecasts": "total open, status",
  },
  {
    "identifier": 3,
    "name": "Arizona",
    "forecasts": "total open, status",
  },
  {
    "identifier": 4,
    "name": "Arkansas",
    "forecasts": "total open, status",
  },
  {
    "identifier": 5,
    "name": "California",
    "forecasts": "total open, status",
  },
  {
    "identifier": 6,
    "name": "Colorado",
    "forecasts": "total open, status",
  }
]
```
## Registering a new state data

### Definition
`POST/states`

### Arguments
* `"identifier":integer` fips id value representing each state
* `"name":string` state name

If a state's data of given identifier already exists, data will be overwritten.

### Response
* `201 Created` on success

## Lookup state details<hr>

`GET/device/<identifier>`
###Response
* `404 Not Found` if the state or data does not exist
* `200 OK` on success

```json
[
  {
    "identifier": "fips",
    "name": "state",
    "forecasts": "total open, status",
  },
]
```

## Delete a state's data<hr>
### Definition
`DELETE/devices/<identifier>`
### Response
* `404 Not Found` if the device does not exist
* `204 No Content` on success


