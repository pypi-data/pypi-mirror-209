import asyncio

import confik

API_KEY = confik.get('PAYMOB_API_KEY')


async def main():
    async with Paymob(api_key=API_KEY) as paymob:
        order = await paymob.create_order(
            data={
                "delivery_needed": False,
                "amount_cents": 500,
                "currency": "EGP",
                "items": [
                    dict(
                        name="Item 3",
                        amount_cents=200,
                        description="Item 1 desc",
                        quantity=1,
                    ),
                    dict(
                        name="Item 4",
                        amount_cents=300,
                        description="Item 1 desc",
                        quantity=1,
                    ),
                ],
                "shipping_data": {
                    "apartment": "803",
                    "email": "claudette09@exa.com",
                    "floor": "42",
                    "first_name": "Clifford",
                    "street": "Ethan Land",
                    "building": "8028",
                    "phone_number": "+86(8)9135210487",
                    "postal_code": "01898",
                    "extra_description": "8 Ram , 128 Giga",
                    "city": "Jaskolskiburgh",
                    "country": "CR",
                    "last_name": "Nicolas",
                    "state": "Utah",
                },
            }
        )

        payment = await paymob.pay(
            500,
            "EGP",
            order.id,
            2020230,
            data={
                "billing_data": {
                    "apartment": "803",
                    "email": "claudette09@exa.com",
                    "floor": "42",
                    "first_name": "Clifford",
                    "street": "Ethan Land",
                    "building": "8028",
                    "phone_number": "+86(8)9135210487",
                    "postal_code": "01898",
                    "extra_description": "8 Ram , 128 Giga",
                    "city": "Jaskolskiburgh",
                    "country": "CR",
                    "last_name": "Nicolas",
                    "state": "Utah",
                },
                "expiration": 3600,
                "lock_order_when_paid": False,
            },
        )


try:
    asyncio.run(main())
except PaymobError as e:
    print(e.response.json())
