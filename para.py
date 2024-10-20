import concurrent.futures
import time

# 定義函數A，包含一些耗時的計算，例如睡眠
def A(P, a, b, c, d, e, f, g, h, i):
    time.sleep(1)  # 模擬耗時操作，每次運算睡眠1秒
    result = (P + a) * (b - c) + (d / e) * (f ** g) - (h + i)
    return result

# 平行運算函數
def parallel_A(P_values, *other_params):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(A, P, *other_params) for P in P_values]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return results

# 序列運算函數
def sequential_A(P_values, *other_params):
    results = [A(P, *other_params) for P in P_values]
    return results

# 測試平行與序列運算
if __name__ == "__main__":
    P_values = [1, 2, 3, 4, 5]
    other_params = (10, 20, 5, 100, 50, 2, 3, 10, 5)
    
    # 計算平行運算的時間
    start_time = time.time()
    parallel_results = parallel_A(P_values, *other_params)
    parallel_time = time.time() - start_time
    print(f"Parallel Results: {parallel_results}, Time: {parallel_time:.2f} seconds")
    
    # 計算序列運算的時間
    start_time = time.time()
    sequential_results = sequential_A(P_values, *other_params)
    sequential_time = time.time() - start_time
    print(f"Sequential Results: {sequential_results}, Time: {sequential_time:.2f} seconds")
