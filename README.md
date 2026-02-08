# HEIC 批次轉換工具

將 HEIC/HEIF 格式照片批次轉換為 JPG 格式。

## 從 GitHub 取得並安裝

```bash
# 1. 複製專案
git clone https://github.com/FanShenYun/heic-to-jpg.git
cd heic-to-jpg

# 2. 建立虛擬環境並安裝依賴
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 使用方式

```bash

# 指定輸出目錄
python heic_converter.py ./input -o ./output

```

## 參數說明

| 參數 | 說明 |
|------|------|
| `input_dir` | 輸入目錄路徑（包含 HEIC 檔案） |
| `-o`, `--output` | 輸出目錄路徑（預設為輸入目錄） |
| `-q`, `--quality` | JPG 品質，1-100（預設 85） |
| `--no-recursive` | 不遞迴搜尋子目錄 |

## 支援格式

`.heic`、`.HEIC`、`.heif`、`.HEIF`
