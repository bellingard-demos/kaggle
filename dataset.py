import os
import time
from kaggle_downloader import kaggle_downloader

class Dataset:
    def __init__(self, dataset_references_path="./references/dataset.txt", checked_dataset_references_path="./references/checked_dataset.txt"):
        self.dataset_references_path = dataset_references_path
        self.checked_dataset_references_path = checked_dataset_references_path
        self.dataset_references = self.load_dataset_references()
        self.checked_dataset_references = self.load_checked_dataset_references()
        self.delay = 5
        self.downloader = kaggle_downloader()
        self.sortby = ['hottest', 'votes', 'updated', 'active', 'published']

    def load_dataset_references(self):
        if not os.path.exists(self.dataset_references_path):
            return []
        references = []
        with open(self.dataset_references_path, "r") as fid:
            for line in fid:
                references.append(line.strip())
        return references

    def load_checked_dataset_references(self):
        if not os.path.exists(self.checked_dataset_references_path):
            return []
        references = []
        with open(self.checked_dataset_references_path, "r") as fid:
            for line in fid:
                references.append(line.strip())
        return references

    def add_dataset_references(self, new_references):
        with open(self.dataset_references_path, "a") as fw:
            for ref in new_references:
                if ref not in self.dataset_references:
                    self.dataset_references.append(ref)
                    fw.write(ref + "\n")

    def download_list_of_datasets_by_sort(self, sortid: int):
        pid = 0
        while True:
            pid = pid + 1
            responses = self.downloader.download_list_of_datasets(pid,self.sortby[sortid])
            if len(responses) == 0:
                break
            references = []
            for r in responses:
                references.append(vars(r)['ref'])
            time.sleep(self.delay)
            self.add_dataset_references(references)

    def check_dataset(self, dataset_ref):
        with open(self.checked_dataset_references_path, "a") as fw:
            fw.write(dataset_ref + "\n")
            self.checked_dataset_references.append(dataset_ref)

    def is_checked(self, dataset_ref):
        if dataset_ref in self.checked_dataset_references:
            return True
        return False

    def  get_list_of_datasets(self):
        return self.dataset_references

if __name__ == "__main__":
    dataset = Dataset()
    for i in range(len(dataset.sortby)):
        dataset.download_list_of_datasets_by_sort(i)
