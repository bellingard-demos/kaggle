import os

class User:
    def __init__(self, references_path="./references/kernels.txt", checked_users_path="./references/checked_users.txt"):
        self.references_path = references_path
        self.user_references = self.load_user_references()
        self.checked_users_path = checked_users_path
        self.checked_users = self.load_checked_users()

    def load_user_references(self):
        if not os.path.exists(self.references_path):
            return set()
        references = set()
        with open(self.references_path, "r") as fid:
            for line in fid:
                references.add(line.split("/")[0])
        return references

    def load_checked_users(self):
        if not os.path.exists(self.checked_users_path):
            return set()
        references = set()
        with open(self.checked_users_path, "r") as fid:
            for line in fid:
                references.add(line.strip())
        return references

    def print_list_of_users(self):
        for user in self.user_references:
            print(user)

    def get_list_of_users(self) -> set:
        return self.user_references

    def check_user(self, user_ref):
        with open(self.checked_users_path, "a") as fw:
            fw.write(user_ref + "\n")
            self.checked_users.add(user_ref)

    def is_checked(self, user_ref):
        if user_ref in self.checked_users:
            return True
        return False

if __name__ == "__main__":
    user = User()
    user.print_list_of_users()
