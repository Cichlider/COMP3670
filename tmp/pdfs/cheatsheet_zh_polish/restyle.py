from pathlib import Path
import re
p=Path('output/pdf/COMP3670_A4_duplex_cheatsheet_ZH.tex')
s=Path('tmp/pdfs/cheatsheet_zh_polish/before.tex').read_text()
s=s.replace('top=7mm,bottom=7mm,left=7mm,right=7mm','top=8mm,bottom=8mm,left=8mm,right=8mm')
s=s.replace('lmsans10-regular.otf','texgyreheros-regular.otf').replace('lmsans10-bold.otf','texgyreheros-bold.otf').replace('lmsans10-oblique.otf','texgyreheros-italic.otf')
s=s.replace('BoldFeatures={FontIndex=11}','BoldFeatures={FontIndex=7}')
s=s.replace(r'\setlength{\parskip}{1.0pt}',r'\setlength{\parskip}{2.0pt}')
s=s.replace(r'\setlength{\jot}{1.1pt}',r'\setlength{\jot}{1.5pt}')
s=s.replace('{HTML}{152E3A}','{HTML}{20343C}').replace('{HTML}{51616A}','{HTML}{68767C}').replace('{HTML}{B7C1C6}','{HTML}{C8D0D3}')
old=r'\newcommand{\sect}[1]{\par\vspace{2.8pt}{\color{ink}\fontsize{8.6}{9.7}\selectfont\bfseries #1}\par\vspace{1.1pt}}'
new=r'''\newcommand{\sect}[2]{\par\vspace{5.2pt}{\color{ink}\fontsize{8.4}{10}\selectfont\bfseries #1}\hspace{3pt}{\color{muted}\fontsize{5.9}{8.4}\selectfont #2}\par\vspace{2.3pt}}
\newcommand{\en}[1]{{\color{muted}\fontsize{5.95}{8.4}\selectfont\,(#1)}}'''
assert old in s;s=s.replace(old,new)
s=s.replace(r'\newcommand{\kw}[1]{\textbf{#1}}',r'\newcommand{\kw}[1]{{\color{ink}\bfseries #1}}')
s=s.replace(r'\textwidth-8mm',r'\textwidth-10mm')
s=s.replace(r'\fontsize{7.2}{8.7}',r'\fontsize{6.7}{8.4}')
s=s.replace(r'\setlength{\abovedisplayskip}{1.5pt}',r'\setlength{\abovedisplayskip}{2.1pt}')
s=s.replace(r'\setlength{\belowdisplayskip}{1.5pt}',r'\setlength{\belowdisplayskip}{2.1pt}')
s=s.replace(r'\setlength{\abovedisplayshortskip}{1pt}',r'\setlength{\abovedisplayshortskip}{1.5pt}')
s=s.replace(r'\setlength{\belowdisplayshortskip}{1pt}',r'\setlength{\belowdisplayshortskip}{1.5pt}')
s=s.replace(r'\begin{document}',r'\DeclareMathSizes{6.7}{7.0}{5.0}{4.0}'+'\n'+r'\begin{document}')
# Give Chinese keywords visual priority and render English terminology in quieter type.
pre,body=s.split(r'\begin{document}',1)
body=re.sub(r'\\sect\{([^{}]+?) / ([^{}]+)\}',lambda m:r'\sect{'+m.group(1)+'}{'+m.group(2)+'}',body)
def balanced_cmd(text,cmd,transform):
 out=[];pos=0;prefix='\\'+cmd+'{'
 while True:
  start=text.find(prefix,pos)
  if start<0:out.append(text[pos:]);break
  out.append(text[pos:start]);i=start+len(prefix);j=i;depth=1
  while depth:
   if text[j]=='{':depth+=1
   elif text[j]=='}':depth-=1
   j+=1
  out.append(transform(text[i:j-1]));pos=j
 return ''.join(out)
def term(t):
 m=re.fullmatch(r'(.*?)（([^（）]+)）([：:]?)',t,flags=re.S)
 if m and not re.search('[\u4e00-\u9fff]',m.group(2)):
  return r'\kw{'+m.group(1)+'}'+r'\en{'+m.group(2)+'}'+m.group(3)
 return r'\kw{'+t+'}'
body=balanced_cmd(body,'kw',term)
s=pre+r'\begin{document}'+body
# A compact editorial masthead, leaving a little more air before the columns.
s=s.replace(r'\fontsize{15}{16}',r'\fontsize{13}{15}')
s=s.replace(r'\fontsize{9}{11}',r'\fontsize{8.0}{10}')
s=s.replace(r'\fontsize{7.1}{8.5}',r'\fontsize{6.1}{8.0}')
s=s.replace(r'\hrule height .7pt',r'\hrule height .45pt')
s=s.replace('机器学习速查 / MACHINE LEARNING','机器学习速查  /  MACHINE LEARNING')
s=s.replace('中文版＋英文术语 / 内容与英文版对应 / 概率界与收敛结论均须满足所列条件','中文解释 · 英文术语 · 公式速查 / 概率界与收敛结论须满足所列条件')
p.write_text(s)
print('Restyled headings, English terminology, type sizes, leading, paragraph and equation spacing.')
