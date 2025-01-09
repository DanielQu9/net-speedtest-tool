import time
import re


def seed_time(seed_time) -> float:
        """
        根據輸入的 seed_time 計算時間戳記。
        支援字典格式、單一整數和字串格式。
        """
        unit_seconds = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}
        current_time = time.time()

        if isinstance(seed_time, dict):
            total_seconds = sum(value * unit_seconds[key] for key, value in seed_time.items() if key in unit_seconds)
            return current_time + total_seconds

        elif isinstance(seed_time, int):
            return seed_time

        elif isinstance(seed_time, str):
            # 解析字串格式，提取數值和單位
            matches = re.findall(r'(\d+)([dhms])', seed_time.lower())
            if not matches:
                raise ValueError(">> 格式錯誤。範例: '1h30m', '5s'")

            total_seconds = sum(int(value) * unit_seconds[unit] for value, unit in matches)
            return current_time + total_seconds

        else:
            raise ValueError(">> Invalid seed_time format. Use a dictionary, integer, or string.")