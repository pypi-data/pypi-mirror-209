import os,sys
PROJ_DIR="/Users/qing/Library/Mobile Documents/com~apple~CloudDocs/workspace/Code/qdls"
sys.path.append(PROJ_DIR)
from src.qdls.gql.sparql.utils.syntax import syntax_check

s1 = "select ?x {?e ?p 'asd'}"

flag, tree, parser = syntax_check(s1)

print(flag)
print(type(tree))
print("error msg:", tree)