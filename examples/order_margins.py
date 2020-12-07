import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="your_api_key")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

data = kite.generate_session("request_token_here", secret="your_secret")
kite.set_access_token(data["access_token"])

# Fetch margin detail for order/orders
try:
    # Fetch margin detail for single order
    order_param_single = [{
        "exchange": "NSE",
        "tradingsymbol": "INFY",
        "transaction_type": "BUY",
        "variety": "regular",
        "product": "MIS",
        "order_type": "MARKET",
        "quantity": 2
        }]

    margin_detail = kite.order_margins(order_param_single)
    logging.info("Required margin for single order: {}".format(order_param_single))    
    
    # Fetch margin detail for list of orders 
    order_param_multi = [{
        "exchange": "NSE",
        "tradingsymbol": "SBIN",
        "transaction_type": "BUY",
        "variety": "regular",
        "product": "MIS",
        "order_type": "MARKET",
        "quantity": 10
        },
        {
        "exchange": "NFO",
        "tradingsymbol": "TCS20DECFUT",
        "transaction_type": "BUY",
        "variety": "regular",
        "product": "MIS",
        "order_type": "LIMIT",
        "quantity": 5,
        "price":2725.30
        },
        {
        "exchange": "NFO",
        "tradingsymbol": "NIFTY20DECFUT",
        "transaction_type": "BUY",
        "variety": "bo",
        "product": "MIS",
        "order_type": "MARKET",
        "quantity": 5
    }]

    margin_detail = kite.order_margins(order_param_multi)
    logging.info("Required margin for order_list: {}".format(margin_detail))

except Exception as e:
    logging.info("Required order margin: {}".format(e))

