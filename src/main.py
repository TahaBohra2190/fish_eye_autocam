r"""
[Summary]
This is the old main.py file, the start file
This file is used to test the functions by running this file in command prompt by typing the
following command 
main.py, camid, test_img_path,perfect_img_path

use relative path
python main.py --camid 1 --image1test autocameratest2\data\TestImages\bluecolortint.png --image2perfect autocameratest2\data\TestImages\perfect.png

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]

curl -F "file1=@D:\El Code\autocameratest2\data\TestImages\bluecolortint.png" -F "file2=@D:\El Code\autocameratest2\data\TestImages\perfect.png" http://localhost:5000/1



"""
# from report import *
# from imgtests import *
# from configmain import *
# import argparse

# #def main()-> None:
#     #start_setup()
# parser = argparse.ArgumentParser()

# parser.add_argument('--id', type=str, required = True)
# parser.add_argument('--test', type=str, required=True)
# parser.add_argument('--perfect', type=str, required=True)
# args = parser.parse_args()
# test_results = generate_report(args.id, args.test, args.perfect)
# test_names = ['CamId','Blur','scale','noise','scrolled','allign','mirror','blackspots','ssim_score','brisque_score']
# #test_names = ['CamId','Blur','scale','noise','scrolled','allign','mirror','blackspots','ssim_score']
# for i in range(0,len(test_names)):
#     print(f"{test_names[i]}: {test_results[i]}")    
 
from re import X
from flask import Flask
from flask import request
from report import *
from imgtests import *
from configmain import *
import json
import pathlib 
import os


test_names = ['CamId', 'Blur', 'scale', 'noise', 'scrolled',
              'allign', 'mirror', 'blackspots', 'ssim_score', 'brisque_score']

app = Flask(__name__)


@app.route('/')
def Main():
    f = open(BASE_PATH.joinpath("LICENSE"), "r")
    print(f.read())
    return f.read()


@app.route('/<id>', methods=['POST'])
def call(id):
    file1 = request.files['file1']
    file2 = request.files['file2']
    file1.save("file1.png")
    file2.save("file2.png")
    
    file_path1 = BASE_PATH.joinpath("src","file1.png").as_posix()
    file_path2 = BASE_PATH.joinpath("src","file2.png").as_posix()

    results = generate_report(id, file_path1, file_path2)
    response = json.dumps({test_names[i]: results[i]
                          for i in range(len(test_names))})
    os.remove("file1.png")
    os.remove("file2.png")
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

