###################################################
# Copyright (c) 2025 DanielQu9
# This code is licensed under the MIT License.
# See LICENSE file for details.
###################################################

import time
from core.wait import wait
from core.seedtime import seed_time
from core.st import SpeedTest
from core.log import TestLog
from core.draw import draw, have_font


class TurnOffError(Exception):
    def __init__(self, messenger) -> None:
        super().__init__(messenger)

def main():
    # 輸入持續時間
    while True:
        try:
            end_time = seed_time(input('(輸入計時(單位 s/m/h/d))>> '))
            break
        except Exception as err:
            print(err)
            log.write_error(err)
        
    now_time = time.time()
    start_time = now_time
    rate: int = 1
    avg_download: (str | list | float) = ''
    avg_upload: (str | list | float) = ''
    error_sleepTime: int = 2
    
    log.add_str(f'start TestSpeed.', 'info')
    try:
        speed_data = SpeedTest()
        pg = speed_data.get_ping()
        log.add_str("get speedtest server.", 'event')
    except Exception as err:
        now_time = time.time()
        print(f"報錯 時間{strftime(now_time)}")
        print(f"error   : {err}\n")
        print(f"若出現403錯誤，請稍等後在測試。")
        
        log.write_error(err)
        raise TurnOffError('')
        
    while now_time <= end_time:
        try:
            # 在現在時間小於結束時間時，持續測速
            try:
                dl = speed_data.get_download_speed()
                ul = speed_data.get_upload_speed()
            except Exception as err:
                now_time = time.time()
                print(f"報錯 時間{strftime(now_time)}")
                print(f"error   : {err}\n")
                
                log.write_error(err)
                time.sleep(error_sleepTime)
            else:    
                now_time = time.time()
                
                _str = ''
                _str += f"第{rate}次 時間{strftime(now_time)}\n"
                _str += f"ping    : {pg:.2f}\n"
                _str += f"download: {dl:.2f} Mbps\n"
                _str += f"upload  : {ul:.2f} Mbps\n"
                
                log.add_str(f'rate: {rate}, ping: {pg:.2f}, download: {dl:.2f} Mbps, upload  : {ul:.2f} Mbps', 'event')
                print(_str)
                rate += 1
                
                # 紀錄歷史數值，用於繪圖與求平均
                avg_download += f"{dl},"
                avg_upload += f"{ul},"
                # time.sleep(10) # 休息10秒
        except KeyboardInterrupt: # ctrl c 例外處理
            print(f'已提前終止')
            log.add_str('提前終止 in st', 'warning')
            break
        
        except Exception as err:
            now_time = time.time()
            print(f"報錯 時間{strftime(now_time)}")
            print(f"error   : {err}\n")
            
            time.sleep(error_sleepTime)
            log.write_error(err)
    log.add_str(f'finish Speedtest.', 'info')
    
    if (avg_download != '') and (avg_upload != ''):
        # 結算所有歷史上下載數值
        avg_download = list(map(float, avg_download.split(',')[:-1]))
        avg_upload = list(map(float, avg_upload.split(',')[:-1]))
        
        # 將上述數值進行繪圖
        try:
            # 檢測有無加載字體
            if not have_font:
                log.add_pkg_str('draw.py', 'not find font. pls into "font" dir and put the "font.ttf". ', 'warning')
            draw(strftime(start_time), strftime(end_time), avg_download, avg_upload)
        except Exception as err:
            print(err)
            log.write_error(err)
            log.add_pkg_str('draw.py', 'img output fail.', 'warning')
        
        # 求平均
        avg_download = (sum(avg_download) / len(avg_download))
        avg_upload = (sum(avg_upload) / len(avg_upload))
        
        print(f'\n\n統計:\n平均下載: {avg_download:.2f}\n平均上傳: {avg_upload:.2f}')
        log.add_str(f'avg>> download: {avg_download:.2f}, upload: {avg_upload:.2f}', 'event')
    else:
        print(f"無請求到任何資料")
        log.add_str('no any data.', 'warning')
    
    log.add_str('main down.', 'info')

def strftime(t):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))

if __name__ == '__main__':
    log = TestLog('main.py')
    
    try:
        main()
    except KeyboardInterrupt:
        print(f'已提前終止')
        log.add_str('提前終止 in out', 'warning')
    except TurnOffError:
        pass
    
    log.add_str("Normal Down.", 'info')
    wait()