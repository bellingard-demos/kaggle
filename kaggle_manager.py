import os.path
from kernel import Kernel
from dataset import Dataset
from user import User

class Kaggle_manager:

    def __init__(self, project_dir, dataset_path="./references/dataset.txt", checked_dataset_path="./references/checked_dataset.txt", references_path="./references/kernels.txt"):
        self.project_dir = project_dir
        self.references_path = references_path
        self.dataset_path = dataset_path
        self.checked_dataset_path = checked_dataset_path

    def kernels_from_datasets(self):
        dataset = Dataset(self.dataset_path,self.checked_dataset_path)
        kernel = Kernel(self.project_dir)
        dataset_list = dataset.get_list_of_datasets()
        for dataset_ref in dataset_list:
            if not dataset.is_checked(dataset_ref):
                print(f"Search for kernels with dataset {dataset_ref}")
                kernel.download_list_of_kernels_by_dataset(dataset_ref)
                dataset.check_dataset(dataset_ref)
            else:
                print(f"dataset {dataset_ref} is already checked")

    def kernels_from_users(self):
        users_instance = User(self.references_path)
        kernel = Kernel(self.project_dir)
        users_list = users_instance.get_list_of_users()
        users_num = len(users_list)
        counter = 0
        for user_ref in users_list:
            counter = counter + 1
            print(f"*** Get data for user {counter} out of {users_num}")
            if not users_instance.is_checked(user_ref):
                print(f"Search for kernels with user {user_ref}")
                kernel.download_list_of_kernels_by_user(user_ref)
                users_instance.check_user(user_ref)
            else:
                print(f"user {user_ref} is already checked")
            #break

    def all_kernels(self):
        kernel = Kernel(self.project_dir)
        kernel.download_kernels()


if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.realpath(__file__))
    kaggle_manager = Kaggle_manager(project_dir)
    #kaggle_manager.kernels_from_datasets()
    #kaggle_manager.kernels_from_users()
    kaggle_manager.all_kernels()
