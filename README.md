# HEIC 批次轉換工具

將 HEIC/HEIF 格式照片批次轉換為 JPG 格式。

## 從 GitHub 取得並安裝

```bash
# 1. 複製專案
git clone https://github.com/<你的帳號>/heic-to-jpg.git
cd heic-to-jpg

# 2. 建立虛擬環境並安裝依賴
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 使用方式

```bash
# 基本用法：轉換後的 JPG 檔案會建立在原目錄
python heic_converter.py <輸入目錄>

# 指定輸出目錄
python heic_converter.py <輸入目錄> -o <輸出目錄>

# 調整 JPG 品質（1-100，預設 85）
python heic_converter.py <輸入目錄> -q 90

# 不遞迴搜尋子目錄
python heic_converter.py <輸入目錄> --no-recursive
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
