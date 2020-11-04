if __name__ == "__main__":
    obj_list_file = "data/Logo.names"
    with open(obj_list_file, "r") as f:
        obj_list = f.readlines()

    obj_list = [x.split("\n")[0] for x in obj_list]

    print(obj_list)
    print(len(obj_list))