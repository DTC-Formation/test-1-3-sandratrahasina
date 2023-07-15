from json_interact import get_json_data
from json_interact import write_json_data
from datetime import datetime


while(True):
    user_connected = input("Iza ny anaranao ? :  ")
    all_task_data_user = get_json_data()

    all_users_data_list = all_task_data_user["users"]

    for user_task in all_users_data_list:
        if(user_task["nom_user"]==user_connected):
            all_this_user_data = user_task
            
            all_task_data_list = all_this_user_data["taches"]

            format_data = "%d/%m/%y"

            def show_day_difference(task_deadine):
                d1 = datetime.strptime(task_deadine, "%d/%m/%y")
                d2 = datetime.now()
                delta = d2 - d1
                return f'Mbola manana {delta.days} andro ianao hanaovana azy'

            while(True):
                option_menu = input("Tsindrio ny 1 raha hampiditra tache vaovao \nTsindrio ny 2 raha hijery io tache miandry anao \nTsindrio ny 3 raha hanisy fanovana \nTsindrio ny 4 raha hitahiry ireo fanovana rehetra natao \nTsindrio ny 5 raha hivoaka \nNy --- safidinao :  ")
                if(int(option_menu)==5):
                    print("Misaotra anao")
                    break

                if(int(option_menu)==1):
                    task_name = input("Ampidiro ny anaran'ilay tache : ")
                    task_dead_line = input("Ampidiro ny date tokony hahavitany jj/mm/aa : ")
                    new_task = {
                        "id": all_this_user_data["max_id"],
                        "nom": task_name, 
                        "deadline": datetime.strptime(task_dead_line, format_data), 
                        "statut": "En attente"
                    }
                    all_this_user_data["max_id"] = all_this_user_data["max_id"]+1
                    all_task_data_list.append(new_task)
                    print("Tafiditra soa aman'tsara ilay tache vaovao")
                    continue
                
                if(int(option_menu)==2):
                    for task in all_task_data_list:
                        print("id: " + task["id"])
                        print("nom: " + task["nom"])
                        print("deadline: " + show_day_difference(task["deadline"]))
                        print("statut: " + task["statut"])
                        print("----------------------------")
                    continue

                if(int(option_menu)==3):
                    task_id_to_update = input("Inona no numero an'ilay tache hasiana fanovana : ")
                    for task in all_task_data_list:
                        if task["id"] == task_id_to_update:
                            task["nom"] = input("Omeo anarana vaovao izy : ")
                            daty_vaovao = input("Omeo deadline vaovao izy jj/mm/aa : ")
                            task["deadline"] = datetime.strptime(daty_vaovao, format_data).strftime(format_data)
                            task["statut"] = input("Omeo statut vaovao izy : ")
                            break 

                    print("voaray soa aman'tsara ireo fanovana natao")
                    continue

                if(int(option_menu)==4):
                    write_json_data({
                        "taches" : all_task_data_list
                    })
                    print("Enregistrer soa amantsara ireo fanovana nataonao")
                    continue

    print("tsy mbola misy ny anaranao ato")   