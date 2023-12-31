Proje 3
[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.

Binary Search Tree (BST) aşamaları şu şekildedir:

7 -> Root olarak eklenir.
5, 1, 8, 3, 6, 0, 9, 4, 2 sırasıyla eklenir.
Aşama aşama BST oluşumu:

7 (Root)
5 (Root'un solunda)
1 (5'in solunda)
8 (7'nin sağına)
3 (1'in sağına)
6 (3'ün sağına)
0 (1'in soluna)
9 (8'in sağına)
4 (3'ün sağına)
2 (4'ün soluna)
BST ağacı şu şekildedir:

        7
       / \
      5   8
     / \   \
    1   6   9
   / \
  0   3
     / \
    2   4

