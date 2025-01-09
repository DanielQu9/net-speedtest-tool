import speedtest

def __main():
    St = speedtest.Speedtest()
    St.get_servers()
    best = St.get_best_server()
    ping = St.results.ping
    unit = 1000000

    download_speed = St.download() / unit
    upload_speed = St.upload() / unit
    ping = St.results.ping

    print(download_speed)
    print(upload_speed)
    print(ping)

def DoTest():
    St = speedtest.Speedtest()
    St.get_servers()
    St.get_best_server()
    St.download()
    St.upload()
    # St.results.share()
    
    return St.results.dict()
    

if __name__ == '__main__':
    print(DoTest())
    # __main()
