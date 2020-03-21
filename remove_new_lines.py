import re
open('DearEsther2.txt','w').write(re.sub('\n{2}(?!\d)',' ',open('DearEsther.txt','r',encoding='utf8').read()))
