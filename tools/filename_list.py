import glob

"""
指定フォルダのファイルリストを取得する。（再帰）
"""
filename_list = glob.glob("C:\\GrepTool\\input\\**", recursive=True)

# ファイル書込み
path_w = 'C:\\GrepTool\\input\\list.txt'
with open(path_w, mode='w') as f:
    f.write('\n'.join(filename_list))
