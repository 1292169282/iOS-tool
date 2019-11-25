mv ${1} 1.zip
unzip 1.zip
cd Payload
cd $(ls)
cp embedded.mobileprovision ../../
cd ../../
security cms -D -i embedded.mobileprovision > 2.plist
#plutil -convert xml1 2.plist -o 2.xml
#plutil -convert json -s -r  -o 2.json 1.xml
#plutil -convert json 1.plist -o 1.json
python t0716.py
