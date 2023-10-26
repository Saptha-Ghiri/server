# import socket
# import cv2
# import pickle
# import struct

# def cam1(port,ip):
#     def start():
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         host_ip = ip # Paste your server IP address here


#         try:
#             client_socket.connect((host_ip, port))  # Attempt to establish the connection
#             print("Connected to the server")
#             receive(client_socket)
#         except Exception as e:
#             print(f"Connection failed: {e}")
#             client_socket.close()
#             start()


#     def receive(client_socket):
#         try:
#             data = b""
#             payload_size = struct.calcsize("Q")
#             while True:
#                 while len(data) < payload_size:
#                     packet = client_socket.recv(4 * 1024)  # 4K
#                     if not packet:
#                         break
#                     data += packet
#                 packed_msg_size = data[:payload_size]
#                 data = data[payload_size:]
#                 msg_size = struct.unpack("Q", packed_msg_size)[0]

#                 while len(data) < msg_size:
#                     data += client_socket.recv(4 * 1024)
#                 frame_data = data[:msg_size]
#                 data = data[msg_size:]
#                 frame = pickle.loads(frame_data)
#                 cv2.imshow("RECEIVING ", frame)

#                 key = cv2.waitKey(1) & 0xFF
#                 if key == ord('q'):
#                     client_socket.close()
#                     start()
#         except Exception as e:
#             print(f"Error receiving data: {e}")
#             client_socket.close()
#             start()
#     start()



import socket
import cv2
import pickle
import struct
import time

def cam3(port, ip):
    def start():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_ip = ip  # Paste your server IP address here

        try:
            client_socket.connect((host_ip, port))  # Attempt to establish the connection
            print("Connected to the server")
            receive(client_socket)
        except Exception as e:
            print(f"Connection failed: {e}")
            client_socket.close()
            start()

    def receive(client_socket):
        try:
            data = b""
            payload_size = struct.calcsize("Q")
            frame_count = 0
            start_time = time.time()

            while True:
                while len(data) < payload_size:
                    packet = client_socket.recv(4 * 1024)  # 4K
                    if not packet:
                        break
                    data += packet
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("Q", packed_msg_size)[0]

                while len(data) < msg_size:
                    data += client_socket.recv(4 * 1024)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)

                # Calculate FPS
                frame_count += 1
                elapsed_time = time.time() - start_time
                if elapsed_time >= 1:
                    frame_rate = frame_count / elapsed_time
                    frame_count = 0
                    start_time = time.time()

                # Add FPS text overlay on the frame
                fps_text = f"FPS: {frame_rate:.2f}"
                cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.imshow("RECEIVING-3", frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    client_socket.close()
                    start()

        except Exception as e:
            print(f"Error receiving data: {e}")
            client_socket.close()
            start()

    start()
