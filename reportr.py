# generate checksums
import zmq
from functions import zip_all

# send if cause of error cannot be determined
generic_error_message = {"action": "error", "message": "There was an error processing the request."}


# server code
# this is basically boilerplate server setup code, based on the course-provided zmq documentation
# establish the context and set up the socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:3333")
print("Listening for messages ...")

# listen for messages
try:
    while True:
        request = socket.recv_json()
        if len(request) > 0:
            print("Received request")
            print("Replying to request\n")
            zip_all(request["directory"], request["zip_name"])
            reply = request
            socket.send_json(reply)
            print("Listening for messages ...")
        else:
            # if the client somehow connected but the message was lost
            socket.send_json(generic_error_message)

# shutdown server when receiving ctrl-C
except KeyboardInterrupt:
    print("\nShutting down the server ...\n")

# Clear the context and exit
context.destroy()
