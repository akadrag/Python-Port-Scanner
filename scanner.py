import socket
import time

class Portscanner:
    def __init__(self,target,start_port=1,end_port=1924):
        self.target = socket.gethostbyname(target)
        self.start_port = start_port
        self.end_port = end_port

    def scan(self):
        try:
            print("=" * 45)
            print("        Python Port Scanner")
            print("=" * 45)
            print(f"Target : {self.target}")
            print(f"Ports  : {self.start_port} - {self.end_port}")
            print("=" * 45)

            start_time = time.time()

            for port in range(self.start_port,self.end_port + 1):
                self.scan_port(port)
        
            end_time = time.time()
            print(f"\nFinished in {end_time - start_time:.2f} seconds")
            print(f"\nScan Complete! Time taken: {end_time - start_time:.2f} seconds")
    
        except KeyboardInterrupt:
            print("\nScan Interrupted by user.")
    
        except socket.gaierror:
            print("\nHostname could not be resolved.")
        
        except Exception as e:
            print(f"\nUnexpected error: {e}")
    
    
    def scan_port(self,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((self.target,port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        
        s.close()

    