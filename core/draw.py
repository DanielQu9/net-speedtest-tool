"""輸出統計圖"""
import os
import time
import platform
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager
from matplotlib import get_cachedir


# 字體設定
font_path = './font/font.ttf'
find_font = True
plat = platform.system()
if os.path.exists(font_path):
    custom_font = font_manager.FontProperties(fname=font_path)
    font_manager.fontManager.addfont(font_path)
    rcParams['font.family'] = custom_font.get_name()
else:
    print('not find font')
    find_font = False
    if plat == 'Darwin':
        rcParams['font.family'] = 'Apple SD Gothic Neo'
    elif plat == 'Windows':
        rcParams['font.family'] = 'Microsoft JhengHei'
    
rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題


def draw(start_time, end_time, datas_1, datas_2):
    download_data = datas_1
    upload_data = datas_2
    
    # 計算平均值
    upload_avg = sum(upload_data) / len(upload_data)
    download_avg = sum(download_data) / len(download_data)

    # 設定圖表大小
    plt.figure(figsize=(10, 6))

    # 繪製折線圖
    plt.plot(range(1, len(upload_data) + 1), upload_data, marker="o", label="上傳數據", color="blue")
    plt.plot(range(1, len(download_data) + 1), download_data, marker="o", label="下載數據", color="orange")

    # 添加平均值的虛線
    plt.axhline(y=upload_avg, color="blue", linestyle="--", label="上傳平均值")
    plt.axhline(y=download_avg, color="orange", linestyle="--", label="下載平均值")

    # 添加標籤與標題
    plt.title("數據筆數內上傳與下載數據", fontsize=16)
    plt.xlabel("數據筆數", fontsize=14)
    plt.ylabel("數據量 (MB)", fontsize=14)

    # 隱藏 X 軸標籤
    plt.gca().xaxis.set_visible(False)

    # 標注開始和結束時間
    plt.text(0.5, -0.1, f"時間: {start_time} - {end_time}", fontsize=12, ha="center", transform=plt.gca().transAxes)
    # plt.text(0.5, -0.18, f"結束時間: {end_time}", fontsize=12, ha="center", transform=plt.gca().transAxes)

    # 添加圖例
    plt.legend(fontsize=12)

    # 添加格線
    plt.grid(True, linestyle="--", alpha=0.6)

    # 顯示圖表
    plt.tight_layout()
    build_imgdir()
    plt.savefig(f'./img/img_{get_time("%Y-%m-%d_%H-%M-%S")}')

def build_imgdir():
    if not os.path.isdir('./img'):
        os.mkdir('./img')

# 獲取當前時間
def get_time(_type="%Y-%m-%d %H:%M:%S"):
    return time.strftime(_type, time.localtime(time.time()))

def fix_font():
    # 清除字體緩存
    cache_dir = get_cachedir()
    print(cache_dir)
    cache_path = os.path.join(cache_dir, "fontlist-v390.json")
    if os.path.exists(cache_path):
        os.remove(cache_path)
        print(f"已刪除字體緩存: {cache_path}")
    else:
        print("無字體緩存可刪除")

def have_font():
    return find_font


if __name__ == '__main__':
    # print('do')
    # fix_font()
    draw('123', '456', [100, 97, 101], [50, 47, 45])