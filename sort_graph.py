
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Macで利用できる日本語フォントを探す
fonts = [
    "Hiragino Sans",
    "Hiragino Kaku Gothic ProN",
    "Yu Gothic",
    "Noto Sans CJK JP"
]

available_fonts = {font.name for font in font_manager.fontManager.ttflist}

for font in fonts:
    if font in available_fonts:
        plt.rcParams["font.family"] = font
        break

names = []
averages = []

# 実験結果のCSVを読み込む
with open("sort_results.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        names.append(row["アルゴリズム"])
        averages.append(float(row["平均値"]))

# 棒グラフを作成する
plt.figure(figsize=(10, 6))
plt.bar(names, averages)

plt.title("Average Number of Comparisons")
plt.xlabel("Sorting Algorithm")
plt.ylabel("Number of Comparisons")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()

# グラフを画像として保存する
plt.savefig("sort_average.png", dpi=300)
plt.show()


# 比較回数が少ない3種類だけを比較する
selected_names = []
selected_averages = []

for name, average in zip(names, averages):
    if name in [
        "マージソート",
        "クイックソート（軸固定）",
        "クイックソート（軸乱択）"
    ]:
        selected_names.append(name)
        selected_averages.append(average)

plt.figure(figsize=(9, 6))
plt.bar(selected_names, selected_averages)

plt.title("Average Number of Comparisons")
plt.xlabel("Sorting Algorithm")
plt.ylabel("Number of Comparisons")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()

plt.savefig("sort_average_detail.png", dpi=300)
plt.show()
