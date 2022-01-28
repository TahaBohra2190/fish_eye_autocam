# **READ ME**

Prerequisites: 

Docker 

Commands to set up flask server :

1) ``docker build --tag <name> .``

2) ``docker run -d -p 5000:5000 <name>``

3) ``curl -F "file1=@<path/to/test_image.png>" -F "file2=@<path/to/perfect_image.png>" http://localhost:5000/<cam_id>``
  NOTE : Path for images can be absolute or relative
  
Response generated is a JSON Object.
