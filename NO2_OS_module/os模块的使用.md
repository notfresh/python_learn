- home目录

https://www.jianshu.com/p/a6592aae075d



- 存在或者创建

  ```
  import os
  print(os.environ['HOME'])
  
  dir = str(os.environ['HOME']) + os.sep + 'celery'
  
  print(dir)
  if not os.path.exists(dir):
      os.makedirs(dir)
  ```



