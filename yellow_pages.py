
categories=["bengkel","taxi","restoran","gym / fitness / yoga center","toko kain","info properti"]
data=[
	{
		"id":1,
		"category_id":1,
		"nama":"Bengkel A",
		"no_telp":"0812-1213-1211",
		"address":"Jln.Bengkel No.1211"
	},
	{
		"id":2,
		"category_id":2,
		"nama":"Taxi A",
		"no_telp":"0812-1213-0012",
		"address":"Jln.Taxi No.0012"
	},
	{
		"id":3,
		"category_id":3,
		"nama":"Restoran A",
		"no_telp":"0812-1213-9812",
		"address":"Jln.Restoran No.9812"
	},
	{
		"id":4,
		"category_id":4,
		"nama":"GYM A",
		"no_telp":"0812-1213-3112",
		"address":"Jln.Bengkel No.3112"
	},
	{
		"id":5,
		"category_id":5,
		"nama":"Toko Kain A",
		"no_telp":"0812-1213-9012",
		"address":"Jln.Toko Kain No.9012"
	},
	{
		"id":6,
		"category_id":6,
		"nama":"Property A",
		"no_telp":"0812-1213-1254",
		"address":"Jln.Bengkel No.1254"
	},
	{
		"id":7,
		"category_id":7,
		"nama":"Taxi B",
		"no_telp":"0812-1213-4123",
		"address":"Jln.Taxi No.4123"
	}
]
tab_status=True
while(tab_status):
	[print(f"	{index+1}.{category}") for index,category in enumerate(categories)]
	print(" 	0 for exit ")
	category_input=int(input("Mohon input kategori: "))
	if(category_input==0):
		break
	
	read_results=list(filter(lambda category: category["category_id"]==category_input,data))
	# print(len(read_results))
	
	
	if(len(read_results)>=1):
		print(f"List data dari kategori {categories[category_input-1]}")
		for a in range(0,len(read_results)):
			information=read_results[a]
			print(f"    {a+1}.  ID {information["id"]}	\n 	Nama {information['nama']} \n   	No Telp {information["no_telp"]} \n   	Address {information["address"]}")
	elif(len(read_results)==0):
		print("Data is 0, please select another category")
		input_decision=input(f"Do you want to create new data for {categories[category_input-1]} ( Yes/No)")
		if(input_decision=="Yes" or input_decision=="yes" or input_decision=="y"):
			print(f"Input data for {categories[category_input-1]}")
			last_id=data[-1]["id"]
			new_id=last_id+1
			nama=input(f"Please input nama:  ")
			no_telp=input(f"Please input No.Telp:	")
			address=input(f"Please input address:	")
			new_dict={"id":new_id,"category_id":category_input,"nama":nama,"no_telp":no_telp,"address":address}
			data.append(new_dict)
			print("Product successfully being created ")
			print(f"Nama : {nama} ,No.Telp {no_telp}	,Address{address}")
			
		else:
			break
	
	print("Please selects action")
	print("	1. Update \n	2. Delete  \n 	3. View 	\n 	4. Create \n 	5. Quit")
	action_input=input()
	list_of_name_id=[f"ID: {id["id"]}"for id in read_results]
	list_of_id=[id["id"] for id in read_results]
	if(action_input=="q"):
		break

	status_list_id=True
	if(int(action_input)==1):
		while(status_list_id):
			id_action=input(f"Please input the number for action {list_of_name_id}: or q for exit updating  ")
			updated_id=[]
			if(id_action=="q"):
				break
			
			if (int(id_action) in list_of_id):
				data_action=list(filter(lambda obj:obj["id"]==int(id_action),read_results))
				print(", ".join(f"{key}: {value}" for key, value in data_action[0].items()))
				status=True
				while(status):
					attribute_input=input("please input what attribute want to update (nama,no_telp,address) or q for exit:")
					if attribute_input=="nama":
					
						updated_data=input("Please input new data for name :")
						next(item.update({"nama": updated_data}) for item in data if item["id"] == data_action[0]["id"])
						print("nama successfully updated")
						print(data_action[0])
					
					elif attribute_input=="no_telp":
						updated_data=input("Please input new data for no_telp :")
						next(item.update({"no_telp": updated_data}) for item in data if item["id"] == data_action[0]["id"])
						print("no_telp successfully updated")
						print(data_action[0])
						
					elif attribute_input=="address":
						updated_data=input("Please input new data for address :")
						next(item.update({"address": updated_data}) for item in data if item["id"] == data_action[0]["id"])
						print("address successfully updated")
						print(data_action[0])
						
					elif attribute_input=="q":break
					else:
						continue
			elif(id_action=="q"):
				break
			else:
				
				print("Data inputted not found")
	elif(int(action_input)==2):
		delete_status=True
		while(delete_status):
			id_action=input(f"Please input the number for action {list_of_name_id}: or q for cancel  ")
			if(id_action=="q"):
				break
			data_action=list(filter(lambda obj:obj["id"]==int(id_action),read_results))
			
			if(int(id_action) in list_of_id):
				print(f"Are you sure want to delete data of {data_action} Yes/No")
				decision_action=input("")
				if(decision_action=="Yes" or decision_action=="yes" or decision_action=="y" or decision_action=="Y"):
					data = [item for item in data if item["id"] != int(id_action)]
					list_of_id.remove(int(id_action))
					print(f"Data ID {id_action} Successfuly deleted")
					print(read_results)
					break
	elif(int(action_input)==3):
		for item in read_results:
			print(f"ID: {item['id']}")
			print(f"Category ID: {item['category_id']}")
			print(f"Name: {item['nama']}")
			print(f"Phone Number: {item['no_telp']}")
			print(f"Address: {item['address']}")
	elif(int(action_input)==4):
		print(f"Input data for {categories[category_input-1]}")
		last_id=data[-1]["id"]
		new_id=last_id+1
		nama=input(f"Please input nama:  ")
		no_telp=input(f"Please input No.Telp:	")
		address=input(f"Please input address:	")
		new_dict={"id":new_id,"category_id":category_input,"nama":nama,"no_telp":no_telp,"address":address}
		data.append(new_dict)
		print("Product successfully being created ")
		print(f"Nama : {nama} ,No.Telp {no_telp}	,Address{address}")

	elif(int(action_input)==5):
		print("You successfully quit the program")
		print("See you later")
		break

















