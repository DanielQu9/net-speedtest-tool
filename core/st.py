import speedtest

class SpeedTest:
    def __init__(self) -> None:
        self.st = speedtest.Speedtest()
        self.st.get_best_server()
        self.server_info = self.st.results.server
        self.client_info = self.st.results.client
        self.threads_tick = 8  # 增加測試執行緒
        self.unit_convert = 1_000_000
    
    def get_ping(self):
        """取得 Ping (延遲時間)"""
        return round(self.st.results.ping, 2)
    
    def get_download_speed(self):
        """測量下載速度 (Mbps)"""
        speed = self.st.download(threads=self.threads_tick) / self.unit_convert
        return round(speed, 2)
    
    def get_upload_speed(self):
        """測量上傳速度 (Mbps)"""
        speed = self.st.upload(threads=self.threads_tick) / self.unit_convert
        return round(speed, 2)
    
    def get_full_report(self, json_output=False):
        """
        執行完整測速並回傳結果。

        :param json_output: 若為 True，則回傳 JSON 格式
        :return: 測速結果（字典 或 JSON 字串）
        """
        download_speed = self.get_download_speed()
        upload_speed = self.get_upload_speed()
        ping = self.get_ping()

        result = {
            "ping": ping,
            "download_speed_mbps": download_speed,
            "upload_speed_mbps": upload_speed,
            "server": self.server_info["host"],
            "timestamp": self.st.results.timestamp,
            "client_ip": self.client_info["ip"]
        }

        return result
        

if __name__ == '__main__':
    print('start... v0.4')
    st = SpeedTest()
    print(st.get_full_report())
    print(st.server_info,"\n",st.client_info)
