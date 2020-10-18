from controllers import *

# FastAPI Rooting
app.add_api_route('/', index)
app.add_api_route('/chatbot', chat, methods=['GET','POST'])
app.add_api_route('/chatbot/{sendMessage}',bot_reply)
app.add_api_route('/register',register, methods=['GET','POST'])
#app.add_api_route('/ws', websocket_endpoint)