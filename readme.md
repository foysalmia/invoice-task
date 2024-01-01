
# Invoice Management

This is a very simple api of Invoice Management system.




# API End Points

``
/api/invoice/
``
provides the invoice list.
#### Methods
```
 GET, POST
```
#### Demo

```

[
    {
        "id": 2,
        "invoice_detail": [
            {
                "id": 2,
                "description": "This is for schools",
                "quantity": 5,
                "unit_price": "15.00",
                "invoice": 2
            },
            {
                "id": 4,
                "description": "This is for an it company",
                "quantity": 10,
                "unit_price": "25.00",
                "invoice": 2
            }
        ],
        "customer_name": "Foysal ahmed",
        "date": "2023-05-01"
    },
    {
        "id": 3,
        "invoice_detail": [
            {
                "id": 3,
                "description": "This is also Mangageable",
                "quantity": 5,
                "unit_price": "20.00",
                "invoice": 3
            }
        ],
        "customer_name": "Jovan",
        "date": "2024-01-10"
    },
    {
        "id": 4,
        "invoice_detail": [],
        "customer_name": "James",
        "date": "2024-01-19"
    },
    {
        "id": 5,
        "invoice_detail": [],
        "customer_name": "Foysal",
        "date": "2024-01-18"
    }
]
```

#
``
/api/invoice/<int:pk> || /api/invoice/2/
``
provides a single invoice by its id.

#### Methods
```
 GET, PUT, PATCH, DELETE
```

#### Demo
~~~
{
    "id": 2,
    "invoice_detail": [
        {
            "id": 2,
            "description": "This is for schools",
            "quantity": 5,
            "unit_price": "15.00",
            "invoice": 2
        },
        {
            "id": 4,
            "description": "This is for an it company",
            "quantity": 10,
            "unit_price": "25.00",
            "invoice": 2
        }
    ],
    "customer_name": "Foysal ahmed",
    "date": "2023-05-01"
}

~~~
#
``
/api/invoice-detail/
``
provides the all invoices details.

#### Methods
```
    GET    POST
```
#### Demo
~~~

[
    {
        "id": 2,
        "description": "This is for schools",
        "quantity": 5,
        "unit_price": "15.00",
        "invoice": 2
    },
    {
        "id": 3,
        "description": "This is also Mangageable",
        "quantity": 5,
        "unit_price": "20.00",
        "invoice": 3
    },
    {
        "id": 4,
        "description": "This is for an it company",
        "quantity": 10,
        "unit_price": "25.00",
        "invoice": 2
    }
]
~~~
#

``
/api/invoice-detail/2/
``
provides a single invoice detail

#### Methods
```
 GET,   PUT,  PATCH,   DELETE
```

#### Demo
~~~
{
    "id": 2,
    "description": "This is for schools",
    "quantity": 5,
    "unit_price": "15.00",
    "invoice": 2
}
~~~



## Local Installation & Setup


```
  Clone the git repo
```
```
  Create a Virtual Environment
```

```
  pip install -r requirements.txt
```

```
  python manage.py migrate
```
```
  python manage.py runserver
```

*** 
### Create a Super User from the terminal to access the admin panel
****

    