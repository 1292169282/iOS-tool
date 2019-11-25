cd ${1}
cp project.pbxproj ../
cd ..
plutil -convert json -s -r  -o converted.json project.pbxproj
#mv converted.json ../
python test12.py
