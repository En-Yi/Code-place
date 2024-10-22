import concurrent.futures
import threading
import time

# 定義全局字典來存儲結果
shared_dict = {}
# 創建一個鎖
lock = threading.Lock()

# 定義函數A，包含一些耗時操作並更新共享字典
def A(P, a, b, c, d, e, f, g, h, i):
    time.sleep(1)  # 模擬耗時操作
    result = (P + a) * (b - c) + (d / e) * (f ** g) - (h + i)
    
    # 嘗試獲取鎖
    print(f"Thread with P={P} is trying to acquire the lock.")
    
    # 獲取鎖並更新共享字典
    with lock:
        print(f"Thread with P={P} has acquired the lock.")
        shared_dict[P] = result
        print(f"Thread with P={P} updated shared_dict and will now release the lock.")
    
    return result

# 用來進行平行運算的函數
def parallel_A(P_values, *other_params):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(A, P, *other_params) for P in P_values]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return results

# 主程式入口，測試範例
if __name__ == "__main__":
    P_values = [1, 2, 3, 4, 5]
    other_params = (10, 20, 5, 100, 50, 2, 3, 10, 5)

    # 呼叫平行運算函數，帶入P_values及其他參數
    results = parallel_A(P_values, *other_params)

    # 輸出結果
    print("Parallel Results:", results)
    print("Shared Dictionary:", shared_dict)
