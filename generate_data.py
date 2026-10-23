import random
import csv

# データの個数
N = 1000

# 生成するデータの個数
TRIALS = 10000

with open("sort_data.csv", "w", newline="") as f:
    writer = csv.writer(f)

    for i in range(TRIALS):
        # 1～1000の整数を用意
        data = list(range(1, N + 1))

        # ランダムに並び替える
        random.shuffle(data)

        # CSVファイルに書き込む
        writer.writerow(data)

print("データ生成完了")
print("生成したデータ数:", TRIALS)
print("1データあたりの要素数:", N)
