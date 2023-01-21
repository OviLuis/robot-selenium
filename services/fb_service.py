class FbService:
    
    def get_groups(self):
        file_name = 'groups.txt'
        groups = []
        with open(file_name, 'r') as file:
            line = file.readlines()
            groups.append(line)

        return groups
