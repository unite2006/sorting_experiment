
import csv
import random
import statistics


# 選択ソート
def selection_sort(data):
    a = data.copy()
    count = 0
    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            count += 1
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return count


# 挿入ソート
def insertion_sort(data):
    a = data.copy()
    count = 0
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0:
            count += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = key

    return count


# マージソート
def merge_sort(data):
    count = [0]

    def sort(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])

        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            count[0] += 1

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sort(data.copy())
    return count[0]


# クイックソート（先頭要素を軸に固定）
def quick_sort_fixed(data):
    a = data.copy()
    count = [0]

    def sort(low, high):
        if low >= high:
            return

        pivot = a[low]
        i = low + 1
        j = high

        while True:
            while i <= high:
                count[0] += 1
                if a[i] > pivot:
                    break
                i += 1

            while j > low:
                count[0] += 1
                if a[j] < pivot:
                    break
                j -= 1

            if i >= j:
                break

            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        a[low], a[j] = a[j], a[low]

        sort(low, j - 1)
        sort(j + 1, high)

    sort(0, len(a) - 1)
    return count[0]


# クイックソート（軸を乱択）
def quick_sort_random(data):
    a = data.copy()
    count = [0]

    def sort(low, high):
        if low >= high:
            return

        pivot_index = random.randint(low, high)
        a[low], a[pivot_index] = a[pivot_index], a[low]
        pivot = a[low]

        i = low + 1
        j = high

        while True:
            while i <= high:
                count[0] += 1
                if a[i] > pivot:
                    break
                i += 1

            while j > low:
                count[0] += 1
                if a[j] < pivot:
                    break
                j -= 1

            if i >= j:
                break

            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        a[low], a[j] = a[j], a[low]

        sort(low, j - 1)
        sort(j + 1, high)

    sort(0, len(a) - 1)
    return count[0]


# CSVファイルを読み込む
with open("sort_data.csv", newline="") as f:
    reader = csv.reader(f)
    datasets = [[int(x) for x in row] for row in reader]


algorithms = {
    "選択ソート": selection_sort,
    "挿入ソート": insertion_sort,
    "マージソート": merge_sort,
    "クイックソート（軸固定）": quick_sort_fixed,
    "クイックソート（軸乱択）": quick_sort_random,
}

results = {name: [] for name in algorithms}

# 各データに対して5種類を実行
for trial, data in enumerate(datasets, start=1):
    for name, algorithm in algorithms.items():
        comparisons = algorithm(data)
        results[name].append(comparisons)

    if trial % 100 == 0:
        print(f"{trial}回目まで完了")

# 統計量を表示し、CSVに保存
with open("sort_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["アルゴリズム", "最小値", "中央値", "平均値", "最大値"])

    for name, values in results.items():
        row = [
            name,
            min(values),
            statistics.median(values),
            statistics.mean(values),
            max(values),
        ]
        writer.writerow(row)

        print(
            f"{name}: "
            f"最小値={row[1]}, "
            f"中央値={row[2]}, "
            f"平均値={row[3]:.2f}, "
            f"最大値={row[4]}"
        )


# 1万回分の比較回数を保存する
with open("sort_all_results.csv", "w", newline="",
          encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["試行回数"] + list(algorithms.keys()))

    for i in range(len(datasets)):
        row = [i + 1]

        for name in algorithms:
            row.append(results[name][i])

        writer.writerow(row)

print("全試行の結果を sort_all_results.csv に保存しました。")


print("実験完了。結果は sort_results.csv に保存しました。")
