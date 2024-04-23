# CMPS 2200 Recitation 08

## Answers

**Name:**__Charles Zhang_
**Name:**__Yundan Yang___


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**


$W(E,V) = W(V) + W(E*log V) = O(V+Elog V)$

 
$S(E,V) = O(E)$  


- **2b)**



def get_path(parents, destination):

    path = []
    
    while parents[destination] is not None:
        path.append(parents[destination])
        destination = parents[destination]
    
    return ''.join(path[::-1])
