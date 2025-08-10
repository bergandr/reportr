import zmq
import time

samples = [{"directory": "reports", "zip_name": "testing.zip"}]


def main():
    # this is basically boilerplate request setup code, based on the course-provided zmq documentation
    # establish the context, set up a request socket, and connect to the server
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:3333")

    # loop over the sample data
    for sample in samples:
        print("\nSending", sample)
        socket.send_json(sample)  # use send_json since all requests will be in JSON format

        # get the reply from the server
        reply = socket.recv_json()
        print("Full reply:", reply)

        time.sleep(5)  # so that we can see each request more clearly on the video demo


if __name__ == "__main__":
    main()
