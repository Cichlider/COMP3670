from pathlib import Path
import re
src=Path('output/pdf/COMP3670_A4_duplex_cheatsheet.tex').read_text()
pre=src.split('\\begin{document}')[0]
pre=pre.replace('\\usepackage[T1]{fontenc}\n','')
pre=pre.replace('\\usepackage{lmodern,amsmath,amssymb,mathtools,microtype,xcolor}',r'''\usepackage{amsmath,amssymb,mathtools,microtype,xcolor,fontspec,xeCJK}
\setsansfont{lmsans10-regular.otf}[BoldFont=lmsans10-bold.otf,ItalicFont=lmsans10-oblique.otf]
\setmainfont{lmsans10-regular.otf}[BoldFont=lmsans10-bold.otf,ItalicFont=lmsans10-oblique.otf]
\setCJKmainfont{PingFang.ttc}[Path=/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/,FontIndex=3,BoldFont=PingFang.ttc,BoldFeatures={FontIndex=11}]
\setCJKsansfont{PingFang.ttc}[Path=/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/,FontIndex=3,BoldFont=PingFang.ttc,BoldFeatures={FontIndex=11}]
\xeCJKsetup{CJKmath=true}''')
pre=pre.replace(r'\fontsize{7.0}{8.0}',r'\fontsize{7.4}{9.1}')
pre=pre.replace('MACHINE LEARNING','机器学习速查 / MACHINE LEARNING')
pre=pre.replace('A4 / 100\\% / duplex, long-edge','A4 / 100\\% / 双面长边翻转')
eqs={k:re.findall(r'\\\[(.*?)\\\]',b,re.S) for k,b in re.findall(r'\\begin\{sheetcol\}\{\\([A-Z])\}(.*?)\\end\{sheetcol\}',src,re.S)}
body=Path('tmp/pdfs/cheatsheet_zh/content.txt').read_text()
chunks=re.split(r'^=== ([A-Z]) ===\s*$',body,flags=re.M)
parts=[pre,'\\begin{document}\n']
for i in range(1,len(chunks),2):
 key,chunk=chunks[i],chunks[i+1]
 ids=list(map(int,re.findall(r'\\EQ\{(\d+)\}',chunk)))
 assert ids==list(range(1,len(eqs[key])+1)),(key,ids,len(eqs[key]))
 def expand(m):
  eq=eqs[key][int(m.group(1))-1]
  eq=eq.replace(r'\text{excess over Bayes}',r'\text{Bayes 超额风险}')
  return '\\['+eq+'\\]'
 chunk=re.sub(r'\\EQ\{(\d+)\}',expand,chunk)
 parts.append('\\begin{sheetcol}{\\'+key+'}\n'+chunk.strip()+'\n\\end{sheetcol}\n')
 print(key,len(eqs[key]),'display equations preserved')
end=src[src.index('\\typeout{COL-A='):]
end=end.replace('LEARNING / STATISTICS / MODELS / CLUSTERING / ORTHONORMAL GEOMETRY','学习 / 统计 / 模型 / 聚类 / 标准正交几何')
end=end.replace('SVM / SVD / SECOND-ORDER TESTS / OPTIMISATION / NEURAL NETWORKS / OPTIMIZERS','SVM / SVD / 二阶检验 / 优化 / 神经网络 / 优化器')
end=end.replace('Selected course notes / L1--4, 5b, 8a--b, 9--12 and LA5--8 / bounds assume their stated conditions','中文版＋英文术语 / 内容与英文版对应 / 概率界与收敛结论均须满足所列条件')
end=end.replace('Notation: unqualified norms are Euclidean / $I$ is identity / optimizer conventions follow Lecture 12','未注明范数均为欧氏范数 / $I$ 为单位矩阵 / 优化器符号约定沿用 Lecture 12')
parts.append(end)
Path('output/pdf/COMP3670_A4_duplex_cheatsheet_ZH.tex').write_text('\n'.join(parts))
