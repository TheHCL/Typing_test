import random,os,time,requests,json

url="https://random-words-api.vercel.app/word"

while True:

	x=requests.get(url)
	x=json.loads(x.text)
	x=x[0]['word'].lower()
	

	print(x)
	s_time=time.time()

	while input() !=x:
		s_time=time.time()
		os.system("cls")
		print(x)


	x=""
	os.system("cls")
	print("Spent : "+str(60/(time.time()-s_time))+" wpm.")