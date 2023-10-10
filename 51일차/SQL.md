# 데이터 받아오는법
- sqlite> .mode csv
- sqlite> .import ../users.csv users
- sqlite> select count(*)
-    ...> from users;

