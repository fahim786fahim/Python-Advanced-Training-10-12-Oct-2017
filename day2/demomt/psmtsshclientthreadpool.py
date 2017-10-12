import threading
from day2.oops.pscustomsshclient import CustomSSHClient
from csv import reader


class MTSSHClient:
    def __init__(self, host, port, user, passwd, cmd):
        self.host = host
        self.cmd = cmd
        self.ssh = CustomSSHClient(host, port, user, passwd)
        self.__run_command()

    def __run_command(self):
        t_name = threading.current_thread().getName()
        payload = self.ssh.check_output(self.cmd)
        print("{} ran {} @ {}".format(t_name, self.cmd, self.host))
        print(payload)

def main():
    threads = list()

    for host_record in reader(open('hosts.csv')):
        host_record[1] = int(host_record[1])
        t = threading.Thread(target=MTSSHClient, args=host_record)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # make to wait for the child to complete

    print('main thread terminates')


if __name__ == '__main__':
    main()
