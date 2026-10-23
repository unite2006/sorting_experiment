
import csv
import matplotlib.pyplot as plt

# Macの日本語フォントを設定
from matplotlib import font_manager

fonts = [
    "Hiragino Sans",
    "Hiragino Kaku Gothic ProN",
    "Yu Gothic",
    "Noto Sans CJK JP"
]
available_fonts = {
    font.name for font in font_manager.fontManager.ttflist
}
for font in fonts:
    if font in available_fonts:
        plt.rcParams["font.family"] = font
        break

# 全試行の比較回数を読み込む
with open("sort_all_results.csv", newline="",
          encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

algorithms = [
    "選択ソート",
    "挿入ソート",
    "マージソート",
    "クイックソート（軸固定）",
    "クイックソート（軸乱択）"
]

data = [
    [int(row[name]) for row in rows]
    for name in algorithms
]

# 箱ひげ図を作成
plt.figure(figsize=(11, 6))
plt.boxplot(data, tick_labels=algorithms, showfliers=True)

plt.title("ソートアルゴリズム別の比較回数の分布")
plt.xlabel("ソートアルゴリズム")
plt.ylabel("比較回数")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()

plt.savefig("sort_boxplot.png", dpi=300)
plt.show()



# マージソートとクイックソート2種類を比較
selected_names = [
    "マージソート",
    "クイックソート（軸固定）",
    "クイックソート（軸乱択）"
]

selected_data = [
    [int(row[name]) for row in rows]
    for name in selected_names
]

plt.figure(figsize=(9, 6))
plt.boxplot(selected_data, tick_labels=selected_names,
            showfliers=True)

plt.title("マージソートとクイックソートの比較回数")
plt.xlabel("ソートアルゴリズム")
plt.ylabel("比較回数")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()

plt.savefig("sort_boxplot_detail.png", dpi=300)
plt.show()
