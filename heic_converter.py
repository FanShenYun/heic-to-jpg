#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HEIC批次轉換工具
將HEIC格式照片批次轉換為JPG格式
"""

import os
import sys
import argparse
from pathlib import Path
from PIL import Image
import pillow_heif
from tqdm import tqdm

# 註冊HEIF格式支援
pillow_heif.register_heif_opener()

def convert_heic_to_jpg(input_path, output_path, quality=85):
    """
    將單個HEIC檔案轉換為JPG
    
    Args:
        input_path (str): 輸入HEIC檔案路徑
        output_path (str): 輸出JPG檔案路徑  
        quality (int): JPG品質 (1-100)
    
    Returns:
        bool: 轉換成功返回True，失敗返回False
    """
    try:
        # 開啟HEIC檔案
        with Image.open(input_path) as image:
            # 轉換為RGB模式（JPG不支援透明度）
            rgb_image = image.convert('RGB')
            # 儲存為JPG
            rgb_image.save(output_path, 'JPEG', quality=quality, optimize=True)
        return True
    except Exception as e:
        print(f"轉換失敗: {input_path} -> {e}")
        return False

def find_heic_files(directory):
    """
    在指定目錄中尋找所有HEIC檔案
    
    Args:
        directory (str): 搜尋目錄路徑
        
    Returns:
        list: HEIC檔案路徑清單
    """
    heic_files = []
    directory = Path(directory)
    
    # 支援的HEIC副檔名
    heic_extensions = ['.heic', '.HEIC', '.heif', '.HEIF']
    
    for ext in heic_extensions:
        heic_files.extend(directory.glob(f'**/*{ext}'))
    
    return heic_files

def batch_convert(input_dir, output_dir=None, quality=85, recursive=True):
    """
    批次轉換HEIC檔案
    
    Args:
        input_dir (str): 輸入目錄路徑
        output_dir (str): 輸出目錄路徑（預設為輸入目錄）
        quality (int): JPG品質
        recursive (bool): 是否遞迴搜尋子目錄
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"錯誤：輸入目錄不存在: {input_dir}")
        return
    
    # 設定輸出目錄
    if output_dir is None:
        output_path = input_path
    else:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    # 尋找所有HEIC檔案
    print("正在搜尋HEIC檔案...")
    if recursive:
        heic_files = find_heic_files(input_path)
    else:
        heic_files = []
        for ext in ['.heic', '.HEIC', '.heif', '.HEIF']:
            heic_files.extend(input_path.glob(f'*{ext}'))
    
    if not heic_files:
        print("未找到HEIC檔案")
        return
    
    print(f"找到 {len(heic_files)} 個HEIC檔案")
    
    # 批次轉換
    success_count = 0
    failed_count = 0
    
    for heic_file in tqdm(heic_files, desc="轉換進度"):
        # 產生輸出檔案名稱
        if output_dir is None:
            # 在原位置建立JPG檔案
            jpg_file = heic_file.with_suffix('.jpg')
        else:
            # 保持相對路徑結構
            rel_path = heic_file.relative_to(input_path)
            jpg_file = output_path / rel_path.with_suffix('.jpg')
            jpg_file.parent.mkdir(parents=True, exist_ok=True)
        
        # 執行轉換
        if convert_heic_to_jpg(str(heic_file), str(jpg_file), quality):
            success_count += 1
        else:
            failed_count += 1
    
    # 顯示結果
    print(f"\n轉換完成!")
    print(f"成功: {success_count} 個檔案")
    print(f"失敗: {failed_count} 個檔案")

def main():
    parser = argparse.ArgumentParser(
        description="HEIC批次轉換工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用範例:
  python heic_converter.py /path/to/photos
  python heic_converter.py /path/to/photos -o /path/to/output
  python heic_converter.py /path/to/photos -q 90 --no-recursive
        """
    )
    
    parser.add_argument(
        'input_dir',
        help='輸入目錄路徑（包含HEIC檔案）'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='輸出目錄路徑（預設為輸入目錄）'
    )
    
    parser.add_argument(
        '-q', '--quality',
        type=int,
        default=85,
        help='JPG品質 (1-100，預設85)'
    )
    
    parser.add_argument(
        '--no-recursive',
        action='store_true',
        help='不遞迴搜尋子目錄'
    )
    
    args = parser.parse_args()
    
    # 驗證品質參數
    if not 1 <= args.quality <= 100:
        print("錯誤：品質參數必須在1-100之間")
        return
    
    # 執行批次轉換
    batch_convert(
        input_dir=args.input_dir,
        output_dir=args.output,
        quality=args.quality,
        recursive=not args.no_recursive
    )

if __name__ == '__main__':
    main()