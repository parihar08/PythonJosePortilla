f = open('ZipUnzipDemo/file1.txt','w+')
f.write('ONE FILE')
f.close()

f = open('ZipUnzipDemo/file2.txt','w+')
f.write('TWO FILE')
f.close()

f = open('ZipUnzipDemo/file3.txt','w+')
f.write('THREE FILE')
f.close()

f = open('ZipUnzipDemo/file4.txt','w+')
f.write('FOUR FILE')
f.close()

f = open('ZipUnzipDemo/file5.txt','w+')
f.write('FIVE FILE')
f.close()

print('****************ZIPPING FILES************************','\n')
#We can use zipfile module to compress the zip files

import zipfile

compressed_file = zipfile.ZipFile('ZipUnzipDemo/compressed_file.zip','w')

compressed_file.write('ZipUnzipDemo/file1.txt',compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('ZipUnzipDemo/file2.txt',compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('ZipUnzipDemo/file3.txt',compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('ZipUnzipDemo/file4.txt',compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('ZipUnzipDemo/file5.txt',compress_type=zipfile.ZIP_DEFLATED)

compressed_file.close()

print('****************EXTRACT ITEMS FROM ZIP FILE************************','\n')

zip_obj = zipfile.ZipFile('ZipUnzipDemo/compressed_file.zip','r')
#For Extracting specific file
#zip_obj.extract('file1.txt')
#For Extracting everything to extracted_content folder
zip_obj.extractall('ZipUnzipDemo/extracted_content/')

print('*****************TO ARCHIVE ENTIRE FOLDER USING SHUTIL***********************','\n')
#Shell Utility library is better way for doing this

#Point out a directory that we to turn into a zip file
#Let's turn extracted_content folder into a zip file

import shutil

dir_to_zip = '/Users/Parihar08/PycharmProjects/PythonJosePortilla/ZipUnzipDemo/extracted_content'
output_filename = 'ZipUnzipDemo/example'
shutil.make_archive(output_filename,'zip',dir_to_zip)

print('**********EXTRACT CONTENTS FROM ZIPPED FOLDER USING SHUTIL**********','\n')

shutil.unpack_archive('ZipUnzipDemo/example.zip','ZipUnzipDemo/final_unzip','zip')